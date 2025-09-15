DMC-S1KDTOOLS-A-21-00-00-00A-040A-D_EN-CA
=============================================

### Ident and Status Section
The `identAndStatusSection` contains information about the identification and status of the data module.

#### DM Address
The `dmAddress` section provides details about the data module's address.

##### DM Identification
The `dmIdent` section contains the following attributes:
* `modelIdentCode`: S1KDTOOLS
* `systemDiffCode`: A
* `systemCode`: 21
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: A
* `infoCode`: 040
* `infoCodeVariant`: A
* `itemLocationCode`: D

The `language` section contains the following attributes:
* `languageIsoCode`: en
* `countryIsoCode`: CA

The `issueInfo` section contains the following attributes:
* `issueNumber`: 033
* `inWork`: 00

##### DM Address Items
The `dmAddressItems` section contains the following information:
* `issueDate`: 2020-09-01
* `dmTitle`:
	+ `techName`: s1kd-newdml
	+ `infoName`: Description

#### DM Status
The `dmStatus` section provides details about the data module's status.

##### Issue Type and Security Classification
* `issueType`: changed
* `securityClassification`: 01

##### Responsible Partner Company and Originator
* `enterpriseName`: khzae.net (responsible partner company)
* `enterpriseName`: khzae.net (originator)

##### Applicability and BREX DM Reference
* `applic`:
	+ `displayText`: All
* `brexDmRef`:
	+ `dmRefIdent`:
		- `modelIdentCode`: S1KDTOOLS
		- `systemDiffCode`: A
		- `systemCode`: 07
		- `subSystemCode`: 0
		- `subSubSystemCode`: 0
		- `assyCode`: 00
		- `disassyCode`: 00
		- `disassyCodeVariant`: A
		- `infoCode`: 040
		- `infoCodeVariant`: A
		- `itemLocationCode`: D

### Content
The `content` section contains the main information about the data module.

#### Description
The `description` section provides a detailed description of the data module.

##### Introduction
The s1kd-newdml command is used to create a new data management list (DML).

##### Usage
The usage of the command is as follows:
```bash
$ s1kd-newdml [options]
```
The available options are:

* `-#`: Specify the DML number.
* `--version`: Show version information.
* `--help`: Display help and exit.

##### Options
The following options are available:

| Option | Description |
| --- | --- |
| `-#` | Specify the DML number. |
| `--version` | Show version information. |
| `--help` | Display help and exit. |
| `--dtdload` | Load the external DTD. |
| `--huge` | Remove any internal arbitrary parser limits. |
| `--net` | Allow network access to load external DTD and entities. |
| `--noent` | Resolve entities. |
| `--parser-errors` | Emit errors from parser. |
| `--parser-warnings` | Emit warnings from parser. |
| `--xinclude` | Do XInclude processing. |
| `--xml-catalog` | Use an XML catalog when resolving entities. |

##### .defaults File
Refer to the [s1kd-newdm](#) documentation for information on the `.defaults` file, which is used by all the s1kd-new\* commands.

##### Example
An example usage of the command is as follows:
```bash
$ s1kd-newdml -# EX-12345-C-2018-00001
```
This will create a new DML with the specified number.