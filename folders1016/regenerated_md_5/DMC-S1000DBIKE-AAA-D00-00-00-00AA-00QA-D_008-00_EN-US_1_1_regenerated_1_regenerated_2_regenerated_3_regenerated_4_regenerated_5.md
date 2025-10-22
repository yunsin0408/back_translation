# DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated_3_regenerated_4_regenerated

## dm

*   **ident:** DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated_3_regenerated_4_regenerated

## dmAddressItems

*   **dmIdent:** DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US_1_1_regenerated_1_regenerated

### dmAddress

*   **dmIdent:**
    *   **modelIdentCode:** S1000DBIKE
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 00
    *   **disassyCodeVariant:** AA
    *   **infoCode:** 00Q
    *   **infoCodeVariant:** A
    *   **itemLocationCode:** D
*   **language:**
    *   **countryIsoCode:** US
    *   **languageIsoCode:** en
*   **issueInfo:**
    *   **issueNumber:** 008
    *   **inWork:** 00
*   **issueDate:**
    *   **year:** 2024
    *   **month:** 06
    *   **day:** 19
*   **dmTitle:**
    *   **techName:** Mountain bicycle
    *   **infoName:** Conditions cross-reference table

## dmStatus

*   **issueType:** changed
*   **security:**
    *   **securityClassification:** 01
    *   **dataRestrictions:**
        *   **restrictionInstructions:**
            *   **dataDistribution:** To be made available to all S1000D users.
            *   **exportControl:**
                *   **exportRegistrationStmt:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
                *   **dataHandling:** There are no specific handling instructions for this data module.
                *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
                *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
        *   **restrictionInfo:**
            *   **copyright:** Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   **publishers:**
                *   publisher: Aerospace, Security and Defence Industries Association of Europe
                *   publisher: Aerospace Industries Association of America
                *   publisher: ATA e-Business Program
            *   **limitationsOfLiability:**
                *   limitation: This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                *   limitation: Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability.
*   **responsibleDepartment:** Engineering

## dependencies

*   **forCondValues:** POST-001
*   **dependencyTest:** A-1

## content

### referencedApplicGroup

*   **applicA_1:**
    *   **assert:**
        *   **applicPropertyType:** condition
        *   **applicPropertyIdent:** SB-S001
        *   **applicPropertyValues:** POST-001~POST-999
*   **applicA_2:**
    *   **evaluate:**
        *   **andOr:** and
    *   **assert1:**
        *   **applicPropertyType:** condition
        *   **applicPropertyIdent:** SB-S001
        *   **applicPropertyValues:** POST-001~POST-999
    *   **assert2:**
        *   **applicPropertyType:** condition
        *   **applicPropertyIdent:** SB-S009
        *   **applicPropertyValues:** PRE

### condCrossReferenceTable

*   **condTypeList:**
    *   **condTypeSB:**
        *   **id:** SB
        *   **valueDataType:** string
        *   **name:** Service bulletin
        *   **descr:** Generic service bulletin type
        *   **enumeration:** PRE
    *   **condTypeBoolean:**
        *   **id:** Boolean
        *   **name:** generic Boolean condition
        *   **descr:** Boolean condition
        *   **enumeration:** True|False
*   **condList:**
    *   **condSB_S001:**
        *   **condTypeRefId:** SB
        *   **id:** SB-S001
        *   **name:** Service bulletin 1
        *   **descr:** Service bulletin description 1
        *   **refs:**
            *   **dmRef:**
                *   **dmIdent:**
                    *   **modelIdentCode:** S1000DBIKE
                    *   **systemDiffCode:** AAA
                    *   **systemCode:** DA0
                    *   **subSystemCode:** 2
                    *   **subSubSystemCode:** 0
                    *   **assyCode:** 00
                    *   **disassyCode:** 00
                    *   **disassyCodeVariant:** AA
                    *   **infoCode:** 520
                    *   **infoCodeVariant:** A
                    *   **itemLocationCode:** A
    *   **condSB_S009:**
        *   **condTypeRefId:** SB
        *   **id:** SB-S009
        *   **name:** Service bulletin 9
        *   **descr:** Service bulletin description 9
        *   **refs:**
            *   **dmRef:**
                *   **dmIdent:**
                    *   **modelIdentCode:** S1000DBIKE
                    *   **systemDiffCode:** AAA
                    *   **systemCode:** DA0
                    *   **subSystemCode:** 2
                    *   **subSubSystemCode:** 0
                    *   **assyCode:** 00
                    *   **disassyCode:** 00
                    *   **disassyCodeVariant:** AA
                    *   **infoCode:** 520
                    *   **infoCodeVariant:** A
                    *   **itemLocationCode:** A