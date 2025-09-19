# DMC-S1000DBIKE-AAA-DA3-10-00-00AA-411A-A_010-00_EN-US_1_1

This document represents a data module (DM) as defined by the S1000D standard.

## DM Ident

### DM Address

*   **modelIdentCode**: S1000DBIKE
*   **systemDiffCode**: AAA
*   **systemCode**: DA3
*   **subSystemCode**: 1
*   **subSubSystemCode**: 0
*   **assyCode**: 00
*   **disassyCode**: 00
*   **disassyCodeVariant**: AA
*   **infoCode**: 411
*   **infoCodeVariant**: A
*   **itemLocationCode**: A
*   **language**: US, en

#### DM Address Items

*   **issueDate**: 2024-06-19
*   **techName**: Horn
*   **infoName**: Isolated fault

### DM Status

*   **issueType**: changed

#### Security

*   **securityClassification**: 01
*   **commercialClassification**: cc51
*   **caveat**: cv51

#### Data Restrictions

##### Restriction Instructions

*   **dataDistribution**: To be made available to all S1000D users.
*   **exportControl**:
    *   **exportRegistrationStmt**: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
*   **dataHandling**: There are no specific handling instructions for this data module.
*   **dataDestruction**: Users may destroy this data module in accordance with their own local procedures.
*   **dataDisclosure**: There are no dissemination limitations that apply to this data module.

##### Restriction Info

*   **copyright**:
    *   **copyrightText**: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
    *   **publishers**:
        *   Aerospace, Security and Defence Industries Association of Europe
        *   Aerospace Industries Association of America
        *   ATA e-Business Program
    *   **limitationsOfLiability**:
        *   This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
        *   Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
        *   Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
    *   **copyrightDetails**: The details for copyright can be found in the S1000D Specification.
*   **policyStatement**: S1000D-SC-2016-017-002-00 Steering Committee TOR
*   **dataConds**: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company

*   **enterpriseCode**: B6865
*   **enterpriseName**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Originator

*   **enterpriseCode**: B6865
*   **enterpriseName**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Applic Cross Reference Table Ref

*   **dmCode**:
    *   **modelIdentCode**: S1000DBIKE
    *   **systemDiffCode**: AAA
    *   **systemCode**: D00
    *   **subSystemCode**: 0
    *   **subSubSystemCode**: 0
    *   **assyCode**: 00
    *   **disassyCode**: 00
    *   **disassyCodeVariant**: AA
    *   **infoCode**: 00W
    *   **infoCodeVariant**: A
    *   **itemLocationCode**: D

#### Applic

*   **displayText**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **evaluate**:
    *   **and**:
        *   **assert**:
            *   **applicPropertyIdent**: type
            *   **applicPropertyType**: prodattr
            *   **applicPropertyValues**: Mountain bicycle
    *   **evaluate**:
        *   **or**:
            *   **evaluate**:
                *   **and**:
                    *   **assert**:
                        *   **applicPropertyIdent**: model
                        *   **applicPropertyType**: prodattr
                        *   **applicPropertyValues**: Mountain storm
                    *   **assert**:
                        *   **applicPropertyIdent**: version
                        *   **applicPropertyType**: prodattr
                        *   **applicPropertyValues**: Mk1
            *   **evaluate**:
                *   **and**:
                    *   **assert**:
                        *   **applicPropertyIdent**: model
                        *   **applicPropertyType**: prodattr
                        *   **applicPropertyValues**: Brook trekker
                    *   **assert**:
                        *   **applicPropertyIdent**: version
                        *   **applicPropertyType**: prodattr
                        *   **applicPropertyValues**: Mk9

#### Tech Standard

*   **authorityInfoAndTp**:
    *   **authorityInfo**: 20010131
    *   **techPubBase**: Bike book
*   **authorityExceptions**:
*   **authorityNotes**:

#### Brex DM Ref

*   **dmCode**:
    *   **modelIdentCode**: S1000DBIKE
    *   **systemDiffCode**: AAA
    *   **systemCode**: D00
    *   **subSystemCode**: 0
    *   **subSubSystemCode**: 0
    *   **assyCode**: 00
    *   **disassyCode**: 00
    *   **disassyCodeVariant**: AA
    *   **infoCode**: 921
    *   **infoCodeVariant**: A
    *   **itemLocationCode**: A

## Content

### Fault Diagnosis

*   **faultDescription**: Horn not working
*   **cause**: Possible short circuit or open circuit in the horn wiring
*   **remedy**: Check the horn wiring for continuity and shorts. Replace the horn if necessary.