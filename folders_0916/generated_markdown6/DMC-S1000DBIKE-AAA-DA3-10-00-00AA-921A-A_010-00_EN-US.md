DMC-S1000DBIKE-AAA-DA3-10-00-00AA-921A-A_010-00_EN-US
==============================================

## Ident and Status Section
The `identAndStatusSection` contains information about the identification and status of the data module.

### DM Address
The `dmAddress` section contains the following elements:

* **DM Ident**: The `dmIdent` element contains the following attributes:
	+ modelIdentCode: S1000DBIKE
	+ systemDiffCode: AAA
	+ systemCode: DA3
	+ subSystemCode: 1
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 921
	+ infoCodeVariant: A
	+ itemLocationCode: A
* **Language**: The `language` element contains the following attributes:
	+ countryIsoCode: US
	+ languageIsoCode: en
* **Issue Info**: The `issueInfo` element contains the following attributes:
	+ issueNumber: 010
	+ inWork: 00

### DM Address Items
The `dmAddressItems` section contains the following elements:

* **Issue Date**: The `issueDate` element contains the following attributes:
	+ year: 2024
	+ month: 06
	+ day: 19
* **DM Title**: The `dmTitle` element contains the following elements:
	+ techName: Horn
	+ infoName: Remove and install a new item

### DM Status
The `dmStatus` section contains the following elements:

* **Issue Type**: changed
* **Security**: The `security` element contains the following attributes:
	+ securityClassification: 01
	+ commercialClassification: cc51
	+ caveat: cv51
* **Data Restrictions**: The `dataRestrictions` section contains the following elements:
	+ restrictionInstructions: 
		- dataDistribution: To be made available to all S1000D users.
		- exportControl: 
			- exportRegistrationStmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- dataHandling: There are no specific handling instructions for this data module.
		- dataDestruction: Users may destroy this data module in accordance with their own local procedures.
		- dataDisclosure: There are no dissemination limitations that apply to this data module.
	+ restrictionInfo:
		- copyright: 
			- copyrightPara: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
			- copyrightPara: Publishers:
			- randomList:
				+ listItem: Aerospace, Security and Defence Industries Association of Europe
				+ listItem: Aerospace Industries Association of America
				+ listItem: ATA e-Business Program
			- copyrightPara: Limitations of liability:
			- randomList:
				+ listItem: This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
				+ listItem: Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
				+ listItem: Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
			- copyrightPara: The details for copyright can be found in the S1000D Specification.
		- policyStatement: S1000D-SC-2016-017-002-00 Steering Committee TOR
		- dataConds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Responsible Partner Company
The `responsiblePartnerCompany` element contains the following attributes:
* enterpriseCode: B6865
* enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Originator
The `originator` element contains the following attributes:
* enterpriseCode: B6865
* enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Applic Cross Ref Table Ref
The `applicCrossRefTableRef` section contains the following elements:

* **DM Ref**: The `dmRef` element contains the following elements:
	+ dmRefIdent: 
		- dmCode: 
			- modelIdentCode: S1000DBIKE
			- systemDiffCode: AAA
			- systemCode: D00
			- subSystemCode: 0
			- subSubSystemCode: 0
			- assyCode: 00
			- disassyCode: 00
			- disassyCodeVariant: AA
			- infoCode: 00W
			- infoCodeVariant: A
			- itemLocationCode: D

### Applic
The `applic` section contains the following elements:

* **Display Text**: The `displayText` element contains the following text:
	+ simplePara: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Evaluate**: The `evaluate` element contains the following attributes and elements:
	+ andOr: and
	+ assert: 
		- applicPropertyIdent: type
		- applicPropertyType: prodattr
		- applicPropertyValues: Mountain bicycle
	+ evaluate: 
		- andOr: or
		- evaluate: 
			- andOr: and
			- assert: (not provided)
		- evaluate: 
			- andOr: and
			- assert: (not provided)

### Tech Notes
There are no technical notes in this section.

## Content
The `content` section contains the following elements:

### Procedure
The `procedure` section contains the following elements:

#### Preliminary Requirements
The `preliminaryRqmts` section contains the following elements:

* **Support Equipment**: The `reqSupportEquips` section contains the following elements:
	+ supportEquipDescrGroup: 
		- supportEquipDescr: 
			- name: Support Equipment (e.g. Tool Kit)
			- identNumber: 
				- manufacturerCode: KZ666
				- partAndSerialNumber: 
					- partNumber: BSK-TLST-001
			- reqQuantity: 1 (unit of measure: EA)
* **Spares**: The `reqSpares` section contains the following elements:
	+ spareDescrGroup: 
		- spareDescr: 
			- name: Horn
			- identNumber: 
				- manufacturerCode: KZ444
				- partAndSerialNumber: 
					- partNumber: Horn-001
			- reqQuantity: 1 (unit of measure: EA)

#### Main Procedure
The `mainProcedure` section contains the following elements:

* **Procedural Steps**: The `proceduralStep` elements contain the following text:
	1. Safely hold the bicycle.
	2. Remove the horn.
		- Use the 8mm Allen wrench from the Support Equipment (e.g. Tool Kit) and remove the two Allen screws.
		- Remove the horn.
	3. Install the new Horn.
		- Install the new Horn on the handlebars.
		- Use the 8mm Allen wrench from the Support Equipment (e.g. Tool Kit) and tighten the two Allen screws.

#### Closing Requirements
The `closeRqmts` section contains the following elements:

* **Required Conditions**: The `reqCondGroup` element contains the following text:
	+ Safely discard the horn that you removed, in accordance with Local Disposal Procedures.

Note: For a complete and accurate interpretation of this data module, please refer to the original XML file or consult with the relevant authorities.