# DMC-S1KDTOOLS-A-00-00-00-00A-018A-D_EN-CA
## Introduction to S1KD-Tools and S1000D
The following document provides an overview of the relationship between s1kd-tools and S1000D, as well as definitions for common terms used throughout the s1kd-tools documentation.

### Ident and Status Section
#### DM Address
The DM address contains information about the document identification and language.
* **DM Ident:**
	+ Model Ident Code: `S1KDTOOLS`
	+ System Diff Code: `A`
	+ System Code: `00`
	+ Sub System Code: `0`
	+ Sub Sub System Code: `0`
	+ Assy Code: `00`
	+ Disassy Code: `00`
	+ Disassy Code Variant: `A`
	+ Info Code: `018`
	+ Info Code Variant: `A`
	+ Item Location Code: `D`
* **Language:**
	+ Language ISO Code: `en`
	+ Country ISO Code: `CA`
* **Issue Info:**
	+ Issue Number: `024`
	+ In Work: `00`
* **DM Address Items:**
	+ Issue Date:
		- Year: `2020`
		- Month: `05`
		- Day: `01`
	+ DM Title:
		- Tech Name: `s1kd-tools`
		- Info Name: `Introduction`

#### DM Status
The DM status contains information about the document's security classification, responsible partner company, and originator.
* **Security Classification:** `01`
* **Responsible Partner Company:**
	+ Enterprise Name: `khzae.net`
* **Originator:**
	+ Enterprise Name: `khzae.net`
* **Applicability:**
	+ Display Text:
		- Simple Para: `All`
* **BREX DM Ref:**
	+ DM Ref:
		- DM Ref Ident:
			- DM Code:
				- Model Ident Code: `S1KDTOOLS`
				- System Diff Code: `A`
				- System Code: `00`
				- Sub System Code: `0`
				- Sub Sub System Code: `0`
				- Assy Code: `00`
				- Disassy Code: `00`
				- Disassy Code Variant: `A`
				- Info Code: `022`
				- Info Code Variant: `A`
				- Item Location Code: `D`
* **Quality Assurance:** Unverified
* **Reason for Update:**
	+ Simple Para: `Upissue`

## Content
### Description
The description section contains an overview of S1000D and s1kd-tools.

#### General
This document provides a basic overview of the relationship between s1kd-tools and S1000D, as well as definitions for common terms used throughout the s1kd-tools documentation.

#### S1000D
S1000D is an international specification for the procurement and production of technical publications. It focuses on breaking down documents into individual components called "data modules," which can be reused in multiple publications. These data modules are typically authored using provided XML schemas, allowing them to be automatically managed in a Common Source Database (CSDB) and validated against defined project "business rules."

#### S1KD-Tools
The s1kd-tools are a set of small tools for creating and manipulating S1000D data. They can be used as a standalone method for maintaining a simple S1000D CSDB, in conjunction with a more typical version control system, or to support an existing S1000D CSDB.

#### CSDB
A Common Source Database (CSDB) is a directory within a filesystem. The s1kd-tools use the "File-based transfer" file naming conventions described in Chapter 7 of the S1000D specification. To facilitate interchange between different CSDB implementations, projects can use "transfer packages" also described in Chapter 7.

#### Relationship to the S1000D Process
The s1kd-tools support multiple parts of the basic S1000D process:
1. **Generation:** The generation of new CSDB objects is supported by the `s1kd-dmrl` tool and the `s1kd-new*` set of tools.
2. **Authoring:** These tools support the authoring process, including creating notation and entity elements to reference an ICN in a data module, listing data modules within a directory, editing S1000D metadata on CSDB objects, changing references to one object into references to another, inserting references to other CSDB objects, organizing the CSDB using a given SNS structure, and moving CSDB objects through the standard S1000D workflow.
3. **Validation:** These tools validate different aspects of CSDB objects, including applicability, business rules exchange (BREX) data modules, CIR references, and general correctness as XML documents.
4. **Publication:** These tools support the production of publications from a CSDB, including marking up acronyms within data modules, generating lists of acronyms marked up within data modules, preprocessing applicability statements in a data module, flattening a publication module and referenced data modules into a single "deliverable" file, generating front matter data module content from a publication module, resolving ICN references in objects, flagging index keywords in a data module based on a user-defined list, producing "instances" of CSDB objects using applicability filtering and/or common information repositories (CIRs), generating IETP neutral metadata for CSDB objects, generating the References table within data modules, and converting units of measure used in data modules.

Some of the key tools used in these processes include:
* `s1kd-acronyms`
* `s1kd-addicn`
* `s1kd-appcheck`
* `s1kd-aspp`
* `s1kd-brexcheck`
* `s1kd-defaults`
* `s1kd-dmrl`
* `s1kd-flatten`
* `s1kd-fmgen`
* `s1kd-icncatalog`
* `s1kd-index`
* `s1kd-instance`
* `s1kd-ls`
* `s1kd-metadata`
* `s1kd-mvref`
* `s1kd-neutralize`
* `s1kd-new*`
* `s1kd-ref`
* `s1kd-repcheck`
* `s1kd-sns`
* `s1kd-syncrefs`
* `s1kd-uom`
* `s1kd-upissue`
* `s1kd-validate`