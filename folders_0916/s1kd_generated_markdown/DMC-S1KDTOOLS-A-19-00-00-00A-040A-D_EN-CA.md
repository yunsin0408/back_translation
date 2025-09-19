# DMC-S1KDTOOLS-A-19-00-00-00A-040A-D_EN-CA
## Introduction
The `DMC-S1KDTOOLS-A-19-00-00-00A-040A-D_EN-CA.XML` file is a S1000D document that provides information about the `s1kd-mvref` tool. This markdown document is a conversion of the original XML file.

## Ident and Status Section
### DM Address
The DM address section contains information about the document identifier and status.
#### DM Ident
* **Model Ident Code:** S1KDTOOLS
* **System Diff Code:** A
* **System Code:** 19
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** A
* **Info Code:** 040
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:**
	+ **Language ISO Code:** en
	+ **Country ISO Code:** CA
* **Issue Info:**
	+ **Issue Number:** 024
	+ **In Work:** 00

#### DM Address Items
* **Issue Date:** 2020-09-01
* **DM Title:**
	+ **Tech Name:** s1kd-mvref
	+ **Info Name:** Description

### DM Status
The DM status section contains information about the document status.
* **Issue Type:** changed
* **Security:**
	+ **Security Classification:** 01
* **Responsible Partner Company:**
	+ **Enterprise Name:** khzae.net
* **Originator:**
	+ **Enterprise Name:** khzae.net
* **Applic:**
	+ **Display Text:** All
* **BrexDm Ref:**
	+ **DM Ref Ident:**
		- **Model Ident Code:** S1KDTOOLS
		- **System Diff Code:** A
		- **System Code:** 00
		- **Sub System Code:** 0
		- **Sub Sub System Code:** 0
		- **Assy Code:** 00
		- **Disassy Code:** 00
		- **Disassy Code Variant:** A
		- **Info Code:** 022
		- **Info Code Variant:** A
		- **Item Location Code:** D
* **Quality Assurance:**
	+ **Unverified:** 
* **Reason For Update:**
	+ **ID:** rfu-xml-catalog
	+ **Update Highlight:** 1
	+ **Update Reason Type:** urt02
	+ **Simple Para:** Add --xml-catalog parser option.

## Content
### Description
The description section contains information about the `s1kd-mvref` tool.
#### General
The `s1kd-mvref` tool changes all references to one object (the source object) into references to another object (the target object) in a specified set of objects.

#### Usage
```bash
s1kd-mvref [-d <dir>] [-s <source>] [-t <target>] [-cflqvh?] 
           [<object>...]
```
#### Options
The following options are available:
##### Main Options
| Option | Description |
| --- | --- |
| `-c, --content` | Only move references within the content section of objects. |
| `-d, --dir <dir>` | Move references in all objects in the specified directory. |
| `-f, --overwrite` | Overwrite updated input objects. |
| `-h, -?, --help` | Show help/usage message |
| `-l, --list` | Treat input as a list of data module filenames, rather than a data module itself. |
| `-q, --quiet` | Quiet mode. Errors are not printed. |
| `-s, --source <source>` | The source object. |
| `-t, --target <target>` | Change all references to the source object specified with -s into references that point to <target>. |
| `-v, --verbose` | Verbose output. |
| `--version` | Show version information. |
| `<object>...` | Objects to move references in. |

##### XML Parser Options
The following options allow configuration of the XML parser:
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

#### Example
```bash
$ s1kd-mvref -f -s <old DM> -t <new DM> DMC-*.XML
```
This command changes all references to the old data module (`<old DM>`) into references to the new data module (`<new DM>`) in all objects with filenames matching `DMC-*.XML`. The `-f` option overwrites the updated input objects.