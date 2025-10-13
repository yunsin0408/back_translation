"""md_to_kg_to_xml.py

Clean, self-contained implementation of the md -> KG -> LLM -> XML pipeline.

Behavior:
- Reads markdown via build_kg.read_markdown()
- Builds a KG via build_kg.build_knowledge_graph()
- Calls an LLM endpoint (env LLM_API_ENDPOINT) with a messages payload
- Saves KG JSON and networkx node-link JSON under ./kg_xml2/jsons
- Validates XML using validator.validate_xml()
- If invalid, iteratively asks the LLM to fix the XML and saves per-attempt artifacts

Functions are intentionally explicit about return values so the runner can collect a final summary
with fields: needed_fix (bool), attempts (int), fixed (bool), last_error (str|None)
"""
from __future__ import annotations
import os
import re
import json
import time
import requests
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=False)

from build_kg import read_markdown, split_to_text_units, build_knowledge_graph
from validator import validate_xml


def sanitize_for_json(obj: Any):
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    if isinstance(obj, dict):
        return {k: sanitize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [sanitize_for_json(v) for v in obj]
    return str(obj)


def call_llm_with_kg(llm_url: str, prompt: str, kg: Dict[str, Any], md_text: str, out_dir: Optional[Path] = None, timeout: int = 600) -> str:
    """Send a messages-style payload to the LLM and return the textual response.

    When out_dir is provided, payload and response are saved for debugging.
    """
    if not llm_url:
        raise ValueError("LLM_API_ENDPOINT (llm_url) is required.")

    system_msg = (
        "You are an expert XML generator. You MUST use the provided Knowledge Graph (KG) as the PRIMARY source of structural information when reconstructing the XML.\n"
        "Return ONLY well-formed XML (no commentary, no markdown fences). If the markdown conflicts with the KG, prefer the KG. Start the response with '<?xml'."
    )

    kg_clean = sanitize_for_json(kg)
    user_content = json.dumps({"kg": kg_clean, "markdown": md_text}, ensure_ascii=False)
    if prompt:
        user_content = user_content + "\n\n" + prompt

    payload = {
        "model": "gemma3:27b",
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_content},
        ],
        "temperature": 0.0,
    }

    if out_dir is not None:
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "payload.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

    resp = requests.post(llm_url, json=payload, headers={"Content-Type": "application/json"}, timeout=timeout)
    try:
        resp.raise_for_status()
    except Exception as e:
        if out_dir is not None:
            try:
                (out_dir / "response_error.txt").write_text(resp.text, encoding="utf-8")
            except Exception:
                pass
        raise

    text = None
    try:
        j = resp.json()
        if isinstance(j, dict) and "choices" in j and isinstance(j["choices"], list) and j["choices"]:
            first = j["choices"][0]
            if isinstance(first, dict):
                if "message" in first and isinstance(first["message"], dict) and "content" in first["message"]:
                    text = first["message"]["content"]
                elif "text" in first:
                    text = first["text"]
        if text is None and isinstance(j, dict) and "text" in j and isinstance(j["text"], str):
            text = j["text"]
        if text is None:
            text = json.dumps(j, ensure_ascii=False)
    except ValueError:
        text = resp.text

    if out_dir is not None:
        try:
            (out_dir / "response.txt").write_text(text, encoding="utf-8")
        except Exception:
            pass

    return text


def fix_xml_with_errors(
    llm_url: str,
    kg: Dict[str, Any],
    md_text: str,
    previous_xml: str,
    error_log: str,
    max_retries: int = 5,
    md_filename: Optional[str] = None,
    out_dir: Optional[Path] = None,
) -> Tuple[Optional[str], int, bool, Optional[str]]:
    """Try to repair previous_xml using validator error_log and the KG.

    Returns (fixed_xml_or_None, attempts, fixed_bool, last_error_message)
    """
    base_name = md_filename or "output"
    fix_root = Path.cwd() / "fix"
    attempt_base = fix_root / base_name
    attempt_base.mkdir(parents=True, exist_ok=True)

    fix_prompt = (
        "The XML failed validation. Use the provided KG and the parser error log to correct the XML. Return only the corrected XML (no extra text)."
    )

    attempts = 0
    last_error: Optional[str] = None

    for attempt in range(1, max_retries + 1):
        attempts = attempt
        attempt_dir = attempt_base / f"attempt{attempt}"
        attempt_dir.mkdir(parents=True, exist_ok=True)

        prompt = (
            fix_prompt + "\nERROR_LOG:\n" + error_log + "\n\nPREVIOUS_XML:\n" + previous_xml + "\n\nProvide corrected XML now."
        )

        try:
            (attempt_dir / "previous.xml").write_text(previous_xml, encoding="utf-8")
            (attempt_dir / "error_log.txt").write_text(error_log, encoding="utf-8")
            (attempt_dir / "prompt.txt").write_text(prompt, encoding="utf-8")
        except Exception:
            pass

        try:
            model_output = call_llm_with_kg(llm_url=llm_url, prompt=prompt, kg=kg, md_text=md_text, out_dir=attempt_dir)
        except Exception as e:
            last_error = str(e)
            try:
                (attempt_dir / "exception.txt").write_text(last_error, encoding="utf-8")
            except Exception:
                pass
            time.sleep(min(2 ** attempt, 30))
            continue

        if not (isinstance(model_output, str) and model_output.strip()):
            last_error = "empty response"
            time.sleep(1)
            continue

        try:
            (attempt_dir / "candidate.xml").write_text(model_output, encoding="utf-8")
        except Exception:
            pass

        try:
            is_valid, message = validate_xml(model_output)
        except Exception as e:
            is_valid = False
            message = str(e)

        if is_valid:
            return model_output, attempts, True, None

        last_error = message
        try:
            (attempt_dir / "error_after.txt").write_text(message, encoding="utf-8")
        except Exception:
            pass

        previous_xml = model_output
        error_log = message
        time.sleep(0.5)

    return None, attempts, False, last_error


