# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-215A-A_010-00_EN-US

## Ident and Status Section

### DM Address

#### DM Ident

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
*   **language countryIsoCode:** US
*   **language languageIsoCode:** en
*   **issueNumber:** 010
*   **inWork:** 00

#### DM Address Items

*   **issueDate year:** 2024
*   **issueDate month:** 06
*   **issueDate day:** 19
*   **techName:** Tire
*   **infoName:** Fill with air

### DM Status

*   **issueType:** changed
*   **security securityClassification:** 01
*   **security commercialClassification:** cc51
*   **security caveat:** cv51

#### Data Restrictions

*   **restrictionInstructions:**
    *   **dataDistribution:** To be made available to all S1000D users.
    *   **exportControl:**
        *   **exportRegistrationStmt:**
            *   `simplePara`: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
    *   **dataHandling:** There are no specific handling instructions for this data module.
    *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
    *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
*   **restrictionInfo:**
    *   **copyright:**
        *   `copyrightPara`: `emphasis`: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
        *   `copyrightPara`: `emphasis`: Publishers:
        *   `randomList listItemPrefix="pf01"`:
            *   `listItem`: Aerospace, Security and Defence Industries Association of Europe
            *   `listItem`: Aerospace Industries Association of America
            *   `listItem`: ATA e-Business Program
        *   `copyrightPara`: `emphasis`: Limitations of liability:
        *   `randomList listItemPrefix="pf02"`:
            *   `listItem`: This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
            *   `listItem`: Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
            *   `listItem`: Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
        *   `copyrightPara`: The details for copyright can be found within.
    *   **policyStatements:**
        *   `noPolicyStatements`

#### Responsible Person

*   **noResponsiblePerson**

#### Applicable Regulations

*   **noApplicableRegulations**

#### Quality Assurance

*   **firstVerification verificationType:** tabtop

#### System Breakdown Code

*   **systemBreakdownCode:** BY112

#### Skill Level

*   **skillLevel skillLevelCode:** sk01

#### Reason For Update

*   **id:** rfu\_general
*   **updateReasonType:** urt03
*   `simplePara`: S1000D upissued

## Content

### References

#### DM Ref

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

### Procedure

#### Preliminary Requirements

*   **reqCondGroup:** noConds
*   **reqPersons:**
    *   **person man:** A
    *   **personCategory personCategoryCode:** Basic user
    *   **trade:** Operator
*   **reqSupportEquips:**
    *   **supportEquipDescrGroup:**
        *   **supportEquipDescr id:** seq-0001
            *   **name:** Specialist toolset
            *   **identNumber:**
                *   **manufacturerCode:** KZ666
                *   **partAndSerialNumber:**
                    *   **partNumber:** BSK-TLST-001
            *   **reqQuantity unitOfMeasure:** EA: 1
        *   **supportEquipDescr id:** seq-0002
            *   **name:** Foot pump
            *   **identNumber:**
                *   **manufacturerCode:** KZ666
                *   **partAndSerialNumber:**
                    *   **partNumber:** BSK-TLST-001-05
            *   **reqQuantity unitOfMeasure:** EA: 1
        *   **supportEquipDescr id:** seq-0003
            *   **name:** Tire pressure gauge
            *   **identNumber:**
                *   **manufacturerCode:** KZ666
                *   **partAndSerialNumber:**
                    *   **partNumber:** BSK-TLST-001-01
            *   **reqQuantity unitOfMeasure:** EA: 1
*   **reqSupplies:** noSupplies
*   **reqSpares:** noSpares
*   **reqSafety:** noSafety

#### Main Procedure

*   Ensure bicycle is on the repair stand.
*   Locate the deflated tire.
*   Attach the outlet valve of the <internalRef internalRefId="seq-0002" internalRefTargetType="irtt05"/>, from the <internalRef internalRefId="seq-0001" internalRefTargetType="irtt05"/>, to the valve of the deflated tire.
*   Inflate the tire.
    *   Operate the foot pump to pump air into the tire.
    *   Check tire pressure. Refer to <dmRef>
        *   <dmRefIdent>
            *   <dmCode modelIdentCode="S1000DBIKE" systemDiffCode="AAA" systemCode="DA0" subSystemCode="1" subSubSystemCode="0" assyCode="20" disassyCode="00" disassyCodeVariant="AA" infoCode="362" infoCodeVariant="B" itemLocationCode="A"/>
        </dmRefIdent>
    </dmRef>

#### Close Requirements

*   **reqCondGroup:** noConds