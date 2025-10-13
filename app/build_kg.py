import re
from typing import List, Dict, Any, Tuple, Optional
import networkx as nx
from pathlib import Path

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
    
    #networkx graph
    from networkx.readwrite import json_graph
    G = nx.Graph()
    for n in nodes_list:
        G.add_node(n["id"], **{"label": n["label"], "type": n["type"]})
    for e in edges_list:
        G.add_edge(e["source"], e["target"], weight=e.get("weight", 1), units=e.get("units", []))
    kg["nx_graph"] = json_graph.node_link_data(G)
    return kg