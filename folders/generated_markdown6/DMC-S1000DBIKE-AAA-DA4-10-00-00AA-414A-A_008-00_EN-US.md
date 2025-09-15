# DMC-S1000DBIKE-AAA-DA4-10-00-00AA-414A-A_008-00_EN-US
## Introduction
The following document is based on the XML file `DMC-S1000DBIKE-AAA-DA4-10-00-00AA-414A-A_008-00_EN-US.XML`. This markdown representation preserves the original structure and content of the XML document.

## Ident and Status Section
### DM Address
#### DM Ident
The DM ident section contains the following attributes:
* `modelIdentCode`: S1000DBIKE
* `systemDiffCode`: AAA
* `systemCode`: DA4
* `subSystemCode`: 1
* `subSubSystemCode`: 0
* `assyCode`: 00
* `disassyCode`: 00
* `disassyCodeVariant`: AA
* `infoCode`: 414
* `infoCodeVariant`: A
* `itemLocationCode`: A

The language and country codes are:
* `countryIsoCode`: US
* `languageIsoCode`: en

Issue information:
* `issueNumber`: 008
* `inWork`: 00

#### DM Address Items
Issue date: 
* `year`: 2024
* `month`: 06
* `day`: 19

DM title:
* `techName`: Drive train
* `infoName`: Correlated fault

### DM Status
The issue type is: changed

#### Security
Security attributes:
* `securityClassification`: 01
* `commercialClassification`: cc51
* `caveat`: cv51

#### Data Restrictions
##### Restriction Instructions
Data distribution: To be made available to all S1000D users.

Export control:
```markdown
Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted.
Storage of this data module is to be at the discretion of the organization.
```
Data handling: There are no specific handling instructions for this data module.

Data destruction: Users may destroy this data module in accordance with their own local procedures.

Data disclosure: There are no dissemination limitations that apply to this data module.

##### Restriction Info
Copyright information:
```markdown
Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
Publishers:
  * Aerospace, Security and Defence Industries Association of Europe
  * Aerospace Industries Association of America
  * ATA e-Business Program
Limitations of liability:
  * This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
  * Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
  * Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
```
The details for copyright can be found in the S1000D Specification.

Policy statement: S1000D-SC-2016-017-002-00 Steering Committee TOR

Data conditions: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company
* `enterpriseCode`: B6865
* `enterpriseName`: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Originator
* `enterpriseCode`: B6865
* `enterpriseName`: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Applic Cross Ref Table Ref
DM reference:
```markdown
modelIdentCode: S1000DBIKE
systemDiffCode: AAA
systemCode: D00
subSystemCode: 0
subSubSystemCode: 0
assyCode: 00
disassyCode: 00
disassyCodeVariant: AA
infoCode: 00W
infoCodeVariant: A
itemLocationCode: D
```

#### Applic
Display text:
```markdown
Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
```
Evaluation:
* `andOr`: and
* `applicPropertyIdent`: type
* `applicPropertyType`: prodattr
* `applicPropertyValues`: Mountain bicycle

Nested evaluation:
* `andOr`: or
* Nested evaluations:
  + `andOr`: and
    - `applicPropertyIdent`: model
    - `applicPropertyType`: prodattr
    - `applicPropertyValues`: Mountain storm
    - `applicPropertyIdent`: version
    - `applicPropertyType`: prodattr
    - `applicPropertyValues`: Mk1
  + `andOr`: and
    - `applicPropertyIdent`: model
    - `applicPropertyType`: prodattr
    - `applicPropertyValues`: Brook trekker
    - `applicPropertyIdent`: version
    - `applicPropertyType`: prodattr
    - `applicPropertyValues`: Mk9

#### Tech Standard
Authority info and TP:
* `authorityInfo`: 20010131
* `techPubBase`: Bike book

Authority exceptions: None

Authority notes: None

#### Brex DM Ref
DM reference:
```markdown
modelIdentCode: S1000DBIKE
systemDiffCode: AAA
systemCode: D00
subSystemCode: 0
subSubSystemCode: 0
assyCode: 00
disassyCode: 00
disassyCodeVariant: AA
infoCode: 022
infoCodeVariant: A
itemLocationCode: D
```

#### Quality Assurance
First verification:
* `verificationType`: tabtop

#### System Breakdown Code
* `systemBreakdownCode`: BY151

#### Skill Level
* `skillLevelCode`: sk01

#### Reason for Update
Reason for update:
* `id`: rfu_general
* `updateReasonType`: urt03
```markdown
S1000D upissued
```

## Content
### Fault Reporting
#### Correlated Fault
Correlated fault ID: cflt-0001

##### Basic Correlated Faults
Bit messages:
* Fault code: 100FC01
  - Description: The pedal mechanism is jammed
* Fault code: 200FC01
  - Description: The derailleur is jammed

##### Isolate Detected Fault
LRU item:
* LRU name: Bicycle chain
* Ident number:
  + Manufacturer code: KZ120
  + Part and serial number:
    - Part number: Tchain-120

##### Remarks
```markdown
Prepare the derailleur to put transmission chain back on pedal mechanism.
```
This markdown document represents the structure and content of the original XML file, following the guidelines for conversion.