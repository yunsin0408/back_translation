"""md_to_kg_to_xml.py

Environment-driven pipeline:
- Configure via env vars:
  - LLM_API_ENDPOINT (required)
  - MD_INPUT_FOLDER or MD_INPUT_FILE (one required)
- Processes a file or all markdown files in a folder
- Builds a KG and sends it + markdown to the LLM endpoint
- Saves XML outputs under ./kg_xml/

This minimal script avoids model-specific fields and sends an OpenAI-style messages array.
"""

from __future__ import annotations
import os
import re
import json
import requests
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
import networkx as nx

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=False)
from lxml import etree

from validator import validate_xml as external_validate_xml


# --- utilities ---

def read_markdown(md_path: str) -> str:
    p = Path(md_path)
    if not p.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    return p.read_text(encoding="utf-8")


def split_to_text_units(md: str) -> List[Dict[str, str]]:
    lines = md.splitlines()
    units: List[Dict[str, str]] = []
    cur_heading = "Document"
    cur_text_lines: List[str] = []
    header_rx = re.compile(r"^#{1,6}\s+(.*)")
    for ln in lines:
        m = header_rx.match(ln)
        if m:
            if cur_text_lines:
                units.append({"heading": cur_heading, "text": "\n".join(cur_text_lines).strip()})
            cur_heading = m.group(1).strip()
            cur_text_lines = []
        else:
            cur_text_lines.append(ln)
    if cur_text_lines:
        units.append({"heading": cur_heading, "text": "\n".join(cur_text_lines).strip()})
    units = [u for u in units if u.get("text")]
    return units


def candidate_entities_from_text(text: str) -> List[str]:
    entities = set()
    for match in re.finditer(r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)", text):
        entities.add(match.group(1).strip())
    for match in re.finditer(r"\b([A-Z]{2,}|[A-Z][a-z]{3,})\b", text):
        entities.add(match.group(1).strip())
    for match in re.finditer(r"\b([A-Za-z0-9\-]+)\s+(?:of|for)\b", text, flags=re.I):
        if len(match.group(1)) > 2:
            entities.add(match.group(1).strip())
    clean = []
    for e in entities:
        e2 = re.sub(r"\s+", " ", e).strip()
        if len(e2) > 1:
            clean.append(e2)
    return clean


def build_knowledge_graph(units: List[Dict[str, str]]) -> Dict[str, Any]:
    nodes: Dict[str, Dict[str, Any]] = {}
    edges: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for uid, unit in enumerate(units, start=1):
        heading = unit["heading"]
        text = unit["text"]
        nodes.setdefault(heading, {"label": heading, "type": "heading", "source_units": []})
        nodes[heading]["source_units"].append(uid)
        cands = candidate_entities_from_text(heading + "\n" + text)
        for ent in cands:
            nodes.setdefault(ent, {"label": ent, "type": "candidate", "source_units": []})
            nodes[ent]["source_units"].append(uid)
        for ent in cands:
            key = (heading, ent) if heading <= ent else (ent, heading)
            e = edges.setdefault(key, {"weight": 0, "units": set()})
            e["weight"] += 1
            e["units"].add(uid)
    edges_list = []
    for (a, b), info in edges.items():
        edges_list.append({"source": a, "target": b, "weight": info["weight"], "units": list(info["units"])})
    nodes_list = []
    for k, v in nodes.items():
        nodes_list.append({"id": k, "label": v["label"], "type": v["type"], "source_units": v["source_units"]})
    kg = {"nodes": nodes_list, "edges": edges_list}
    
    from networkx.readwrite import json_graph
    G = nx.Graph()
    for n in nodes_list:
        G.add_node(n["id"], **{"label": n["label"], "type": n["type"]})
    for e in edges_list:
        G.add_edge(e["source"], e["target"], weight=e.get("weight", 1), units=e.get("units", []))
    kg["nx_graph"] = json_graph.node_link_data(G)
    return kg


# --- LLM call ---

