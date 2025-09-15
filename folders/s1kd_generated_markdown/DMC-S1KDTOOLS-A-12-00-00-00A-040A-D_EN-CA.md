DMC-S1KDTOOLS-A-12-00-00-00A-040A-D_EN-CA
==============================================

## Ident and Status Section
The Ident and Status Section contains information about the identification and status of the publication module.

### DM Address
The DM Address section provides details about the publication module's address.

#### DM Ident
The DM Ident section contains the following attributes:
* `modelIdentCode`: S1KDTOOLS
* `systemDiffCode`: A
* `systemCode`: 12
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: A
* `infoCode`: 040
* `infoCodeVariant`: A
* `itemLocationCode`: D

The language of the publication module is:
* `languageIsoCode`: en
* `countryIsoCode`: CA

The issue information is:
* `issueNumber`: 030
* `inWork`: 00

#### DM Address Items
The DM Address Items section contains the following information:
* Issue date: 
	+ `year`: 2020
	+ `month`: 09
	+ `day`: 01
* DM title: 
	+ Technical name: s1kd-newpm
	+ Information name: Description

### DM Status
The DM Status section provides details about the publication module's status.

#### Issue Type
The issue type is: changed

#### Security
The security classification is: 01

#### Responsible Partner Company
The responsible partner company enterprise name is: khm (not specified in the provided XML)

#### Reason for Update
The reason for update reference IDs is: rfu-xml-catalog

## Content
The content section contains information about the publication module's content.

### Description
The description of the publication module is as follows:

#### General Information
The `s1kd-newpm` command is used to create a new publication module. The general syntax of the command is:
```bash
$ s1kd-newpm [options] <DM>...
```
The options for the command are:

| Option | Description |
| --- | --- |
| `-#` | Publication module number (required) |
| `--dtdload` | Load the external DTD |
| `--huge` | Remove any internal arbitrary parser limits |
| `--net` | Allow network access to load external DTD and entities |
| `--noent` | Resolve entities |
| `--parser-errors` | Emit errors from parser |
| `--parser-warnings` | Emit warnings from parser |
| `--xinclude` | Do XInclude processing |
| `--xml-catalog` | Use an XML catalog when resolving entities |
| `-h`, `-?`, `--help` | Show help/usage message |
| `-I` | Issue date in the form of YYYY-MM-DD |
| `-i` | Include issue information in referenced data modules |
| `-L` | Language ISO code |
| `-l` | Include language information in referenced data modules |
| `-m` | Remarks for the new publication module |
| `-n` | Issue number |
| `-p` | Prompt the user for any values left unspecified |
| `-q` | Do not report an error when the file already exists |
| `-R` | CAGE code of the responsible partner company |
| `-r` | Responsible partner company enterprise name |
| `-s` | Short title |
| `-T` | Include titles in referenced data modules |
| `-t` | Title |
| `-v` | Print the file name of the newly created publication module |
| `-w` | Inwork number |
| `-z` | Issue type |
| `--version` | Show version information |

#### Defaults File
The `.defaults` file is used by all the `s1kd-new*` commands. Refer to [s1kd-newdm](#) for more information on the `.defaults` file.

#### Example Usage
An example of using the `s1kd-newpm` command is:
```bash
$ s1kd-newpm -# EX-12345-00001-00
```
Note: The provided XML does not contain any specific data for the `<DM>...` section, so it has been omitted in this markdown document.