def generate_xml_from_markdown(md_path: str, llm_url: str, out_xml_path: Optional[str] = None) -> Tuple[str, int, bool, Optional[str]]:
    md_text = read_markdown(md_path)
    units = split_to_text_units(md_text)
    kg = build_knowledge_graph(units)

    kg_dir = Path.cwd() / "kg_xml2"
    kg_dir.mkdir(parents=True, exist_ok=True)
    json_subdir = kg_dir / "jsons"
    json_subdir.mkdir(parents=True, exist_ok=True)

    stem = Path(md_path).stem
    try:
        (json_subdir / f"{stem}_kg.json").write_text(json.dumps(sanitize_for_json(kg), ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    if isinstance(kg.get("nx_graph"), dict):
        try:
            (json_subdir / f"{stem}_nx_graph.json").write_text(json.dumps(sanitize_for_json(kg["nx_graph"]), ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

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
    
    model_output = re.sub(r'^```xml\s*', '', model_output, flags=re.MULTILINE)
    model_output = re.sub(r'^```\s*', '', model_output, flags=re.MULTILINE)
    model_output = re.sub(r'^`\s*', '', model_output, flags=re.MULTILINE)
    model_output = re.sub(r'`\s*$', '', model_output, flags=re.MULTILINE)

    (kg_dir / (stem + "_kg_generated.XML")).write_text(model_output, encoding="utf-8")

    try:
        is_valid, message = validate_xml(model_output)
    except Exception as e:
        is_valid = False
        message = str(e)

    if is_valid:
        return model_output, 0, True, None

    fixed_xml, attempts, fixed_flag, last_error = fix_xml_with_errors(
        llm_url=llm_url,
        kg=kg,
        md_text=md_text,
        previous_xml=model_output,
        error_log=message,
        max_retries=5,
        md_filename=stem,
        out_dir=kg_dir,
    )

    if fixed_xml:
        (kg_dir / (stem + "_kg_fixed.XML")).write_text(fixed_xml, encoding="utf-8")
        return fixed_xml, attempts, True, None

    return model_output, attempts, False, last_error


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

        fix_summary = []
        for m in md_files:
            print(f"\n--- Processing {m} ---")
            try:
                xml, attempts, fixed, last_error = generate_xml_from_markdown(str(m), llm_url)
                needed_fix = attempts > 0
            except Exception as e:
                print(f"Error processing {m}: {e}")
                xml = ""
                attempts = 0
                fixed = False
                needed_fix = False
                last_error = str(e)

            fix_summary.append({
                "file": str(m),
                "needed_fix": needed_fix,
                "attempts": attempts,
                "fixed": fixed,
                "last_error": last_error,
            })

        print("\n=== XML Fix Summary ===")
        total = len(fix_summary)
        needed = sum(1 for f in fix_summary if f["needed_fix"])
        fixed_count = sum(1 for f in fix_summary if f["fixed"])
        still_invalid = [f for f in fix_summary if f["needed_fix"] and not f["fixed"]]
        print(f"Total files processed: {total}")
        print(f"Files needing fix: {needed}")
        print(f"Files fixed: {fixed_count}")
        print(f"Files still invalid after all attempts: {len(still_invalid)}")
        if still_invalid:
            print("\nFiles still invalid:")
            for f in still_invalid:
                print(f"- {f['file']} (attempts: {f['attempts']}, last error: {f['last_error']})")
        print("\nAttempts per file needing fix:")
        for f in fix_summary:
            if f["needed_fix"]:
                print(f"- {f['file']}: {f['attempts']} attempts, fixed: {f['fixed']}")

    elif md_path.is_file():
        xml, attempts, fixed, last_error = generate_xml_from_markdown(str(md_path), llm_url)
        print(f"Processed single file: {md_path} -> fixed={fixed}, attempts={attempts}, last_error={last_error}")

    else:
        raise RuntimeError(f"Specified markdown input does not exist: {md_path}")