def call_llm_with_kg(llm_url: str, prompt: str, kg: Dict[str, Any], md_text: str, out_dir: Optional[Path] = None) -> str:
    if not llm_url:
        raise ValueError("LLM_API_ENDPOINT (llm_url) is required.")
    kg_for_json = dict(kg)
    if "nx_graph" in kg_for_json and not isinstance(kg_for_json["nx_graph"], (dict, list, str, int, float, bool)):
        del kg_for_json["nx_graph"]
    headers = {"Content-Type": "application/json"}

    # Stronger, explicit system prompt to force the model to consult the KG
    system_msg = (
        "You are an expert XML generator. You MUST use the provided Knowledge Graph (KG) as the PRIMARY source of structuralinformation when reconstructing the XML.\n"
        "Instructions:\n"
        "- ALWAYS consult the KG and prioritize node/edge relationships when deciding element nesting and attributes.\n"
        "- Return ONLY well-formed XML, with no surrounding commentary, no markdown fences, and no extra text.\n"
        "- If any information is ambiguous between the markdown and the KG, prefer the KG and document nothing in the output other than XML.\n"
        "- Start the response with '<?xml' and end with the final closing tag.\n"
    )

    # Build the chat-style payload. Use temperature=0.0 for deterministic output.
    data = {
        "model": "gemma3:27b",
        "messages": [
            {"role": "system", "content": system_msg},
            {
                "role": "user",
                "content": json.dumps({"kg": kg_for_json, "markdown": md_text}, ensure_ascii=False) + "\n\n" + prompt,
            },
        ],
        "temperature": 0.7
    }

    # Save outgoing payload for inspection. If caller provides out_dir, use it (per-attempt).
    try:
        from urllib.parse import urlparse
        parsed = urlparse(llm_url)
        host_tag = parsed.netloc.replace(":", "_") if parsed.netloc else "llm"
    except Exception:
        host_tag = "llm"
    try:
        save_dir = out_dir if out_dir is not None else (Path.cwd() / "kg_xml2" / "payload")
        save_dir.mkdir(parents=True, exist_ok=True)
        payload_path = save_dir / f"payload_{host_tag}.json"
        payload_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved outgoing payload to {payload_path}")
    except Exception as e:
        print(f"Warning: failed to save outgoing payload: {e}")

    resp = requests.post(llm_url, json=data, headers=headers, timeout=600)
    try:
        resp.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"LLM request failed: {e} - {resp.text}")
    try:
        data = resp.json()
    except ValueError:
        return resp.text
    if isinstance(data, dict) and "choices" in data and isinstance(data["choices"], list) and len(data["choices"]) > 0:
        choice = data["choices"][0]
        if isinstance(choice, dict):
            if "message" in choice and isinstance(choice["message"], dict) and "content" in choice["message"]:
                return choice["message"]["content"]
            if "text" in choice:
                return choice["text"]
    if isinstance(data, dict) and "text" in data:
        return data["text"]
    return json.dumps(data, ensure_ascii=False)


# --- XML validation & fix helper ---


def validate_xml_string(xml_content: str) -> tuple[bool, str]:
    """Return (is_valid, message). Uses lxml strict parsing and collects errors when possible."""
    try:
        if isinstance(xml_content, str):
            xml_bytes = xml_content.encode("utf-8")
        else:
            xml_bytes = xml_content
        parser = etree.XMLParser(recover=False)
        etree.fromstring(xml_bytes, parser=parser)
        return True, "Valid XML"
    except (etree.XMLSyntaxError, etree.ParseError) as e:
        # try to get recover parser logs
        recover_parser = etree.XMLParser(recover=True)
        try:
            etree.fromstring(xml_bytes, parser=recover_parser)
        except Exception:
            pass
        errors = []
        if hasattr(recover_parser, "error_log"):
            for err in recover_parser.error_log:
                errors.append(f"Line {err.line}, Col {err.column}: {err.message}")
        if not errors:
            errors = [str(e)]
        return False, "\n".join(errors)
    except Exception as e:
        return False, str(e)


