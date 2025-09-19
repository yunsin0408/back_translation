# DMC-S1KDTOOLS-A-02-00-00-00A-040A-D_EN-CA
## Ident and Status Section
The ident and status section contains information about the document identification and its current status.

### DM Address
The DM address provides details about the document's identity.
* **DM Ident:**
	+ Model Ident Code: `S1KDTOOLS`
	+ System Diff Code: `A`
	+ System Code: `02`
	+ Sub System Code: `0`
	+ Sub Sub System Code: `0`
	+ Assy Code: `00`
	+ Disassy Code: `00`
	+ Disassy Code Variant: `A`
	+ Info Code: `040`
	+ Info Code Variant: `A`
	+ Item Location Code: `D`
* **Language:** 
	+ Language Iso Code: `en`
	+ Country Iso Code: `CA`
* **Issue Info:**
	+ Issue Number: `026`
	+ In Work: `00`

### DM Address Items
The DM address items provide additional information about the document.
* **Issue Date:**
	+ Year: `2020`
	+ Month: `09`
	+ Day: `01`
* **DM Title:**
	+ Tech Name: `s1kd-validate`
	+ Info Name: `Description`

### DM Status
The DM status provides information about the document's current status.
* **Issue Type:** `changed`
* **Security Classification:** `01`
* **Responsible Partner Company:** 
	+ Enterprise Name: `khzae.net`
* **Originator:**
	+ Enterprise Name: `khzae.net`
* **Applic:** 
	+ Display Text: `All`
* **BrexDm Ref:**
	+ DM Ref Ident:
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
* **Quality Assurance:** 
	+ Unverified
* **Reason for Update:**
	1. ID: `rfu-0001`
		- Update Reason Type: `urt02`
		- Update Highlight: `1`
		- Description: Remove -d (--schemas) option.
	2. ID: `rfu-xml-catalog`
		- Update Reason Type: `urt02`
		- Update Highlight: `1`
		- Description: Add --xml-catalog parser option.

## Content
The content section contains the main description of the document.

### Description
The description provides an overview of the s1kd-validate tool.
#### General
The s1kd-validate tool validates S1000D CSDB objects, checking whether they are valid XML files and if they are valid against their own S1000D schemas.

#### Usage
The usage section describes how to use the s1kd-validate tool.
```bash
s1kd-validate [-s <path>] [-x <URI>] [-F|-f] [-eloqv^h?] 
              [<object>...]
```
#### Options
The options section lists the available command-line options for the s1kd-validate tool.

| Option | Description |
| --- | --- |
| -e, --ignore-empty | Ignore validation for empty or non-XML documents. |
| -F, --valid-filenames | List valid files. |
| -f, --filenames | List invalid files. |
| -h, -?, --help | Show help/usage message. |
| -l, --list | Treat input as a list of object names to validate, rather than an object itself. |
| -o, --output-valid | Output valid CSDB objects to stdout. |
| -q, --quiet | Quiet mode. The tool will not output anything to stdout or stderr. Success/failure will only be indicated through the exit status. |
| -s, --schema <path> | Validate the objects against the specified schema, rather than the one that they reference. |
| -v, --verbose | Verbose mode. Success/failure will be explicitly reported on top of any errors. |
| -x, --exclude <URI> | Exclude an XML namespace from the validation. Elements in the namespace specified by <URI> are ignored. |
| -^, --remove-deleted | Validate with elements that have a change type of "delete" removed. |
| --version | Show version information. |
| <object>... | Any number of CSDB objects to validate. If none are specified, input is read from stdin. |

Additionally, the following options allow configuration of the XML parser:

| Option | Description |
| --- | --- |
| --dtdload | Load the external DTD. |
| --huge | Remove any internal arbitrary parser limits. |
| --net | Allow network access to load external DTD and entities. |
| --noent | Resolve entities. |
| --parser-errors | Emit errors from parser. |
| --parser-warnings | Emit warnings from parser. |
| --xinclude | Do XInclude processing. |
| --xml-catalog <file> | Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times. |

#### XML Catalogs
XML catalogs allow redirecting the canonical URIs of XML schemas and other external resources to local files, so as to avoid the unnecessary overhead of downloading those static resources over the Internet.

Example of a catalog file which maps the S1000D schemas to a local directory:
```xml
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <rewriteURI 
    uriStartString="http://www.s1000d.org"
    rewritePrefix="/usr/share/s1kd/schemas"/>
</catalog>
```
This can be placed in a catalog file automatically loaded by libxml2 (e.g., `/etc/xml/catalog`) or saved to a file which is then specified in an environment variable used by libxml2 (e.g., `XML_CATALOG_FILES`):
```bash
$ XML_CATALOG_FILES=catalog.xml s1kd-validate <DMs...>
```
Alternatively, the --xml-catalog option may be used:
```bash
$ s1kd-validate --xml-catalog=catalog.xml <DMs>...
```

#### Exit Status
The exit status section describes the possible exit codes returned by the s1kd-validate tool.

| Code | Description |
| --- | --- |
| 0 | No errors. |
| 1 | Some CSDB objects are not well-formed or valid. |
| 2 | The number of schemas cached exceeded the available memory. |
| 3 | A specified schema could not be read. |

#### Example
Example usage of the s1kd-validate tool:
```bash
$ s1kd-validate DMC-EX-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
```
Note: This is a markdown representation of the provided XML document, and it may not include all the details or nuances present in the original XML file.