# DMC-BRAKE-AAA-DA1-10-00-00AA-251A-A_004-00_EN-US

## Ident and Status Section

### DM Address

#### DM Ident

*   **modelIdentCode:** BRAKE
*   **systemDiffCode:** AAA
*   **systemCode:** DA1
*   **subSystemCode:** 1
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 251
*   **infoCodeVariant:** A
*   **itemLocationCode:** A
*   **language:** US, en
*   **issueNumber:** 004
*   **inWork:** 00

#### DM Address Items

*   **issueDate:** 2024-06-19
*   **techName:** Brake pads
*   **infoName:** Clean with rubbing alcohol

### DM Status

*   **issueType:** changed
*   **security:**
    *   **securityClassification:** 01
    *   **commercialClassification:** cc51
    *   **caveat:** cv51
*   **dataRestrictions:**
    *   **restrictionInstructions:**
        *   **dataDistribution:** To be made available to all S1000D users.
        *   **exportControl:**
            *   **exportRegistrationStmt:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   **dataHandling:** There are no specific handling instructions for this data module.
        *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
        *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
    *   **restrictionInfo:**
        *   **copyright:**
            *   Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   **Publishers:**
                *   Aerospace, Security and Defence Industries Association of Europe
                *   Aerospace Industries Association of America
                *   ATA e-Business Program
            *   **Limitations of liability:**
                *   This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                *   Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability.
        *   **systemBreakdownCode:** BY131
*   **skillLevel:** sk01
*   **reasonForUpdate:**
    *   **id:** rfu_general
    *   **updateReasonType:** urt03
    *   **simplePara:** S1000D upissued
*   **reasonForUpdate:**
    *   **id:** rfu_CPF2020-030
    *   **updateHighlight:** 1
    *   **updateReasonType:** urt02
    *   **simplePara:** CPF_2020-030US: Added &lt;hazards&gt; to &lt;supplyDescr&gt;.

## Content

### Refs

*   **dmRefIdent:**
    *   **modelIdentCode:** S1000DBIKE
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 00
    *   **disassyCodeVariant:** AA
    *   **infoCode:** 121
    *   **infoCodeVariant:** A
    *   **itemLocationCode:** A

### Procedure

#### Preliminary Requirements

*   **reqCondGroup:** No conditions.
*   **reqPersons:**
    *   **person:**
        *   **man:** A
        *   **personCategory:** Basic user
        *   **trade:** Operator
        *   **estimatedTime:** 0.3 h
*   **reqSupportEquips:** No support equipments.
*   **reqSupplies:**
    *   **supplyDescrGroup:**
        *   **supplyDescr (id: sup-0001):**
            *   **name:** Rubbing alcohol
            *   **identNumber:**
                *   **manufacturerCode:** KZ222
                *   **partAndSerialNumber:**
                    *   **partNumber:** LL-002
            *   **reqQuantity:** As required
            *   **hazards:**
                *   **symbol:** ICN-B6865-GHS02-001-01
                *   **symbol:** ICN-B6865-GHS07-001-01
                *   **hazardousClass:** hz03
                *   **hazardousClass:** hz07
                *   **safetyInformation:** May form explosive mixtures with air.
                *   **safetyInformation:** Highly flammable liquid and vapor.
                *   **safetyInformation:** Causes serious eye irritation.
                *   **safetyInformation:** May cause drowsiness or dizziness.
        *   **supplyDescr (id: sup-0002):**
            *   **name:** Lint-free cloth
            *   **identNumber:** N/A
            *   **reqQuantity:** As required
*   **reqSpares:** No spares.
*   **reqSafety:** No safety requirements.
#### Main Procedure

*   **proceduralStep:** Do a visual inspection of the brakes as given in the pre-ride checks (refer to dmRef).
*   **proceduralStep:** Clean the brake pads.
    *   **proceduralStep:** Find each of the brake pads.
    *   **proceduralStep:**
        *   **warning:** Hazard
        *   **warningAndCautionPara:** Internal Ref: sup-0001
        *   **para:** Apply a thin layer of the rubbing alcohol (sup-0001) on each of the brake pads using a lint-free cloth (sup-0002).
    *   **proceduralStep:** Rub the surface until you have applied the alcohol to the complete surface of the pad.
    *   **proceduralStep:** Remove the unwanted alcohol.

#### Close Requirements

*   **reqCondGroup:** No conditions.