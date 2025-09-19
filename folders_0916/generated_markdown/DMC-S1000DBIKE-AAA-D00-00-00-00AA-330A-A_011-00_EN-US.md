# DMC-S1000DBIKE-AAA-D00-00-00-00AA-330A-A_011-00_EN-US
## Introduction
The following document is based on the XML file `DMC-S1000DBIKE-AAA-D00-00-00-00AA-330A-A_011-00_EN-US.XML`. This markdown document aims to provide a clear and readable representation of the original XML content.

## IdentAndStatusSection
### dmAddress
#### dmIdent
* **dmCode**:
	+ modelIdentCode: S1000DBIKE
	+ systemDiffCode: AAA
	+ systemCode: D00
	+ subSystemCode: 0
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 330
	+ infoCodeVariant: A
	+ itemLocationCode: A
* **language**:
	+ countryIsoCode: US
	+ languageIsoCode: en
* **issueInfo**:
	+ issueNumber: 011
	+ inWork: 00

#### dmAddressItems
* **issueDate**:
	+ year: 2024
	+ month: 06
	+ day: 19
* **dmTitle**:
	+ techName: Bicycle
	+ infoName: Place on test stand

### dmStatus
* **issueType**: changed
#### security
* **securityClassification**: 01
* **commercialClassification**: cc51

#### dataRestrictions
##### restrictionInstructions
* **dataDistribution**: To be made available to all S1000D users.
* **exportControl**:
	+ exportRegistrationStmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
* **dataHandling**: There are no specific handling instructions for this data module.
* **dataDestruction**: Users may destroy this data module in accordance with their own local procedures.
* **dataDisclosure**: There are no dissemination limitations that apply to this data module.

##### restrictionInfo
* **copyright**:
	+ copyrightPara: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
	+ publishers:
		- Aerospace, Security and Defence Industries Association of Europe
		- Aerospace Industries Association of America
		- ATA e-Business Program
	+ limitations of liability:
		- This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
		- Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
		- Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* **policyStatement**: S1000D-SC-2016-017-002-00 Steering Committee TOR
* **dataConds**: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### responsiblePartnerCompany
* **enterpriseCode**: B6865
* **enterpriseName**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### originator
* **enterpriseCode**: B6865
* **enterpriseName**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### applicCrossRefTableRef
* **dmRef**:
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

#### applic
* **displayText**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **evaluate**:
	+ assert: type = Mountain bicycle
	+ evaluate:
		- assert: model = Mountain storm, version = Mk1
		- assert: model = Brook trekker, version = Mk9

#### techStandard
* **authorityInfoAndTp**:
	+ authorityInfo: 20010131
	+ techPubBase: Bike book
* **authorityExceptions**: None
* **authorityNotes**: None

#### brexDmRef
* **dmRef**:
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
			- infoCode: 022
			- infoCodeVariant: A
			- itemLocationCode: D

#### qualityAssurance
* **firstVerification**: tabtop

#### systemBreakdownCode
* **systemBreakdownCode**: BY112

#### skillLevel
* **skillLevelCode**: sk01

#### reasonForUpdate
* **id**: rfu_general
* **updateReasonType**: urt03
* **simplePara**: S1000D upissued

## Content
### Procedure
#### Preliminary Requirements
* **reqCondGroup**: No conditions
* **reqPersons**:
	+ person: A
		- personCategory: Basic user
		- trade: Operator
		- estimatedTime: 0.3 hours
* **reqSupportEquips**:
	+ supportEquipDescrGroup:
		- supportEquipDescr: seq-0001
			- name: Test stand
			- identNumber:
				- manufacturerCode: KZ666
				- partAndSerialNumber:
					- partNumber: BSK-TLST-999-01
			- reqQuantity: 1 EA
* **reqSupplies**: No supplies
* **reqSpares**: No spares
* **reqSafety**: No safety requirements

#### Main Procedure
1. Ensure the test stand is level.
2. Place the bicycle on the test stand.
3. Tighten clamps until the bicycle is securely attached to the test stand.

#### Close Requirements
* **reqCondGroup**: No conditions