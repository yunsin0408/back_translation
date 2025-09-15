from lxml import etree
from pathlib import Path
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import csv
import os
from dotenv import load_dotenv, find_dotenv  
load_dotenv(find_dotenv(), override=False)

def validate_xml(xml_content: str) -> tuple[bool, str]:
    """Validate if the XML content is well-formed and collect all errors."""
    try:
        if isinstance(xml_content, str):
            xml_bytes = xml_content.encode("utf-8")
        else:
            xml_bytes = xml_content
        
        # strict parsing - if success-> valid, else collect all errors
        try:
            strict_parser = etree.XMLParser(recover=False)
            etree.fromstring(xml_bytes, parser=strict_parser)
            return True, "Valid XML"
        except (etree.XMLSyntaxError, etree.ParseError) as e:
            errors = []
            
            # recover=True to continue parsing and collect all errors
            recover_parser = etree.XMLParser(recover=True)
            try:
                etree.fromstring(xml_bytes, parser=recover_parser)
            except Exception as recover_error:
                errors.append(f"Recovery error: {recover_error}")
            
            # Get parser errors if available
            if hasattr(recover_parser, 'error_log'):
                for error in recover_parser.error_log:
                    errors.append(f"Line {error.line}, Column {error.column}: {error.message}")
            
            # If collected errors, return them
            if errors:
                error_details = []
                for i, error_msg in enumerate(errors, 1):
                    error_details.append(f"Error {i}: {error_msg}")
                return False, f"Errors found:\n" + "\n".join(error_details)
            else:
                # Fallback to original error
                error_type = e.__class__.__name__
                line, column = getattr(e, "position", (None, None))
                position_str = f"line {line}, column {column}" if line is not None else "unknown position"
                return False, f"{error_type} at {position_str}: {e}"
            
    except Exception as e:
        # Fallback for non-parsing errors
        error_type = e.__class__.__name__
        line, column = getattr(e, "position", (None, None))
        position_str = f"line {line}, column {column}" if line is not None else "unknown position"
        return False, f"{error_type} at {position_str}: {e}"

def validate_xml_file(file_path: Path) -> tuple[bool, str]:
    try:
        content = file_path.read_text(encoding="utf-8", errors="strict")
    except Exception as e:
        return False, f"Cannot read file: {e}"
    return validate_xml(content)

def validate_xml_folder(folder: str, max_workers: int = 4) -> List[tuple[Path, bool, str]]:
    path = Path(folder)
    if not path.exists() or not path.is_dir():
        raise ValueError(f"Folder not found or not a directory: {folder}")

    files = list(path.glob("*.xml")) + list(path.glob("*.XML"))
    if not files:
        print(f"No XML files found in {folder}")
        return []

    results: List[tuple[Path, bool, str]] = []

    def _worker(p: Path) -> tuple[Path, bool, str]:
        is_valid, message = validate_xml_file(p)
        return (p, is_valid, message)

    print(f"Validating {len(files)} XML files in {folder}...")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(_worker, f): f for f in files}
        for future in as_completed(future_map):
            p, ok, msg = future.result()
            status = "✓" if ok else "✗"
            print(f"{status} {p.name}: {msg}")
            results.append((p, ok, msg))

    total = len(results)
    passed = sum(1 for _, ok, _ in results if ok)
    failed = total - passed
    print("\n=== Summary ===")
    print(f"Total: {total}  Passed: {passed}  Failed: {failed}")
    
    # Count error types and list files
    if failed > 0:
        print("\n=== Error Analysis ===")
        error_files = {}
        for file_path, is_valid, message in results:
            if not is_valid:
                # Extract error type from message
                if "Errors found:" in message:
                    # Multiple errors - count each type
                    error_lines = message.split("\n")[1:]  # Skip "Errors found:" line
                    for line in error_lines:
                        if line.strip():
                            # Extract error type 
                            error_type = line.split(":")[0].strip() if ":" in line else "Unknown error"
                            if error_type not in error_files:
                                error_files[error_type] = []
                            error_files[error_type].append(file_path.name)
                else:
                    # Single error
                    error_type = message.split(" at ")[0] if " at " in message else message.split(":")[0] if ":" in message else "Unknown error"
                    if error_type not in error_files:
                        error_files[error_type] = []
                    error_files[error_type].append(file_path.name)
        
        # Sort by count (descending)
        sorted_errors = sorted(error_files.items(), key=lambda x: len(x[1]), reverse=True)
        for error_type, files in sorted_errors:
            print(f"\n{error_type}: {len(files)} files")
            for filename in sorted(files):
                print(f"  - {filename}")
    
    return results

DEFAULT_XML_FOLDER = os.getenv("XML_FOLDER_VALIDATION") 

def main():
    parser = argparse.ArgumentParser(description="Validate well-formedness of XML files in a folder.")
    parser.add_argument("--folder", type=str, help="Path to folder containing XML files (*.xml or *.XML)")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers (default: 4)")
    parser.add_argument("--csv", type=str, default="results/xml_validation_results6.csv", help="Path to write CSV results (default: xml_validation_results.csv)")
    args = parser.parse_args()

    folder = DEFAULT_XML_FOLDER
    if not folder:
        print("Please provide a folder via --folder or set DEFAULT_XML_FOLDER in validator.py")
        return

    results = validate_xml_folder(folder, max_workers=args.workers)

    # Write results to CSV
    try:
        csv_path = Path(args.csv)
        if csv_path.parent and not csv_path.parent.exists():
            csv_path.parent.mkdir(parents=True, exist_ok=True)
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["file", "is_valid", "message"])
            for p, ok, msg in results:
                writer.writerow([str(p), ok, msg])
        print(f"\nCSV written: {csv_path}")
    except Exception as e:
        print(f"Failed to write CSV: {e}")

if __name__ == "__main__":
    main()