def fix_xml_with_errors(
    llm_url: str,
    kg: Dict[str, Any],
    md_text: str,
    previous_xml: str,
    error_log: str,
    max_retries: int = 5,
    out_dir: Optional[Path] = None,
) -> Optional[str]:
    """Attempt to fix `previous_xml` using the KG and the provided error_log by calling the LLM up to max_retries.

    Returns the first valid XML string or None if all attempts fail.
    Side effects: writes attempts to out_dir/jsons/<stem>_fix_attempt_<i>.XML and prints progress.
    """
    if out_dir is None:
        out_dir = Path.cwd() / "kg_xml2"
    json_subdir = out_dir / "jsons"
    json_subdir.mkdir(parents=True, exist_ok=True)

    # Short prompt that instructs the model to correct the provided XML using the KG.
    fix_prompt_template = (
        "You were previously asked to generate XML. The model's output failed validation.\n"
        "Use the provided Knowledge Graph (KG) and the attached error log to produce a corrected, well-formed XML document.\n"
        "Inputs available:\n"
        "- KG (node/edge list) which you MUST consult for structure and nesting.\n"
        "- The previously generated XML (PREVIOUS_XML).\n"
        "- The parser error log (ERROR_LOG) describing syntactic problems.\n"
        "Task:\n"
        "- Return ONLY the corrected XML document. Do not include any explanation.\n"
        "- Fix all syntax errors mentioned in ERROR_LOG.\n"
        "- Ensure the output starts with '<?xml' and is well-formed.\n"
    )

    for attempt in range(1, max_retries + 1):
        prompt = (
            fix_prompt_template
            + "\nERROR_LOG:\n"
            + error_log
            + "\n\nPREVIOUS_XML:\n"
            + previous_xml
            + "\n\nProvide the corrected XML now."
        )

        print(f"Fix attempt {attempt}/{max_retries} - calling LLM to correct XML...")
        try:
            model_output = call_llm_with_kg(llm_url=llm_url, prompt=prompt, kg=kg, md_text=md_text)
        except Exception as e:
            print(f"LLM call failed on attempt {attempt}: {e}")
            model_output = None

        if not model_output:
            continue

        # Create per-attempt folder and save inputs + output there for easy inspection
        attempt_dir = json_subdir / f"attempt_{attempt}"
        attempt_dir.mkdir(parents=True, exist_ok=True)
        try:
            (attempt_dir / "previous_xml.XML").write_text(previous_xml, encoding="utf-8")
            (attempt_dir / "error_log.txt").write_text(error_log, encoding="utf-8")
            (attempt_dir / "prompt.txt").write_text(prompt, encoding="utf-8")
        except Exception as e:
            print(f"Warning: failed to save attempt inputs for attempt {attempt}: {e}")

        # Call LLM and instruct it to save payload into the attempt folder as well
        try:
            model_output = call_llm_with_kg(llm_url=llm_url, prompt=prompt, kg=kg, md_text=md_text, out_dir=attempt_dir)
        except Exception as e:
            print(f"LLM call failed on attempt {attempt}: {e}")
            model_output = None

        if not model_output:
            continue

        # Save attempt output
        attempt_path = attempt_dir / f"fix_attempt.XML"
        try:
            attempt_path.write_text(model_output, encoding="utf-8")
            print(f"Saved fix attempt {attempt} to {attempt_path}")
        except Exception as e:
            print(f"Warning: failed to save fix attempt {attempt}: {e}")

        # Validate the returned XML using the external validator if available
        try:
            if external_validate_xml is not None:
                is_valid, message = external_validate_xml(model_output)
            else:
                is_valid, message = validate_xml_string(model_output)
        except Exception as e:
            is_valid = False
            message = f"Validation invocation failed: {e}"

        if is_valid:
            print(f"Fix attempt {attempt} produced valid XML.")
            return model_output

        # Not valid: save the new error log and use it for the next attempt
        print(f"Fix attempt {attempt} did not validate: {message}")
        try:
            (attempt_dir / "error_log_after_attempt.txt").write_text(message, encoding="utf-8")
        except Exception as e:
            print(f"Warning: failed to save post-attempt error log: {e}")

        # Prepare for next attempt: the previous_xml becomes this model_output and error_log becomes the latest parser message
        previous_xml = model_output
        error_log = message

    print(f"All {max_retries} fix attempts failed to produce valid XML.")
    return None


# --- generator ---


