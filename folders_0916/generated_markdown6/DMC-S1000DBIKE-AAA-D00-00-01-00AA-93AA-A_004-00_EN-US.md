# DMC-S1000DBIKE-AAA-D00-00-01-00AA-93AA-A_004-00_EN-US
## Introduction
The document `DMC-S1000DBIKE-AAA-D00-00-01-00AA-93AA-A_004-00_EN-US` is a S1000D XML file that contains information about the modification procedures for a bicycle axis.

## Ident and Status Section
### DM Address
#### DM Ident
The DM ident section contains the following attributes:
* `modelIdentCode`: S1000DBIKE
* `systemDiffCode`: AAA
* `systemCode`: D00
* `subSystemCode`: 0
* `subSubSystemCode`: 0
* `assyCode`: 01
* `disassyCode`: 00
* `disassyCodeVariant`: AA
* `infoCode`: 93A
* `infoCodeVariant`: A
* `itemLocationCode`: A

The language section contains the following attributes:
* `countryIsoCode`: US
* `languageIsoCode`: en

The issue info section contains the following attributes:
* `issueNumber`: 004
* `inWork`: 00

#### DM Address Items
The issue date is: 
* `year`: 2024
* `month`: 06
* `day`: 19

The DM title is:
### Technical Name: Bicycle axis
### Information Name: Modification procedures

### DM Status
The issue type is: status

#### Security
The security section contains the following attributes:
* `securityClassification`: 01
* `commercialClassification`: cc51
* `caveat`: cv51

#### Data Restrictions
The data restrictions section contains the following information:

##### Restriction Instructions
* **Data Distribution**: To be made available to all S1000D users.
* **Export Control**:
	+ Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted.
	+ Storage of this data module is to be at the discretion of the organization.
* **Data Handling**: There are no specific handling instructions for this data module.
* **Data Destruction**: Users may destroy this data module in accordance with their own local procedures.
* **Data Disclosure**: There are no dissemination limitations that apply to this data module.

##### Restriction Info
* **Copyright**:
	+ Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
	+ Publishers:
		- Aerospace, Security and Defence Industries Association of Europe
		- Aerospace Industries Association of America
		- ATA e-Business Program
	+ Limitations of liability:
		- This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
		- Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
		- Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* **Policy Statement**: S1000D-SC-2016-017-002-00 Steering Committee TOR
* **Data Conds**: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company
The responsible partner company is:
* `enterpriseCode`: B6865
* `enterpriseName`: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Originator
The originator is:
* `enterpriseCode`: B6865
* `enterpriseName`: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Applic Cross Ref Table Ref
The applic cross ref table ref section contains the following information:
* `dmRefIdent`:
	+ `modelIdentCode`: S1000DBIKE
	+ `systemDiffCode`: AAA
	+ `systemCode`: D00
	+ `subSystemCode`: 0
	+ `subSubSystemCode`: 0
	+ `assyCode`: 00
	+ `disassyCode`: 00
	+ `disassyCodeVariant`: AA
	+ `infoCode`: 00W
	+ `infoCodeVariant`: A
	+ `itemLocationCode`: D

#### Applic
The applic section contains the following information:
* **Display Text**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Evaluate**:
	+ `andOr`: and
	+ `assert`:
		- `applicPropertyIdent`: type
		- `applicPropertyType`: prodattr
		- `applicPropertyValues`: Mountain bicycle
	+ `evaluate`:
		- `andOr`: or
		- `evaluate`:
			- `andOr`: and
			- `assert`:
				- `applicPropertyIdent`: type
				- `applicPropertyType`: prodattr
				- `applicPropertyValues`: Mountain storm Mk1
			- `assert`:
				- `applicPropertyIdent`: type
				- `applicPropertyType`: prodattr
				- `applicPropertyValues`: Brook trekker Mk9

#### Tech Status
Not specified in the provided XML.

## Content
### Preliminary Requirements
The preliminary requirements section contains the following information:

#### Required Support Equipment
* **Support Equip Descr Group**:
	+ `supportEquipDescr`:
		- `materialUsage`: mu05 (material set)
		- `name`: Saw tool set
		- `materialSetRef`:
			- `materialSetIdent`: BSK-TLST-200
			- `materialSetIssue`: 001
			- `dmRef`:
				- `modelIdentCode`: S1000DBIKE
				- `systemDiffCode`: AAA
				- `systemCode`: D00
				- `subSystemCode`: 0
				- `subSubSystemCode`: 0
				- `assyCode`: 01
				- `disassyCode`: 00
				- `disassyCodeVariant`: AA
				- `infoCode`: 930
				- `infoCodeVariant`: A
				- `itemLocationCode`: A
				- `issueInfo`:
					- `issueNumber`: 004
					- `inWork`: 00
		- `reqQuantity`:
			- `unitOfMeasure`: EA
			- `quantity`: 1
		- **Embedded Support Equip Descr**:
			- `id`: seq-0001
			- `name`: Saw tool
			- `identNumber`:
				- `manufacturerCode`: KZ666
				- `partAndSerialNumber`:
					- `partNumber`: BSK-TW-100
			- `reqQuantity`:
				- `unitOfMeasure`: EA
				- `quantity`: 1
		- **Embedded Support Equip Descr**:
			- `id`: seq-0002
			- `name`: Threading tool
			- `identNumber`:
				- `manufacturerCode`: KZ666
				- `partAndSerialNumber`:
					- `partNumber`: BSK-THR-3001
			- `reqQuantity`:
				- `unitOfMeasure`: EA
				- `quantity`: 1

#### Required Spares
* **Spare Descr Group**:
	+ `spareDescr`:
		- `id`: spa-0001
		- `materialUsage`: mu03 (modified from)
		- `name`: Wheel axis
		- `identNumber`:
			- `manufacturerCode`: KZ666
			- `partAndSerialNumber`:
				- `partNumber`: BSK-AXS-2001
		- `reqQuantity`:
			- `unitOfMeasure`: EA
			- `quantity`: 1
		- **Embedded Spare Descr**:
			- `id`: spa-0002
			- `name`: Wheel axis
			- `identNumber`:
				- `manufacturerCode`: KZ666
				- `partAndSerialNumber`:
					- `partNumber`: BSK-AXS-2000
			- `reqQuantity`:
				- `unitOfMeasure`: EA
				- `quantity`: 1

### Main Procedure
The main procedure section contains the following steps:

#### Procedural Step 1
Use the (internal reference to seq-0001, supequip) to saw the (internal reference to spa-0002, spare)

#### Procedural Step 2
Use the (internal reference to seq-0002, supequip) when the saw is unbended

#### Procedural Step 3
Put the frame on the floor

### Close Requirements
The close requirements section contains no conditions.