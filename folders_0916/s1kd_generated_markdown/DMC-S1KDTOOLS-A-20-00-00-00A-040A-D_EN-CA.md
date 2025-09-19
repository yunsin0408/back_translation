DMC-S1KDTOOLS-A-20-00-00-00A-040A-D_EN-CA
=============================================

### Ident and Status Section

The ident and status section contains information about the data module.

#### DM Address

* **DM Ident**
	+ Model Ident Code: `S1KDTOOLS`
	+ System Diff Code: `A`
	+ System Code: `20`
	+ Sub System Code: `0`
	+ Sub Sub System Code: `0`
	+ Assy Code: `00`
	+ Disassy Code: `00`
	+ Disassy Code Variant: `A`
	+ Info Code: `040`
	+ Info Code Variant: `A`
	+ Item Location Code: `D`
* **Language**
	+ Language Iso Code: `en`
	+ Country Iso Code: `CA`
* **Issue Info**
	+ Issue Number: `026`
	+ In Work: `00`

#### DM Address Items

* **Issue Date**
	+ Year: `2020`
	+ Month: `09`
	+ Day: `01`
* **DM Title**
	+ Tech Name: `s1kd-acronyms`
	+ Info Name: `Description`

### DM Status

The DM status section contains information about the status of the data module.

* **Issue Type**: `changed`
* **Security**
	+ Security Classification: `01`
* **Responsible Partner Company**
	+ Enterprise Name: `khzae.net`
* **Originator**
	+ Enterprise Name: `khzae.net`
* **Applic**
	+ Display Text: `All`
* **BrexDm Ref**
	+ DM Ref Ident
		- Model Ident Code: `S1KDTOOLS`
		- System Diff Code: `A`
		- System Code: `00`
		- Sub System Code: `0`
		- Sub Sub System Code: `0`
		- Assy Code: `00`
		- Disassy Code: `00`
		- Disassy Code Variant: `A`
		- Info Code: `040`
		- Info Code Variant: `A`
		- Item Location Code: `D`
* **Reason for Update**
	+ ID: `rfu-xml-catalog`

### Content

The content section contains the main information of the data module.

#### Description

The description section contains a detailed explanation of the data module.

##### General Information

The `s1kd-acronyms` tool is used to find and markup acronyms in data modules.

##### Usage

The following are examples of how to use the `s1kd-acronyms` tool:

* List all acronyms used in all data modules: `$ s1kd-acronyms DMC-*.XML`
* Markup predefined acronyms in a data module: `$ s1kd-acronyms -mf DMC-EX-A-00-00-00-00A-040A-D_EN-CA.XML`
* Unmarkup acronyms in a data module: `$ s1kd-acronyms -Df DMC-EX-A-00-00-00-00A-040A-D_EN-CA.XML`

##### Options

The following are the available options for the `s1kd-acronyms` tool:

| Option | Description |
| --- | --- |
| `-m` | Markup predefined acronyms in a data module |
| `-f` | Unmarkup acronyms in a data module |
| `-T` | Only search for acronyms with an attribute `acronymType` whose value is contained within the string `<types>` |
| `-t` | Format XML output as an S1000D `<table>` |
| `-v` | Verbose output |
| `-X` | Use a custom XPath expression to specify which text nodes to search for acronyms in |
| `-x` | Use XML output instead of plain text |
| `-!` | Mark where acronyms are found using a `<chooseAcronym>` element |
| `--version` | Show version information |
| `--dtdload` | Load the external DTD |
| `--huge` | Remove any internal arbitrary parser limits |
| `--net` | Allow network access to load external DTD and entities |
| `--noent` | Resolve entities |
| `--parser-errors` | Emit errors from parser |
| `--parser-warnings` | Emit warnings from parser |
| `--xinclude` | Do XInclude processing |
| `--xml-catalog` | Use an XML catalog when resolving entities |

##### .acronyms File

The `.acronyms` file specifies a list of acronyms for a project. The following is an example of the format:
```xml
<acronyms>
  <acronym acronymType="at01">
    <acronymTerm>BREX</acronymTerm>
    <acronymDefinition>Business Rules Exchange</acronymDefinition>
  </acronym>
  <acronym acronymType="at01">
    <acronymTerm>SNS</acronymTerm>
    <acronymDefinition>Standard Numbering System</acronymDefinition>
  </acronym>
</acronyms>
```