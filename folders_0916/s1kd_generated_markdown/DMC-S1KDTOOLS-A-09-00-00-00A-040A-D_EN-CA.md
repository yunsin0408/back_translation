# DMC-S1KDTOOLS-A-09-00-00-00A-040A-D_EN-CA
## Ident and Status Section
The Ident and Status Section contains information about the document identification and status.

### DM Address
#### DM Ident
* **Model Ident Code:** S1KDTOOLS
* **System Diff Code:** A
* **System Code:** 09
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** A
* **Info Code:** 040
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:**
	+ **Language Iso Code:** en
	+ **Country Iso Code:** CA
* **Issue Info:**
	+ **Issue Number:** 036
	+ **In Work:** 00

#### DM Address Items
* **Issue Date:** 
	+ **Year:** 2020
	+ **Month:** 09
	+ **Day:** 01
* **DM Title:**
	+ **Tech Name:** s1kd-metadata
	+ **Info Name:** Description

### DM Status
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
	+ **Id:** rfu-xml-catalog
	+ **Update Highlight:** 1
	+ **Update Reason Type:** urt02
	+ **Simple Para:** Add --xml-catalog parser option.

## Content
### Description
#### General
The `s1kd-metadata` tool provides a simple way to fetch and change metadata on S1000D CSDB objects.

#### Usage
```bash
s1kd-metadata [options] [<object>...]
```

#### Options
The following options are available:
| Option | Description |
| --- | --- |
| `-n <name>` | Specify the name of the metadata to show or edit. |
| `-v <value>` | Specify the new value for the metadata specified by the preceding `-n` option. |
| `-w <name>` | Show or edit metadata only on objects where the value of `<name>` is equal to the value specified in the following `-v` option. |
| `-W <name>` | Show or edit metadata only on objects where the value of `<name>` is not equal to the value specified in the following `-v` option. |
| `--version` | Show version information. |
| `<object>...` | The object(s) to show/edit metadata on. The default is to read from stdin. |

Additional options for configuring the XML parser:
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
$ ls
DMC-S1KDTOOLS-A-09-00-00-00A-040A-D_EN-CA.XML
DMC-S1KDTOOLS-A-0Q-00-00-00A-040A-D_EN-CA.XML

$ DMOD=DMC-S1KDTOOLS-A-09-00-00-00A-040A-D_EN-CA.XML
$ s1kd-metadata $DMOD
issueDate                      2017-08-14
techName                       s1kd-metadata(1) | s1kd-tools
responsiblePartnerCompany      khzae.net
originator                     khzae.net
securityClassification         01
schema                         descript
schemaUrl                      http://www.s1000d.org/S1000D_5-0/xml_
schema_flat/descript.xsd
type                           dmodule
applic                         All
brex                           S1000D-F-04-10-0301-00A-022A-D
issueType                      new
languageIsoCode                en
countryIsoCode                 CA
issueNumber                    001
inWork                         00
dmCode                         S1KDTOOLS-A-09-00-00-00A-040A-D

$ s1kd-metadata -n techName -v "New title" $DMOD
$ s1kd-metadata -n techName $DMOD
New title

$ s1kd-metadata -n techName DMC-*.XML
New title
s1kd-aspp(1) | s1kd-tools

$ s1kd-metadata -F "%techName% (%issueDate%) %issueType%" DMC-*.XML
New title (2017-08-14) new
s1kd-aspp(1) | s1kd-tools (2018-03-28) changed

$ s1kd-metadata -F "%techName%" -w subSubSystemCode -v Q DMC-*.XML
s1kd-aspp(1) | s1kd-tools

$ s1kd-metadata -n path -w subSystemCode -v Q
DMC-S1KDTOOLS-A-0Q-00-00-00A-040A-D_EN-CA.XML

$ s1kd-metadata -n path -W subSystemCode -v Q
DMC-S1KDTOOLS-A-09-00-00-00A-040A-D_EN-CA.XML

$ s1kd-metadata -n path -w subSystemCode -m [0-9]
DMC-S1KDTOOLS-A-09-00-00-00A-040A-D_EN-CA.XML
```