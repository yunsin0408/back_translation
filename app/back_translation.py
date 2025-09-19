import os
from dotenv import load_dotenv, find_dotenv  
load_dotenv(find_dotenv(), override=False)
from pathlib import Path
import re
from typing import List
import requests

class XMLToMarkdownToXMLProcessor:
    def __init__(self):
        self.llm_url = os.getenv("LLM_API_ENDPOINT")
        if not self.llm_url:
            raise ValueError(
                "Environment variable LLM_API_ENDPOINT is not set. Set it in your .env or export it in the shell."
            )
    
    def xml_to_markdown_prompt(self, xml_content: str, filename: str) -> str:
        """Create a prompt for LLM to convert XML to Markdown."""
        prompt = f"""Please convert the following XML document to a well-structured markdown format.

Guidelines for conversion:
1. Create a clear document title using the filename
2. Use appropriate markdown headers (# ## ###) to represent the XML hierarchy
3. Convert XML elements to markdown sections with proper nesting
4. Preserve all attributes as key-value pairs in a readable format
5. Maintain all text content from the XML
6. Use code blocks, lists, or tables where appropriate for better readability
7. Make the markdown human-readable and well-organized
8. Please ensure that the XML references the same schema as the original XML file

XML file: {filename}

XML content:
{xml_content}

Please provide a clean, well-structured markdown document:"""
        
        return prompt
    
    def markdown_to_xml_prompt(self, markdown_content: str, original_filename: str) -> str:
        #Input S1000D schema
        prompt = f"""Please convert the following markdown document back to its original XML format.

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
{markdown_content}

IMPORTANT: Provide ONLY the raw XML content. Do NOT wrap it in markdown code blocks (```), do NOT add backticks (`), do NOT add any markdown formatting. Just return the pure XML text starting with <?xml and ending with the closing tag."""
        
        return prompt
    
    def call_llm(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json"
        }
        session = requests.Session()
        session.timeout = 600  # 10 minutes

        data = {
            "model": "gemma3:27b",
            "messages": [{
                "role": "user",
                "content": prompt
            }],
            "temperature": 0.7
        }

        try:
            response = session.post(self.llm_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise Exception(f"LLM API call failed: {str(e)}")
    
    def process_xml_to_markdown(self, xml_content: str, filename: str) -> str:
        system_context = "You are an expert at converting XML documents to well-structured, readable markdown format. Always create clean, organized markdown."
        user_prompt = self.xml_to_markdown_prompt(xml_content, filename)
        
        full_prompt = f"{system_context}\n\n{user_prompt}"
        
        try:
            markdown_content = self.call_llm(full_prompt)
            return markdown_content.strip()
            
        except Exception as e:
            raise Exception(f"XML to Markdown conversion failed: {str(e)}")
    
    def process_markdown_to_xml(self, markdown_content: str, original_filename: str) -> str:
        system_context = "You are an expert at converting structured markdown back to valid XML format. Always return only well-formed XML."
        user_prompt = self.markdown_to_xml_prompt(markdown_content, original_filename)
        
        full_prompt = f"{system_context}\n\n{user_prompt}"
        xml_content = self.call_llm(full_prompt)
           
         # Clean up (remove markdown code blocks and backticks)
        xml_content = re.sub(r'^```xml\s*', '', xml_content, flags=re.MULTILINE)
        xml_content = re.sub(r'^```\s*', '', xml_content, flags=re.MULTILINE)
        xml_content = re.sub(r'^`\s*', '', xml_content, flags=re.MULTILINE)
        xml_content = re.sub(r'`\s*$', '', xml_content, flags=re.MULTILINE)
        
        return xml_content.strip()
    
    def process_xml_folder_to_markdown(self, input_folder: str, output_folder: str, loop_num: int) -> List[Path]:
        input_path = Path(input_folder)
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
        xml_files = list(input_path.glob("*.XML"))
        if not xml_files:
            print(f"No XML files found in {input_folder}")
            return []
        converted_files = []
        print(f"Converting {len(xml_files)} XML files to Markdown using LLM...")
        for xml_file in xml_files:
            try:
                md_filename = f"{xml_file.stem}_{loop_num}.md"
                md_filepath = output_path / md_filename
                if md_filepath.exists():
                    print(f"~ Skipping {xml_file.name}: {md_filename} already exists")
                    continue
                with open(xml_file, 'r', encoding='utf-8') as f:
                    xml_content = f.read()
                print(f"Processing {xml_file.name} -> Markdown...")
                markdown_content = self.process_xml_to_markdown(xml_content, xml_file.name)
                with open(md_filepath, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                converted_files.append(md_filepath)
                print(f"✓ Saved: {md_filename}")
            except Exception as e:
                print(f"✗ Error converting {xml_file.name}: {str(e)}")
        return converted_files
    
    def process_markdown_folder_to_xml(self, markdown_folder: str, output_folder: str, loop_num: int) -> List[Path]:
        if not markdown_folder or not output_folder:
            raise ValueError("markdown_folder and output_folder must be non-empty strings.")
        md_path = Path(markdown_folder)
        output_path = Path(output_folder)
        output_path.mkdir(parents=True, exist_ok=True)
        md_files = list(md_path.glob(f"*_{loop_num}.md"))
        if not md_files:
            print(f"No markdown files found in {markdown_folder}")
            return []
        converted_files = []
        print(f"Converting {len(md_files)} Markdown files back to XML using LLM...")
        for md_file in md_files:
            try:
                xml_filename = f"{md_file.stem}_regenerated.XML"
                xml_filepath = output_path / xml_filename
                if xml_filepath.exists():
                    print(f"~ Skipping {md_file.name}: {xml_filename} already exists")
                    continue
                with open(md_file, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
                original_filename = md_file.stem.rsplit('_', 1)[0] + ".XML"
                print(f"Processing {md_file.name} -> XML...")
                xml_content = self.process_markdown_to_xml(markdown_content, original_filename)
                from validator import validate_xml
                is_valid, validation_msg = validate_xml(xml_content)
                if is_valid:
                    print(f"✓ Generated valid XML")
                else:
                    print(f"⚠ Warning: {validation_msg}")
                with open(xml_filepath, 'w', encoding='utf-8') as f:
                    f.write(xml_content)
                converted_files.append(xml_filepath)
                print(f"✓ Saved: {xml_filename}")
            except Exception as e:
                print(f"✗ Error converting {md_file.name}: {str(e)}")
        return converted_files
    
    def full_pipeline(self, input_xml_folder: str, output_md_folder: str, 
                     output_xml_folder: str, loop_num: int) -> dict:
        """
        Run complete pipeline: XML files -> LLM (generate MD) -> LLM (generate XML back).
        
        Returns a dictionary with information about the processed files.
        """
        print("=== XML → LLM  → Markdown → LLM → XML Pipeline ===\n")
        results = {
            'original_xml_count': 0,
            'markdown_generated': 0,
            'xml_regenerated': 0,
            'errors': []
        }
        xml_files = list(Path(input_xml_folder).glob("*.XML"))
        results['original_xml_count'] = len(xml_files)
        if not xml_files:
            print(f"No XML files found in {input_xml_folder}")
            return results
        try:
            print("Step 1: Converting XML files to Markdown using LLM...")
            md_files = self.process_xml_folder_to_markdown(input_xml_folder, output_md_folder, loop_num)
            results['markdown_generated'] = len(md_files)
            print(f"Generated {len(md_files)} markdown files.\n")
            if not md_files:
                print("No markdown files generated. Pipeline stopped.")
                return results
            print("Step 2: Converting Markdown files back to XML using LLM...")
            xml_files = self.process_markdown_folder_to_xml(output_md_folder, output_xml_folder, loop_num)
            results['xml_regenerated'] = len(xml_files)
            print(f"Generated {len(xml_files)} XML files.\n")
            print("=== Pipeline Complete ===")
            print(f"Original XML files: {results['original_xml_count']}")
            print(f"Markdown files generated: {results['markdown_generated']}")
            print(f"XML files regenerated: {results['xml_regenerated']}")
        except Exception as e:
            error_msg = f"Pipeline failed: {str(e)}"
            print(error_msg)
            results['errors'].append(error_msg)
        return results

def main():
    
    processor = XMLToMarkdownToXMLProcessor()
    original_input_xml_folder = os.getenv("INPUT_XML_FOLDER")
    input_xml_folder = original_input_xml_folder
    for i in range(2, 6):
        output_md_folder = f"folders/regenerated_md_{i}"
        output_xml_folder = f"folders/regenerated_xml_{i}"
        print(f"\n=== Pipeline iteration {i} ===")
        try:
            results = processor.full_pipeline(
                input_xml_folder=input_xml_folder,
                output_md_folder=output_md_folder,
                output_xml_folder=output_xml_folder,
                loop_num=i
            )
            # For next iteration, use the just-generated XMLs as input
            input_xml_folder = output_xml_folder
        except Exception as e:
            print(f"Pipeline failed in iteration {i}: {e}")

if __name__ == "__main__": 
    main()
