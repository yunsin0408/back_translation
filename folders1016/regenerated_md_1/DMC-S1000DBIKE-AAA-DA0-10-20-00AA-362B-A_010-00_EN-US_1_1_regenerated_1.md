# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-362B-A_010-00_EN-US_1_1

## dmIdent

*   **modelIdentCode:** S1000DBIKE
*   **systemDiffCode:** AAA
*   **systemCode:** DA0
*   **subSystemCode:** 1
*   **subSubSystemCode:** 0
*   **assyCode:** 20
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 362
*   **infoCodeVariant:** B
*   **itemLocationCode:** A
*   **language:** en-US

## dmAddressItems

*   **issueDate:** 2024-06-19
*   **techName:** Tire
*   **infoName:** Check pressure
*   **infoNameVariant:** Use pressure gauge

## dmStatus

*   **issueType:** changed

### Security

*   **securityClassification:** 01
*   **commercialClassification:** cc51
*   **caveat:** cv51

### Data Restrictions

#### Restriction Instructions

*   **dataDistribution:** To be made available to all S1000D users.
*   **exportControl:**
    *   **exportRegistrationStmt:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
*   **dataHandling:** There are no specific handling instructions for this data module.
*   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
*   **dataDisclosure:** There are no dissemination limitations that apply to this data module.

#### Restriction Info

*   **copyright:**
    *   *Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD
    *   *Publishers:*
        *   Aerospace, Security and Defence Industries Association of Europe
        *   Aerospace Industries Association of America
        *   ATA e-Business Program
    *   *Limitations of liability:*
        *   This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
        *   Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
        *   Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
    *   The details for copyright can be found in the S1000D Specification.
*   **policyStatement:** S1000D upissued

*   **qualityAssurance:** verificationType="tabtop"
*   **systemBreakdownCode:** BY112
*   **skillLevel:** sk01

## Content

### Refs

#### dmRef

*   **modelIdentCode:** S1000DBIKE
*   **systemDiffCode:** AAA
*   **systemCode:** DA0
*   **subSystemCode:** 1
*   **subSubSystemCode:** 0
*   **assyCode:** 10
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 921
*   **infoCodeVariant:** A
*   **itemLocationCode:** A

#### dmRef

*   **modelIdentCode:** S1000DBIKE
*   **systemDiffCode:** AAA
*   **systemCode:** DA0
*   **subSystemCode:** 1
*   **subSubSystemCode:** 0
*   **assyCode:** 20
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 215
*   **infoCodeVariant:** A
*   **itemLocationCode:** A

### Procedure

#### Preliminary Requirements

*   **reqPersons:**
    *   **person:**
        *   **personCategory:** Basic user
        *   **trade:** Operator
        *   **estimatedTime:** 0.3 h
*   **reqSupportEquips:**
    *   **supportEquipDescr:**
        *   **name:** Tire pressure gauge
        *   **identNumber:**
            *   **manufacturerCode:** KZ666
            *   **partAndSerialNumber:**
                *   **partNumber:** BSK-TLST-001-01
        *   **reqQuantity:** 1 EA

#### Main Procedure

*   Locate the valve stem of tire.
*   Use the tire pressure gauge (<internalRef internalRefId="seq-0003" internalRefTargetType="irtt05"/>) to check the tire pressure.
*   Tire pressure should between 2000 hPa to 2700 hPa.

*   **Conditional:**
    *   **condition:** If tire pressure is less than 2000 hPa inflate tire. Refer to <dmRef>
        *   **modelIdentCode:** S1000DBIKE
        *   **systemDiffCode:** AAA
        *   **systemCode:** DA0
        *   **subSystemCode:** 1
        *   **subSubSystemCode:** 0
        *   **assyCode:** 20
        *   **disassyCode:** 00
        *   **disassyCodeVariant:** AA
        *   **infoCode:** 215
        *   **infoCodeVariant:** A
        *   **itemLocationCode:** A
    </dmRef>

*   **Conditional:**
    *   **condition:** If the tire cannot maintain pressure or the tire pressure is greater than 2700 hPa replace the inner tube. Refer to <dmRef>
        *   **modelIdentCode:** S1000DBIKE
        *   **systemDiffCode:** AAA
        *   **systemCode:** DA0
        *   **subSystemCode:** 1
        *   **subSubSystemCode:** 0
        *   **assyCode:** 10
        *   **disassyCode:** 00
        *   **disassyCodeVariant:** AA
        *   **infoCode:** 921
        *   **infoCodeVariant:** A
        *   **itemLocationCode:** A
    </dmRef>

#### Close Requirements

*   No close requirements.