def generate_xml_from_markdown(md_path: str, llm_url: str, out_xml_path: Optional[str] = None) -> str:
    md_text = read_markdown(md_path)
    units = split_to_text_units(md_text)
    kg = build_knowledge_graph(units)

    # Persist KG for debugging and later reuse (save JSONs into kg_xml/jsons)
    kg_dir = Path.cwd() / "kg_xml2"
    kg_dir.mkdir(parents=True, exist_ok=True)
    json_subdir = kg_dir / "jsons"
    json_subdir.mkdir(parents=True, exist_ok=True)
    stem = Path(md_path).stem
    kg_json_path = json_subdir / f"{stem}_kg.json"
    try:
        kg_json_path.write_text(json.dumps(kg, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved KG JSON to {kg_json_path}")
    except Exception as e:
        print(f"Warning: failed to save KG JSON: {e}")
    if isinstance(kg.get("nx_graph"), dict):
        nx_path = json_subdir / f"{stem}_nx_graph.json"
        try:
            nx_path.write_text(json.dumps(kg["nx_graph"], ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Saved nx_graph JSON to {nx_path}")
        except Exception as e:
            print(f"Warning: failed to save nx_graph JSON: {e}")

    original_filename = Path(md_path).name
    prompt = f"""Please convert the markdown document back to its original XML format.

Guidelines for conversion:
1. Recreate the XML structure based on the markdown hierarchy and content
2. Convert markdown headers back to appropriate XML elements
3. Restore all attributes that were mentioned in the markdown
4. Preserve all text content exactly as shown
5. Ensure the XML is well-formed and valid
6. Use proper XML syntax with matching opening and closing tags
7. Include XML declaration if appropriate
8. IMPORTANT: Include these specific schema references in the root element:
   xmlns:dc="http://www.purl.org/dc/elements/1.1/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd"

Original filename: {original_filename}

Markdown content to convert:
{md_text}

IMPORTANT: Provide ONLY the raw XML content. Do NOT wrap it in markdown code blocks (```), do NOT add backticks (`), do NOT add any markdown formatting. Just return the pure XML text starting with <?xml and ending with the closing tag."""

    print(f"Calling LLM at {llm_url} with KG ({len(kg['nodes'])} nodes, {len(kg['edges'])} edges) ...")
    model_output = call_llm_with_kg(llm_url=llm_url, prompt=prompt, kg=kg, md_text=md_text)

    # Save XML output
    if out_xml_path is None:
        out_xml_path = str(kg_dir / (Path(md_path).stem + "_kg_generated.XML"))
    else:
        Path(out_xml_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_xml_path).write_text(model_output, encoding="utf-8")
    print(f"Saved XML to {out_xml_path}")
    # Validate the generated XML using validator if available (or local validator)
    is_valid = False
    message = ""
    try:
        if external_validate_xml is not None:
            is_valid, message = external_validate_xml(model_output)
        else:
            is_valid, message = validate_xml_string(model_output)
    except Exception as e:
        print(f"Validation step failed: {e}")

    if is_valid:
        print("Generated XML validated as well-formed.")
        return model_output

    # If invalid, run the fixer which will create per-attempt folders
    print(f"Generated XML failed validation: {message}")
    error_log = message
    fixed = fix_xml_with_errors(llm_url=llm_url, kg=kg, md_text=md_text, previous_xml=model_output, error_log=error_log, max_retries=5, out_dir=kg_dir)
    if fixed:
        fixed_path = kg_dir / (Path(md_path).stem + "_kg_fixed.XML")
        fixed_path.write_text(fixed, encoding="utf-8")
        print(f"Saved fixed XML to {fixed_path}")
        return fixed

    print("Failed to fix XML after retries. Returning original (invalid) output.")
    return model_output


# --- runner  ---

if __name__ == "__main__":
    llm_url = os.getenv("LLM_API_ENDPOINT")
    if not llm_url:
        raise RuntimeError("LLM API endpoint not specified. Set LLM_API_ENDPOINT env var.")
    md_input = os.getenv("MD_INPUT_FOLDER") or os.getenv("MD_INPUT_FILE")
    if not md_input:
        raise RuntimeError("Markdown input not specified. Set MD_INPUT_FOLDER or MD_INPUT_FILE env var.")
    md_path = Path(md_input)
    if md_path.is_dir():
        md_files = list(md_path.rglob("*.md")) + list(md_path.rglob("*.markdown"))
        if not md_files:
            raise RuntimeError(f"No markdown files found in directory: {md_path}")
        for m in md_files:
            print(f"\n--- Processing {m} ---")
            try:
                generate_xml_from_markdown(str(m), llm_url)
            except Exception as e:
                print(f"Error processing {m}: {e}")
    elif md_path.is_file():
        generate_xml_from_markdown(str(md_path), llm_url)
    else:
        raise RuntimeError(f"Specified markdown input does not exist: {md_path}")
