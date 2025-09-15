DMC-S1KDTOOLS-A-16-00-00-00A-040A-D_EN-CA
==============================================

## Ident and Status Section
The ident and status section contains information about the document identification and its current status.

### DM Address
The DM address section provides details about the document's identification and addressing.

#### DM Ident
The DM ident section contains the following attributes:
* `modelIdentCode`: S1KDTOOLS
* `systemDiffCode`: A
* `systemCode`: 16
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: A
* `infoCode`: 040
* `infoCodeVariant`: A
* `itemLocationCode`: D

The language details are:
* `languageIsoCode`: en
* `countryIsoCode`: CA

Issue information:
* `issueNumber`: 028
* `inWork`: 00

#### DM Address Items
The issue date is: 
* Year: 2020
* Month: 09
* Day: 01

The document title is:
### s1kd-newcom - Description

### DM Status
The current status of the document is:
* `issueType`: changed

Security classification: 
* `securityClassification`: 01

Responsible partner company: 
* Enterprise name: khzae.net

Originator:
* Enterprise name: khzae.net

Applicability:
* Display text: All

BREX DM reference:
* Model ident code: S1KDTOOLS
* System diff code: A
* System code: 00
* Sub system code: 0
* Sub sub system code: 0
* Assy code: 00
* Disassy code: 00
* Disassy code variant: A
* Info code: 022
* Info code variant: A
* Item location code: D

Quality assurance:
* Unverified

Reason for update:
* ID: rfu-xml-catalog
* Update highlight: 1
* Update reason type: urt02
* Simple para: Add --xml-catalog parser option.

## Content
The content section contains references and descriptions of the document.

### References
Reference to another DM:
* Model ident code: S1KDTOOLS
* System diff code: A
* System code: 07
* Sub system code: 0
* Sub sub system code: 0
* Assy code: 00
* Disassy code: 00
* Disassy code variant: A
* Info code: 040
* Info code variant: A
* Item location code: D

Reference title:
### s1kd-newdm - Description

### Description
The description section contains detailed information about the document.

#### General
The `s1kd-newcom` tool creates a new S1000D comment with the specified code and metadata.

#### Usage
Usage: `s1kd-newcom [options]`

#### Options
Available options:
| Option | Description |
| --- | --- |
| -#, --code \<code> | The code of the comment, in the form of MODELIDENTCODE-SENDERIDENT-YEAR-SEQ-TYPE. |
| -$, --issue \<issue> | Specify which issue of S1000D to use. Supported issues are: 5.0 (default), 4.2, 4.1, 4.0, 3.0, 2.3, 2.2, 2.1, and 2.0. |
| -@, --out \<path> | Save the new comment to \<path>. If \<path> is a directory, the comment will be saved with a default filename. |
| -L, --language \<lang> | The language ISO code of the new comment. |
| -m, --remarks \<remarks> | Set the remarks for the new comment. |
| -o, --origname \<orig> | The enterprise name of the originator of the comment. |
| -P, --priority \<code> | The priority code of the new comment. |
| -p, --prompt | Prompt the user for values left unspecified. |
| -q, --quiet | Do not report an error when the file already exists. |
| -r, --response \<type> | The response type of the new comment. |
| -t, --title \<title> | The title of the new comment. |
| -v, --verbose | Print the filename of the newly created comment. |
| -z, --issue-type \<type> | The issue type of the new comment. |
| --version | Show version information. |

Additional options for XML parser configuration:
| Option | Description |
| --- | --- |
| --dtdload | Load the external DTD. |
| --huge | Remove any internal arbitrary parser limits. |
| --net | Allow network access to load external DTD and entities. |
| --noent | Resolve entities. |
| --parser-errors | Emit errors from parser. |
| --parser-warnings | Emit warnings from parser. |
| --xinclude | Do XInclude processing. |
| --xml-catalog \<file> | Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times. |

#### .defaults file
Refer to [s1kd-newdm - Description](#) for information on the `.defaults` file used by all `s1kd-new*` commands.

#### Example
Example usage: `$ s1kd-newcom -# EX-12345-2018-00001-Q`