# DMC-S1000DBIKE-AAA-DA1-00-00-00AA-341A-A_010-00_EN-US_1_1

This document represents the content of the XML file `DMC-S1000DBIKE-AAA-DA1-00-00-00AA-341A-A_010-00_EN-US_1_1`.

## 1. dmIdent

This section defines the data module identification.

*   **modelIdentCode**: `S1000DBIKE`
*   **systemDiffCode**: `AAA`
*   **systemCode**: `DA1`
*   **subSystemCode**: `0`
*   **subSubSystemCode**: `0`
*   **assyCode**: `00`
*   **disassyCode**: `00`
*   **disassyCodeVariant**: `AA`
*   **infoCode**: `341`
*   **infoCodeVariant**: `A`
*   **itemLocationCode**: `A`
*   **language**:
    *   **countryIsoCode**: `US`
    *   **languageIsoCode**: `en`

## 2. dmAddress

This section provides addressing information for the data module.

### 2.1 dmIdent

*   **modelIdentCode**: `S1000DBIKE`
*   **systemDiffCode**: `AAA`
*   **systemCode**: `DA1`
*   **subSystemCode**: `0`
*   **subSubSystemCode**: `0`
*   **assyCode**: `00`
*   **disassyCode**: `00`
*   **disassyCodeVariant**: `AA`
*   **infoCode**: `341`
*   **infoCodeVariant**: `A`
*   **itemLocationCode**: `A`

### 2.2 dmAddressItems

*   **issueDate**:
    *   **year**: `2024`
    *   **month**: `06`
    *   **day**: `19`
*   **techName**: `Brake system`
*   **infoName**: `Manual test`

## 3. dmStatus

This section details the status of the data module.

*   **issueType**: `deleted`

### 3.1 Security

*   **securityClassification**: `01`
*   **commercialClassification**: `cc51`
*   **caveat**: `cv51`

### 3.2 dataRestrictions

#### 3.2.1 restrictionInstructions

*   **dataDistribution**: `To be made available to all S1000D users.`

*   **exportControl**:
    *   **exportRegistrationStmt**: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`

*   **dataHandling**: `There are no specific handling instructions for this data module.`

*   **dataDestruction**: `Users may destroy this data module in accordance with their own local procedures.`

*   **dataDisclosure**: `There are no dissemination limitations that apply to this data module.`

#### 3.2.2 restrictionInfo

*   **copyright**:
    *   **copyrightText**: `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
    *   **publishers**:
        *   `Aerospace, Security and Defence Industries Association of Europe`
        *   `Aerospace Industries Association of America`
        *   `ATA e-Business Program`
    *   **limitationsOfLiability**:
        *   `This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.`
        *   `Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.`
        *   `Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.`
    *   **copyrightDetails**: `The details for copyright can be found in the S1000D Specification.`

*   **policyStatement**: `S1000D-SC-2016-017-002-00 Steering Committee TOR`
*   **dataConds**: `There are no known conditions that would change the data restrictions for, or security classification of, this data module.`

## 4. responsiblePartnerCompany

*   **enterpriseCode**: `B6865`
*   **enterpriseName**: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`

## 5. originator

*   **enterpriseCode**: `B6865`
*   **enterpriseName**: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`

## 6. applicCrossReferenceTableRef

### 6.1 dmRefIdent

#### 6.1.1 dmCode

*   **modelIdentCode**: `S1000DBIKE`
*   **systemDiffCode**: `AAA`
*   **systemCode**: `D00`
*   **subSystemCode**: `0`
*   **subSubSystemCode**: `0`
*   **assyCode**: `00`
*   **disassyCode**: `00`
*   **disassyCodeVariant**: `AA`
*   **infoCode**: `00W`
*   **infoCodeVariant**: `A`
*   **itemLocationCode**: `D`

## 7. applic

*   **displayText**: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)`

*   **evaluate**:

    *   **andOr**: `and`
    *   **assert**:
        *   **applicPropertyIdent**: `type`
        *   **applicPropertyType**: `prodattr`
        *   **applicPropertyValues**: `Mountain bicycle`
    *   **evaluate**:
        *   **andOr**: `or`
        *   **evaluate**:
            *   **andOr**: `and`
            *   **assert**:
                *   **applicPropertyIdent**: `model`
                *   **applicPropertyType**: `prodattr`
                *   **applicPropertyValues**: `Mountain storm`
            *   **assert**:
                *   **applicPropertyIdent**: `version`
                *   **applicPropertyType**: `prodattr`
                *   **applicPropertyValues**: `Mk1``
        *   **evaluate**:
            *   **andOr**: `and`
            *   **assert**:
                *   **applicPropertyIdent**: `model`
                *   **applicPropertyType**: `prodattr`
                *   **applicPropertyValues**: `Mk9`
            *   **assert**:
                *   **applicPropertyIdent**: `version`
                *   **applicPropertyType**: `prodattr`
                *   **applicPropertyValues**: `Brook trekker`

## 8. techStandard

*   **authorityInfoAndTp**:
    *   **authorityInfo**: `20010131`
    *   **techPubBase**: `Bike book`
*   **authorityExceptions**: (empty)
*   **authorityNotes**: (empty)

## 9. brexDMRef

### 9.1 dmRefIdent

#### 9.1.1 dmCode

*   **modelIdentCode**: `S1000DBIKE`
*   **systemDiffCode**: `AAA`
*   **systemCode**: `D00`
*   **subSystemCode**: `0`
*   **subSubSystemCode**: `0`
*   **assyCode**: `00`
*   **disassyCode**: `00`
*   **disassyCodeVariant**: `AA`
*   **infoCode**: `00W`
*   **infoCodeVariant**: `A`
*   **itemLocationCode**: `D`

## 10. procedure

### 10.1 taskSequence

*   **task**:
    *   **taskDescription**: `Put the bicycle on a flat surface.`
*   **task**:
    *   **taskDescription**: `Put the bicycle on a flat surface.`
*   **task**:
    *   **taskDescription**: `Put the bicycle on a flat surface.`

### 10.2 step

*   **stepNumber**: `1`
*   **stepDescription**: `Put the bicycle on a flat surface.`

## 11. closeRequirements

(empty)