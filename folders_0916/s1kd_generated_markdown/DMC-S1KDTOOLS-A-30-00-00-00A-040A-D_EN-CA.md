# DMC-S1KDTOOLS-A-30-00-00-00A-040A-D_EN-CA
## Ident and Status Section
The `identAndStatusSection` contains information about the document's identity and status.

### DM Address
The `dmAddress` section provides details about the document's address.
* **DM Ident**
	+ Model Ident Code: S1KDTOOLS
	+ System Diff Code: A
	+ System Code: 30
	+ Sub System Code: 0
	+ Sub Sub System Code: 0
	+ Assy Code: 00
	+ Disassy Code: 00
	+ Disassy Code Variant: A
	+ Info Code: 040
	+ Info Code Variant: A
	+ Item Location Code: D
* **Language**
	+ Language Iso Code: en
	+ Country Iso Code: CA
* **Issue Info**
	+ Issue Number: 022
	+ In Work: 00

### DM Address Items
The `dmAddressItems` section contains additional information about the document's address.
* **Issue Date**: 2020-09-01
* **DM Title**
	+ Tech Name: s1kd-defaults
	+ Info Name: Description

## Status
The `dmStatus` section provides information about the document's status.
* **Issue Type**: changed
* **Security Classification**: 01
* **Responsible Partner Company**: khzae.net
* **Originator**: khzae.net
* **Applic**: All
* **BrexDm Ref**
	+ DM Ref Ident
		- Model Ident Code: S1KDTOOLS
		- System Diff Code: A
		- System Code: 00
		- Sub System Code: 0
		- Sub Sub System Code: 0
		- Assy Code: 00
		- Disassy Code: 00
		- Disassy Code Variant: A
		- Info Code: 022
		- Info Code Variant: A
		- Item Location Code: D
* **Quality Assurance**: unverified
* **Reason for Update**
	+ ID: rfu-xml-catalog
	+ Change Type: add
	+ Reason for Update Ref IDs: rfu-xml-catalog

## Content
The `content` section contains the main content of the document.

### Description
The `description` section provides a detailed description of the s1kd-defaults tool.
#### General Information
The s1kd-defaults tool is used to generate default values for S1000D documents.

#### Options
The following options are available:
##### Configuration Options
* `-d` : Generate a `.defaults` file
* `-D` : Generate a `.dmtypes` file
* `-F` : Generate a `.fmtypes` file
* `-i` : Initialize a new CSDB
* `-n` : Set a default value for the specified key
* `-t` : Output in text format instead of XML
* `-v` : Set the value for the specified key

##### XML Parser Options
* `--dtdload` : Load the external DTD
* `--huge` : Remove any internal arbitrary parser limits
* `--net` : Allow network access to load external DTD and entities
* `--noent` : Resolve entities
* `--parser-errors` : Emit errors from parser
* `--parser-warnings` : Emit warnings from parser
* `--xinclude` : Do XInclude processing
* `--xml-catalog` : Use an XML catalog when resolving entities

#### .brexmap File
The `.brexmap` file specifies a mapping between BREX structure object rules and `.defaults` and `.dmtypes` files.

##### Example
```xml
<brexMap>
  <dmtypes path="//@infoCode"/>
  <default path="//@languageIsoCode" ident="languageIsoCode"/>
  <default path="//@countryIsoCode" ident="countryIsoCode"/>
</brexMap>
```

#### Examples
The following examples demonstrate how to use the s1kd-defaults tool:
##### Initialize a new CSDB using XML format
```bash
$ mkdir mycsdb
$ cd mycsdb
$ s1kd-defaults -i
```

##### Initialize a new CSDB using simple text format
```bash
$ mkdir mycsdb
$ cd mycsdb
$ s1kd-defaults -ti
```

##### Generate a custom-named `.defaults` file
```bash
$ s1kd-defaults > custom-defaults.xml
```

##### Convert a simple text formatted file to XML
```bash
$ s1kd-defaults -df
```

##### Sort entries and output in text format
```bash
$ s1kd-defaults -dts custom-defaults.txt
```

##### Set a default value in the current `.defaults` file
```bash
$ s1kd-defaults -df -n issue -v 5.0
```