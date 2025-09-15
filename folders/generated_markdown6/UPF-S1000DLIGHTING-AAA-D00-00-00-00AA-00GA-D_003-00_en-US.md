UPF-S1000DLIGHTING-AAA-D00-00-00-00AA-00GA-D_003-00_en-US
==============================================

## Update Ident and Status Section
### Update Address
#### Update Ident
* **Update Code**
	+ objectIdentCode: UPF
	+ modelIdentCode: S1000DLIGHTING
	+ systemDiffCode: AAA
	+ systemCode: D00
	+ subSystemCode: 0
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 00G
	+ infoCodeVariant: A
	+ itemLocationCode: D
* **Language**
	+ languageIsoCode: en
	+ countryIsoCode: US
* **Issue Info**
	+ issueNumber: 003
	+ inWork: 00

#### Issue Date
* year: 2024
* month: 06
* day: 19

### Update Status
#### Source DM Ident
* **DM Code**
	+ modelIdentCode: S1000DLIGHTING
	+ systemDiffCode: AAA
	+ systemCode: D00
	+ subSystemCode: 0
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 00G
	+ infoCodeVariant: A
	+ itemLocationCode: D
* **Language**
	+ languageIsoCode: en
	+ countryIsoCode: US
* **Issue Info**
	+ issueNumber: 003
	+ inWork: 00

#### Target DM Issue Info
* issueNumber: 003
* inWork: 03

#### Responsible Partner Company
* enterpriseCode: B6865
* enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Originator
* enterpriseCode: B6865
* enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### BrexDm Ref
```markdown
* DM Code:
	+ modelIdentCode: S1000DBIKE
	+ systemDiffCode: AAA
	+ systemCode: D00
	+ subSystemCode: 0
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 022
	+ infoCodeVariant: A
	+ itemLocationCode: D
```

#### Quality Assurance
* verificationType: tabtop

## Target DM Status
### Issue Type
* issueType: changed

### Security
* securityClassification: 01
* commercialClassification: cc51
* caveat: cv51

### Data Restrictions
#### Restriction Instructions
* **Data Distribution**: To be made available to all S1000D users.
* **Export Control**:
	+ Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
* **Data Handling**: There are no specific handling instructions for this data module.
* **Data Destruction**: Users may destroy this data module in accordance with their own local procedures.
* **Data Disclosure**: There are no dissemination limitations that apply to this data module.

#### Restriction Info
##### Copyright
* (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
* Publishers:
	1. Aerospace, Security and Defence Industries Association of Europe
	2. Aerospace Industries Association of America
	3. ATA e-Business Program
* Limitations of liability:
	1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
	2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
	3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* The details for copyright can be found in the S1000D Specification.

##### Policy Statement
* S1000D-SC-2016-017-002-00 Steering Committee TOR

##### Data Conds
* There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Responsible Partner Company
* enterpriseCode: B6865
* enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Originator
* enterpriseCode: B6865
* enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Applic Cross Ref Table Ref
```markdown
* DM Code:
	+ modelIdentCode: S1000DBIKE
	+ systemDiffCode: AAA
	+ systemCode: D00
	+ subSystemCode: 0
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 022
	+ infoCodeVariant: A
	+ itemLocationCode: D
```

### Tech Standard
* authorityInfoAndTp:
	+ authorityInfo: 
		- techBase: 
	+ baseDoc: 
* authorityExceptions: None
* authorityNotes: None

### BrexDm Ref
```markdown
* DM Code:
	+ modelIdentCode: S1000DBIKE
	+ systemDiffCode: AAA
	+ systemCode: D00
	+ subSystemCode: 0
	+ subSubSystemCode: 0
	+ assyCode: 00
	+ disassyCode: 00
	+ disassyCodeVariant: AA
	+ infoCode: 022
	+ infoCodeVariant: A
	+ itemLocationCode: D
```

### Quality Assurance
* verificationType: tabtop

### Reason For Update
1. **rfu_general**
	* updateReasonType: urt03
	* reason: S1000D upissued
2. **rfu-0001**
	* updateHighlight: 1
	* updateReasonType: urt01
	* reason: The description for part has been modified
3. **rfu-0002**
	* updateHighlight: 1
	* updateReasonType: urt01
	* reason: The part LRU1027 added to the repository.
4. **rfu-0003**
	* updateHighlight: 1
	* updateReasonType: urt01
	* reason: The part LRU1010 deleted from the repository.

## Content
### Update
#### Insert Object Group
* insertionOrder: before
* targetPath: //partSpec[@id=part-0008]
* **Part Spec**
	+ id: part-0007
	+ **Part Ident**
		- partNumberValue: LRU1027
		- manufacturerCodeValue: KZ777
		- id: ID00026
	+ **Item Ident Data**
		- descrForPart: Light, sub-assembly front
	+ **Procurement Data**
		- enterpriseRef:
			- enterpriseRefType: manufacturer
			- manufacturerCodeValue: F0001
	+ **Tech Data**
		- partUsage: pu23
		- specialStorage: 1

#### Delete Object Group
* **Part Ident**
	+ partNumberValue: LRU1010
	+ manufacturerCodeValue: KZ777
	+ id: ID00007

#### Replace Object Group
1. **Replace Object**
	* **Part Spec**
		+ id: part-0010
		+ **Part Ident**
			- partNumberValue: LRU1020
			- manufacturerCodeValue: KZ777
			- id: ID00014
		+ **Item Ident Data**
			- descrForPart: This is a reflector part
		+ **Procurement Data**
			- enterpriseRef:
				- enterpriseRefType: manufacturer
				- manufacturerCodeValue: F0001
		+ **Tech Data**
			- partUsage: pu23
			- specialStorage: 0

2. **Replace Object**
	* **Part Spec**
		+ id: part-0011
		+ **Part Ident**
			- partNumberValue: LIRUS-L1-11
			- manufacturerCodeValue: KZ777
			- id: ID00015
		+ **Item Ident Data**
			- descrForPart: This is a bulb part
		+ **Procurement Data**
			- enterpriseRef:
				- enterpriseRefType: manufacturer
				- manufacturerCodeValue: F0001
		+ **Tech Data**
			- partUsage: pu23
			- specialStorage: 1