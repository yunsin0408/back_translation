# DMC-S1KDTOOLS-A-00-00-00-00A-022A-D_EN-CA
## Introduction
The following document is based on the XML file `DMC-S1KDTOOLS-A-00-00-00-00A-022A-D_EN-CA.XML`. This markdown document aims to provide a clear and readable representation of the original XML content.

## Ident and Status Section
### DM Address
#### DM Ident
The following attributes are associated with the `dmIdent` element:
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

The language and issue information are as follows:
* Language: English (en) - Canada (CA)
* Issue Number: 001
* In Work: 01

#### DM Address Items
The following attributes are associated with the `dmAddressItems` element:
* Issue Date: 2018-09-21
* DM Title:
	+ Technical Name: s1kd-tools
	+ Information Name: Business rules

### DM Status
The following attributes are associated with the `dmStatus` element:
* Issue Type: changed
* Security Classification: 01
* Responsible Partner Company: khzae.net
* Originator: khzae.net
* Applic: All
* BREX DM Ref:
	+ DM Ref Ident:
		- Model Identification Code: S1KDTOOLS
		- System Difference Code: A
		- System Code: 00
		- Subsystem Code: 0
		- Sub-subsystem Code: 0
		- Assembly Code: 00
		- Disassembly Code: 00
		- Disassembly Code Variant: A
		- Information Code: 022
		- Information Code Variant: A
		- Item Location Code: D

## Content
### BREX
The following sections are part of the `brex` element:
#### SNS Rules
The SNS description includes a list of SNS systems with their corresponding codes and titles:

| SNS Code | SNS Title |
| --- | --- |
| 00 | s1kd-tools |
| 01 | s1kd-syncrefs |
| 02 | s1kd-validate |
| 03 | s1kd-instance |
| 04 | s1kd-brexcheck |
| 05 | s1kd-upissue |
| 06 | s1kd-ls |
| 07 | s1kd-newdm |
| 08 | s1kd-ref |
| 09 | s1kd-metadata |
| 12 | s1kd-newpm |
| 13 | s1kd-newimf |
| 14 | s1kd-neutralize |
| 15 | s1kd-transform |
| 16 | s1kd-newcom |
| 17 | s1kd-newddn |
| 19 | s1kd-checkrefs |
| 20 | s1kd-acronyms |
| 21 | s1kd-newdml |
| 22 | s1kd-dmrl |
| 23 | s1kd-flatten |
| 25 | s1kd-refls |
| 26 | s1kd-aspp |
| 27 | s1kd-addicn |
| 28 | s1kd-index |
| 30 | s1kd-defaults |
| 31 | s1kd-newupf |
| 32 | s1kd-icncatalog |
| 33 | s1kd-fmgen |
| 34 | s1kd-sns |
| 35 | s1kd-newsmc |

#### Context Rules
The context rules include a structure object rule group with multiple structure object rules:

##### Structure Object Rule Group

The following structure object rules are defined:
1. **Model Identification Code**
	* Object Path: `//dmIdent/dmCode/@modelIdentCode`
	* Allowed Object Flag: 2
	* Object Use: The model identification code must be S1KDTOOLS.
	* Object Value: s1kd-tools (single value, allowed value: S1KDTOOLS)
2. **System Difference Code**
	* Object Path: `//dmIdent/dmCode/@systemDiffCode`
	* Allowed Object Flag: 2
	* Object Use: The system difference code must be A.
	* Object Value: Default system diff code (single value, allowed value: A)
3. **Disassembly Code Variant**
	* Object Path: `//dmIdent/dmCode/@disassyCodeVariant`
	* Allowed Object Flag: 2
	* Object Use: The disassembly code variant must be a single alpha character.
	* Object Value: Alpha character (range value, allowed values: A-Z)
4. **Information Code Variant**
	* Object Path: `//dmIdent/dmCode/@infoCodeVariant`
	* Allowed Object Flag: 2
	* Object Use: The information code variant must be a single alpha character.
	* Object Value: Alpha character (range value, allowed values: A-Z)