DMC-S1KDTOOLS-A-35-00-00-00A-040A-D_EN-CA
==============================================

### Ident and Status Section
The Ident and Status section contains information about the identification and status of the data module.

#### DM Address
The DM address section contains information about the data module's identification and address.

##### DM Ident
The DM ident section contains the following attributes:
* `modelIdentCode`: S1KDTOOLS
* `systemDiffCode`: A
* `systemCode`: 35
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: A
* `infoCode`: 040
* `infoCodeVariant`: A
* `itemLocationCode`: D

The language and country codes are:
* `languageIsoCode`: en
* `countryIsoCode`: CA

The issue information is:
* `issueNumber`: 012
* `inWork`: 00

##### DM Address Items
The DM address items section contains the following information:
* `issueDate`: 
	+ `year`: 2020
	+ `month`: 09
	+ `day`: 01
* `dmTitle`:
	+ `techName`: s1kd-newsmc
	+ `infoName`: Description

#### DM Status
The DM status section contains the following information:
* `issueType`: changed
* `securityClassification`: 01
* `responsiblePartnerCompany`: khzae.net
* `originator`: khzae.net
* `applic`:
	+ `displayText`: All
* `brexDmRef`:
	+ `dmRefIdent`:
		- `modelIdentCode`: S1KDTOOLS
		- `systemDiffCode`: A
		- `systemCode`: 00
		- `subSystemCode`: 0
		- `subSubSystemCode`: 0
		- `assyCode`: 00
		- `disassyCode`: 00
		- `disassyCodeVariant`: A
		- `infoCode`: 040
		- `infoCodeVariant`: A
		- `itemLocationCode`: D

### Content
The content section contains the description of the data module.

#### Description
The description section contains the following information:
##### Introduction
The s1kd-newsmc command is used to create a new SCORM content package.

##### Usage
The usage of the command is as follows:
```bash
$ s1kd-newsmc [options] <DM>...
```
The options are:

| Option | Description |
| --- | --- |
| -# | Specify the SCORM code |
| --dtdload | Load the external DTD |
| --huge | Remove any internal arbitrary parser limits |
| --net | Allow network access to load external DTD and entities |
| --noent | Resolve entities |
| --parser-errors | Emit errors from parser |
| --parser-warnings | Emit warnings from parser |
| --xinclude | Do XInclude processing |
| --xml-catalog | Use an XML catalog when resolving entities |
| -@ | Specify the input file |
| -v | Print the version information |

The `<DM>` argument specifies the data module to be referenced in the new SCORM content package.

##### Options
The following options are available:

* `-# <code>`: Specify the SCORM code
* `--dtdload`: Load the external DTD
* `--huge`: Remove any internal arbitrary parser limits
* `--net`: Allow network access to load external DTD and entities
* `--noent`: Resolve entities
* `--parser-errors`: Emit errors from parser
* `--parser-warnings`: Emit warnings from parser
* `--xinclude`: Do XInclude processing
* `--xml-catalog <file>`: Use an XML catalog when resolving entities
* `-@ <file>`: Specify the input file
* `-v`: Print the version information

The following options allow configuration of the XML parser:
* `--dtdload`
* `--huge`
* `--net`
* `--noent`
* `--parser-errors`
* `--parser-warnings`
* `--xinclude`
* `--xml-catalog`

##### Defaults File
Refer to [s1kd-newdm](#) for information on the `.defaults` file which is used by all the s1kd-new\* commands.

##### Example
The following example creates a new SCORM content package with the SCORM code EX-12345-00001-00:
```bash
$ s1kd-newsmc -# EX-12345-00001-00
```
Note: The above markdown document is a clean and well-structured representation of the provided XML data. It includes all the necessary information from the original XML file, formatted in a clear and readable manner.