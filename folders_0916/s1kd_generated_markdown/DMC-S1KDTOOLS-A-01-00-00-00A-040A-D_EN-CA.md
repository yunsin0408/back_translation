# DMC-S1KDTOOLS-A-01-00-00-00A-040A-D_EN-CA
## Introduction
The `DMC-S1KDTOOLS-A-01-00-00-00A-040A-D_EN-CA` document is a data module that provides information about the `s1kd-syncrefs` tool.

### Ident and Status Section
The ident and status section contains metadata about the document.
* **DM Address**:
	+ DM Ident:
		- Model Ident Code: `S1KDTOOLS`
		- System Diff Code: `A`
		- System Code: `01`
		- Sub System Code: `0`
		- Sub Sub System Code: `0`
		- Assy Code: `00`
		- Disassy Code: `00`
		- Disassy Code Variant: `A`
		- Info Code: `040`
		- Info Code Variant: `A`
		- Item Location Code: `D`
	+ Language:
		- Language Iso Code: `en`
		- Country Iso Code: `CA`
	+ Issue Info:
		- Issue Number: `019`
		- In Work: `00`
* **DM Address Items**:
	+ Issue Date:
		- Year: `2020`
		- Month: `09`
		- Day: `01`
	+ DM Title:
		- Tech Name: `s1kd-syncrefs`
		- Info Name: `Description`
* **DM Status**:
	+ Issue Type: `changed`
	+ Security:
		- Security Classification: `01`
	+ Responsible Partner Company:
		- Enterprise Name: `khzae.net`
	+ Originator:
		- Enterprise Name: `khzae.net`
	+ Applic:
		- Display Text:
			- Simple Para: `All`
	+ BrexDm Ref:
		- DM Ref:
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
	+ Quality Assurance:
		- Unverified
	+ Reason For Update:
		- ID: `rfu-xml-catalog`
		- Update Highlight: `1`
		- Update Reason Type: `urt02`
		- Simple Para: `Add --xml-catalog parser option.`

## Content
The content section contains the main body of the document.

### Description
The description section provides a detailed explanation of the `s1kd-syncrefs` tool.
#### General
The `s1kd-syncrefs` tool copies all external references (dmRef, pmRef, externalPubRef) within the content of a data module and uses them to generate the `<refs>` element. Each unique reference is copied, sorted, and placed in to the `<refs>` element. If a `<refs>` element already exists, it is overwritten.

#### Usage
The usage section explains how to use the `s1kd-syncrefs` tool.
```bash
s1kd-syncrefs [-dflqvh?] [-o <out>] [<data module>...]
```

#### Options
The options section lists the available command-line options for the `s1kd-syncrefs` tool.

| Option | Description |
| --- | --- |
| `-d, --delete` | Delete the `<refs>` element. |
| `-f, --overwrite` | Overwrite the data modules automatically. |
| `-h, -?, --help` | Show help/usage message. |
| `-l, --list` | Treat input (stdin or arguments) as lists of data modules to synchronize references in, rather than data modules themselves. |
| `-o, --out <out>` | The resulting XML is written to `<out>` instead of stdout. |
| `-q, --quiet` | Quiet mode. Errors are not printed. |
| `-v, --verbose` | Verbose output. |
| `--version` | Show version information. |
| `<data module>...` | The data module(s) to synchronize references in. Default is to read from stdin. |

In addition, the following options allow configuration of the XML parser:

| Option | Description |
| --- | --- |
| `--dtdload` | Load the external DTD. |
| `--huge` | Remove any internal arbitrary parser limits. |
| `--net` | Allow network access to load external DTD and entities. |
| `--noent` | Resolve entities. |
| `--parser-errors` | Emit errors from parser. |
| `--parser-warnings` | Emit warnings from parser. |
| `--xinclude` | Do XInclude processing. |
| `--xml-catalog <file>` | Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times. |

#### Exit Status
The exit status section explains the possible exit codes returned by the `s1kd-syncrefs` tool.

| Code | Description |
| --- | --- |
| 0 | No errors. |
| 1 | Invalid data module. |
| 2 | Number of references in a data module exceeded the available memory. |

#### Example
The example section provides an example usage of the `s1kd-syncrefs` tool.
```bash
$ s1kd-syncrefs -f DMC-EX-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
```