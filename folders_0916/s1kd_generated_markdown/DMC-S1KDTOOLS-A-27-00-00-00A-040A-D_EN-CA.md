# DMC-S1KDTOOLS-A-27-00-00-00A-040A-D_EN-CA
## Introduction
The following document is a conversion of the XML file `DMC-S1KDTOOLS-A-27-00-00-00A-040A-D_EN-CA.XML` to markdown format.

## Ident and Status Section
### DM Address
#### DM Ident
The DM ident section contains the following attributes:
* `modelIdentCode`: S1KDTOOLS
* `systemDiffCode`: A
* `systemCode`: 27
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: A
* `infoCode`: 040
* `infoCodeVariant`: A
* `itemLocationCode`: D

The language used in this document is:
* `languageIsoCode`: en
* `countryIsoCode`: CA

The issue information is:
* `issueNumber`: 014
* `inWork`: 00

#### DM Address Items
The issue date is:
* `year`: 2020
* `month`: 09
* `day`: 01

The DM title is:
* `techName`: s1kd-addicn
* `infoName`: Description

### DM Status
The issue type is: changed

#### Security
The security classification is: 01

#### Responsible Partner Company
The enterprise name is: khzae.net

#### Originator
The enterprise name is: khzae.net

#### Applic
The display text is: All

#### BrexDmRef
The DM reference ident contains the following attributes:
* `modelIdentCode`: S1KDTOOLS
* `systemDiffCode`: A
* `systemCode`: 00
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: A
* `infoCode`: 022
* `infoCodeVariant`: A
* `itemLocationCode`: D

#### Quality Assurance
The quality assurance status is: unverified

#### Reason for Update
The reason for update is:
* `id`: rfu-xml-catalog
* `updateHighlight`: 1
* `updateReasonType`: urt02
The update reason is: Add --xml-catalog parser option.

## Content
### Description
The description section contains the following levelled paragraphs:

#### General
The s1kd-addicn tool adds the required DTD entity and notation declarations to an S1000D module in order to reference an ICN file.

#### Usage
The usage of the tool is:
```bash
s1kd-addicn [-o <file>] [-s <src>] [-fh?] <ICN>...
```

#### Options
The available options are:

| Option | Description |
| --- | --- |
| -F, --full-path | Use the whole path given for the ICN file as the SYSTEM ID. |
| -f, --overwrite | Overwrite source file instead of writing to stdout. |
| -h, -?, --help | Show help/usage message. |
| -o, --out <out> | The filename to output to. Default is to write to stdout. |
| -s, --source <src> | The source module to add the ICN(s) to. Default is to read from stdin. |
| --version | Show version information. |
| <ICN>... | Any number of ICN files to add. |

Additional options for configuring the XML parser:

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

#### Example
An example usage of the tool is:
```bash
$ s1kd-addicn -fs <DM> ICN-EX-12345-001-01.JPG
```

Note: This markdown document is a conversion of the original XML file and follows the same schema and structure.