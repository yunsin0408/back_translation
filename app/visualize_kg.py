"""visualize_kg.py

Small standalone utility to visualize knowledge-graph JSONs produced by
`md_to_kg_to_xml.py` (or any node-link JSON). It produces:

- PNG (matplotlib static preview)
- interactive HTML (pyvis)
- GEXF export (Gephi)

It is tolerant of missing optional libraries: if matplotlib or pyvis are
not installed the script will skip that output and print an instruction.

Usage:
    # visualize a single file
    python app/visualize_kg.py --input kg_xml/jsons/example_nx_graph.json

    # visualize all JSONs in a folder
    python app/visualize_kg.py --input kg_xml/jsons/

Options:
    --input / -i   : path to a JSON file or directory containing JSON files
    --out / -o     : output directory (defaults to kg_xml/visuals/)
    --top-k / -k   : limit graph to top-K nodes by degree (helps large graphs)
    --open-html    : try to open the generated HTML in the default browser

"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import argparse

try:
    import networkx as nx
    from networkx.readwrite import json_graph
except Exception:
    print("networkx is required. Install it in your venv: pip install networkx")
    raise


def load_node_link(path: Path) -> Dict[str, Any]:
    txt = path.read_text(encoding="utf-8")
    obj = json.loads(txt)
    # If this is a KG wrapper with 'nx_graph', extract it
    if isinstance(obj, dict) and "nx_graph" in obj:
        return obj["nx_graph"]
    # Otherwise assume the file itself is node-link data
    return obj


def save_png(node_link: Dict[str, Any], out_path: Path, top_k: Optional[int] = None) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        print("matplotlib not available; skipping PNG (pip install matplotlib to enable)")
        return
    try:
        G = json_graph.node_link_graph(node_link)
        if top_k is not None and G.number_of_nodes() > top_k:
            # keep only top_k nodes by degree
            degrees = sorted(G.degree(), key=lambda x: x[1], reverse=True)
            keep = {n for n, _ in degrees[:top_k]}
            G = G.subgraph(keep).copy()
        plt.figure(figsize=(12, 10))
        pos = nx.spring_layout(G, seed=42)
        nx.draw_networkx_nodes(G, pos, node_size=150)
        nx.draw_networkx_edges(G, pos, alpha=0.6)
        nx.draw_networkx_labels(G, pos, font_size=8)
        plt.axis("off")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path, bbox_inches="tight", dpi=150)
        plt.close()
        print(f"Saved PNG: {out_path}")
    except Exception as e:
        print(f"Warning: failed to save PNG: {e}")


def save_html_pyvis(node_link: Dict[str, Any], out_path: Path, top_k: Optional[int] = None) -> None:
    try:
        from pyvis.network import Network
    except Exception:
        print("pyvis not installed; skipping HTML (pip install pyvis to enable)")
        return
    try:
        G = json_graph.node_link_graph(node_link)
        if top_k is not None and G.number_of_nodes() > top_k:
            degrees = sorted(G.degree(), key=lambda x: x[1], reverse=True)
            keep = {n for n, _ in degrees[:top_k]}
            G = G.subgraph(keep).copy()
        net = Network(height="800px", width="100%", notebook=False)
        net.from_nx(G)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # Use write_html when available (safer than show which may attempt to render)
        try:
            net.write_html(str(out_path))
        except Exception:
            # Fall back to show (some pyvis versions only provide show)
            net.show(str(out_path))
        print(f"Saved interactive HTML: {out_path}")
    except Exception as e:
        print(f"Warning: failed to save HTML: {e}")


def save_gexf(node_link: Dict[str, Any], out_path: Path, top_k: Optional[int] = None) -> None:
    try:
        G = json_graph.node_link_graph(node_link)
        if top_k is not None and G.number_of_nodes() > top_k:
            degrees = sorted(G.degree(), key=lambda x: x[1], reverse=True)
            keep = {n for n, _ in degrees[:top_k]}
            G = G.subgraph(keep).copy()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # Sanitize node and edge attributes: GEXF does not support complex types
        try:
            for n, attrs in list(G.nodes(data=True)):
                for k, v in list(attrs.items()):
                    if not isinstance(v, (str, int, float, bool)):
                        attrs[k] = json.dumps(v, ensure_ascii=False)
            for u, v, attrs in list(G.edges(data=True)):
                for k, vv in list(attrs.items()):
                    if not isinstance(vv, (str, int, float, bool)):
                        attrs[k] = json.dumps(vv, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: failed to sanitize attributes for GEXF: {e}")
        nx.write_gexf(G, str(out_path))
        print(f"Saved GEXF: {out_path}")
    except Exception as e:
        print(f"Warning: failed to save GEXF: {e}")


def process_file(path: Path, out_dir: Path, top_k: Optional[int], open_html: bool) -> None:
    try:
        node_link = load_node_link(path)
    except Exception as e:
        print(f"Failed to load {path}: {e}")
        return
    stem = path.stem.replace("_nx_graph", "").replace("_kg", "")
    visuals = out_dir
    png_path = visuals / f"{stem}_graph.png"
    html_path = visuals / f"{stem}_graph.html"
    gexf_path = visuals / f"{stem}_graph.gexf"

    save_png(node_link, png_path, top_k=top_k)
    save_html_pyvis(node_link, html_path, top_k=top_k)
    save_gexf(node_link, gexf_path, top_k=top_k)

    if open_html and html_path.exists():
        try:
            import webbrowser
            webbrowser.open(str(html_path))
        except Exception as e:
            print(f"Failed to open HTML in browser: {e}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Visualize kg node-link JSONs (PNG, HTML, GEXF)")
    p.add_argument("-i", "--input", required=True, help="JSON file or directory containing JSONs")
    p.add_argument("-o", "--out", default="kg_xml/visuals", help="output visuals directory")
    p.add_argument("-k", "--top-k", type=int, default=None, help="keep only top-k nodes by degree for visualization")
    p.add_argument("--open-html", action="store_true", help="open the generated HTML in the default browser")
    args = p.parse_args(argv)

    inp = Path(args.input)
    out_dir = Path(args.out)
    if inp.is_dir():
        files = list(inp.glob("*.json"))
        if not files:
            print(f"No json files found in {inp}")
            return
        for f in files:
            print(f"Processing {f}")
            process_file(f, out_dir, args.top_k, args.open_html)
    elif inp.is_file():
        process_file(inp, out_dir, args.top_k, args.open_html)
    else:
        print(f"Input path not found: {inp}")


if __name__ == "__main__":
    main()
