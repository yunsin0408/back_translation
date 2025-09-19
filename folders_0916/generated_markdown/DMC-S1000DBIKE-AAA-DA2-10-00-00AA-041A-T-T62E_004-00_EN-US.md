DMC-S1000DBIKE-AAA-DA2-10-00-00AA-041A-T-T62E_004-00_EN-US
============================================
### Ident and Status Section
The following section provides identification and status information for the data module.

#### DM Address
The DM address contains the following elements:

* **DM Ident**: This section identifies the data module.
	+ `dmCode` attributes:
		- `modelIdentCode`: S1000DBIKE
		- `systemDiffCode`: AAA
		- `systemCode`: DA2
		- `subSystemCode`: 1
		- `subSubSystemCode`: 0
		- `assyCode`: 00
		- `disassyCode`: 00
		- `disassyCodeVariant`: AA
		- `infoCode`: 041
		- `infoCodeVariant`: A
		- `itemLocationCode`: T
		- `learnCode`: T62
		- `learnEventCode`: E
	+ `language` attributes:
		- `countryIsoCode`: US
		- `languageIsoCode`: en
	+ `issueInfo` attributes:
		- `issueNumber`: 004
		- `inWork`: 00
* **DM Address Items**: This section contains additional address information.
	+ `issueDate` attributes:
		- `year`: 2024
		- `month`: 06
		- `day`: 19
	+ `dmTitle` elements:
		- `techName`: Steering
		- `infoName`: Description of how it is made: Knowledge Check

#### DM Status
The DM status contains the following elements:

* **Issue Type**: The issue type is `status`.
* **Security**:
	+ `securityClassification`: 01
* **Data Restrictions**:
	+ **Restriction Instructions**:
		- `dataDistribution`: To be made available to all S1000D users.
		- `exportControl`:
			- `exportRegistrationStmt`: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- `dataHandling`: There are no specific handling instructions for this data module.
		- `dataDestruction`: Users may destroy this data module in accordance with their own local procedures.
		- `dataDisclosure`: There are no dissemination limitations that apply to this data module.
	+ **Restriction Info**:
		- **Copyright**:
			- Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
			- Publishers:
				1. Aerospace, Security and Defence Industries Association of Europe
				2. Aerospace Industries Association of America
				3. ATA e-Business Program
			- Limitations of liability:
				1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
				2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
				3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
			- The details for copyright can be found in the S1000D Specification.
		- `policyStatement`: S1000D-SC-2016-017-002-00 Steering Committee TOR
		- `dataConds`: There are no known conditions that would change the data restrictions for, or security classification of, this data module.
* **Responsible Partner Company**:
	+ `enterpriseCode`: B6865
	+ `enterpriseName`: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
* **Originator**:
	+ `enterpriseCode`: B6865
	+ `enterpriseName`: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
* **Applic**:
	+ `displayText`: All
* **BrexDmRef**:
	+ `dmRef` elements:
		- `dmCode` attributes:
			- `modelIdentCode`: S1000DBIKE
			- `systemDiffCode`: AAA
			- `systemCode`: D00
			- `subSystemCode`: 0
			- `subSubSystemCode`: 0
			- `assyCode`: 00
			- `disassyCode`: 00
			- `disassyCodeVariant`: AA
			- `infoCode`: 022
			- `infoCodeVariant`: A
			- `itemLocationCode`: D
		- `issueInfo` attributes:
			- `issueNumber`: 011
			- `inWork`: 00
* **Quality Assurance**:
	+ `firstVerification` attribute: `verificationType` = tabtop
* **System Breakdown Code**: DA210
* **Reason for Update**:
	+ `id`: rfu_general
	+ `updateReasonType`: urt03
	+ Description: S1000D upissued

### Content
The following section provides the content of the data module.

#### Learning
The learning section contains a single learning assessment.

##### Learning Assessment
* **Title**: Knowledge Check
* **LC Interaction**:
	+ **LC Single Select**:
		- **LC Question**:
			- Description: Select your answer, and then click CHECK.
				The stem attaches the _________________________ to the ________________________.
		- **LC Answer Option Group**:
			1. `id`: ao_001
				* `shuffle`: 1
				* Description: headset / fork
			2. `id`: ao_002
				* `shuffle`: 1
				* Description: fork / handlebar
			3. `id`: ao_003
				* `shuffle`: 1
				* Description: handlebar / headset
				* `lcCorrectResponse` attribute: lcName = lcCorrectResponse
			4. `id`: ao_004
				* `shuffle`: 1
				* Description: frame / handlebar
		- **LC Feedback Item Group**:
			1. `attemptMatch`: 1
				* Description: The answer "headset / fork" is incorrect. Try again!
				* `internalRef` attribute: internalRefId = ao_001
			2. `attemptMatch`: 1
				* Description: The answer "fork / handlebar" is incorrect. Try again! 
				* `internalRef` attribute: internalRefId = ao_002
			3. 
				* Description: Correct! 
				* `internalRef` attribute: internalRefId = ao_003
			4. `attemptMatch`: 1
				* Description: The answer "frame / handlebar" is incorrect. Try again! 
				* `internalRef` attribute: internalRefId = ao_004
			5. `attemptMatch`: 2
				* Description: The answer "headset / fork" is incorrect. The correct answer is handlebar / headset. 
				* `internalRef` attribute: internalRefId = ao_001
			6. `attemptMatch`: 2
				* Description: The answer "fork / handlebar" is incorrect. The correct answer is handlebar / headset. 
				* `internalRef` attribute: internalRefId = ao_002
			7. `attemptMatch`: 2
				* Description: The answer "frame / handlebar" is incorrect. The correct answer is handlebar / headset. 
				* `internalRef` attribute: internalRefId = ao_004