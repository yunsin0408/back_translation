# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-362B-A_010-00_EN-US_1_1_regenerated_2_regenerated_3_regenerated_4_regenerated

## dmIdent

*   **modelIdentCode**: S1000DBIKE
*   **systemDiffCode**: AAA
*   **systemCode**: DA0
*   **subSystemCode**: 1
*   **subSubSystemCode**: 0
*   **assyCode**: 20
*   **disassyCode**: 00
*   **disassyCodeVariant**: AA
*   **infoCode**: 362
*   **infoCodeVariant**: B
*   **itemLocationCode**: A
*   **language**: en-US

## dmAddressItems

*   **issueDate**: 2024-06-19
*   **techName**: Tire
*   **infoName**: Check pressure
*   **infoNameVariant**: Use pressure gauge

## dmStatus

*   **issueType**: changed

## Security

*   **securityClassification**: 01
*   **commercialClassification**: cc51
*   **caveat**: cv51

## Data Restrictions

### restrictionInstructions

*   **dataDistribution**: To be made available to all S1000D users.
*   **exportControl**:
    *   **exportRegistrationStmt**: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
*   **dataHandling**: There are no specific handling instructions for this data module.
*   **dataDestruction**: Users may destroy this data module in accordance with their own local procedures.
*   **dataDisclosure**: There are no dissemination limitations that apply to this data module.

### restrictionInfo

*   **copyright**:
    *   **text**: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
    *   **publishers**:
        *   Aerospace, Security and Defence Industries Association of Europe
        *   Aerospace Industries Association of America
        *   ATA e-Business Program
    *   **limitationsOfLiability**:
        *   **limitation**: This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
        *   **limitation**: Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
        *   **limitation**: Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
    *   **text**: The details for copyright can be found in the S1000D Specification.
*   **policyStatement**: S1000D upissued

## Content

### Refs

*   **dmRef 1**:
    *   **modelIdentCode**: S1000DBIKE
    *   **systemDiffCode**: AAA
    *   **systemCode**: DA0
    *   **subSystemCode**: 1
    *   **subSubSystemCode**: 0
    *   **assyCode**: 10
    *   **disassyCode**: 00
    *   **disassyCodeVariant**: AA
    *   **infoCode**: 921
    *   **infoCodeVariant**: A
    *   **itemLocationCode**: A
*   **dmRef 2**:
    *   **modelIdentCode**: S1000DBIKE
    *   **systemDiffCode**: AAA
    *   **systemCode**: DA0
    *   **subSystemCode**: 1
    *   **subSubSystemCode**: 0
    *   **assyCode**: 20
    *   **disassyCode**: 00
    *   **disassyCodeVariant**: AA
    *   **infoCode**: 215
    *   **infoCodeVariant**: A
    *   **itemLocationCode**: A

### Procedure

#### preliminaryRequirements

*   **reqPersons**:
    *   **person**:
        *   **personCategory**: Basic user
        *   **trade**: Operator
        *   **estimatedTime**: 0.3 h
*   **reqSupportEquips**:
    *   **supportEquipDescr**:
        *   **name**: Tire pressure gauge
        *   **identNumber**:
            *   **manufacturerCode**: KZ666
            *   **partAndSerialNumber**:
                *   **partNumber**: BSK-TLST-001-01
        *   **reqQuantity**: 1 EA

#### mainProcedure

*   Locate the valve stem of tire.
*   Use the tire pressure gauge to check the tire pressure.
*   Tire pressure should between 2000 hPa to 2700 hPa.

*   **Conditional 1**:
    *   **condition**: If tire pressure is less than 2000 hPa inflate tire.
    *   **dmRef**:
        *   **modelIdentCode**: S1000DBIKE
        *   **systemDiffCode**: AAA
        *   **systemCode**: DA0
        *   **subSystemCode**: 1
        *   **subSubSystemCode**: 0
        *   **assyCode**: 20
        *   **disassyCode**: 00
        *   **disassyCodeVariant**: AA
        *   **infoCode**: 215
        *   **infoCodeVariant**: A
        *   **itemLocationCode**: A
*   **Conditional 2**:
    *   **condition**: If the tire cannot maintain pressure or the tire pressure is greater than 2700 hPa replace the inner tube.
    *   **dmRef**:
        *   **modelIdentCode**: S1000DBIKE
        *   **systemDiffCode**: AAA
        *   **systemCode**: DA0
        *   **subSystemCode**: 1
        *   **subSubSystemCode**: 0
        *   **assyCode**: 10
        *   **disassyCode**: 00
        *   **disassyCodeVariant**: AA
        *   **infoCode**: 921
        *   **infoCodeVariant**: A
        *   **itemLocationCode**: A

#### closeRequirements

*   **requirement**: No close requirements.