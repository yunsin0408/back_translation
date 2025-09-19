```markdown
# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-058A-A_011-00_EN-US

## Ident and Status Section

### DM Address

#### DM Ident

*   **modelIdentCode:** S1000DLIGHTING
*   **systemDiffCode:** AAA
*   **systemCode:** D00
*   **subSystemCode:** 0
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 058
*   **infoCodeVariant:** A
*   **itemLocationCode:** A

*   **language:**
    *   **countryIsoCode:** US
    *   **languageIsoCode:** en

*   **issueInfo:**
    *   **issueNumber:** 011
    *   **inWork:** 00

#### DM Address Items

*   **issueDate:**
    *   **year:** 2024
    *   **month:** 06
    *   **day:** 19
*   **dmTitle:**
    *   **techName:** Wiring
    *   **infoName:** Loom list

### DM Status

*   **issueType:** changed

#### Security

*   **securityClassification:** 01
*   **commercialClassification:** cc51
*   **caveat:** cv51

#### Data Restrictions

*   **restrictionInstructions:**
    *   **dataDistribution:** To be made available to all S1000D users.
    *   **exportControl:**
        *   **exportRegistrationStmt:**
            *   Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
    *   **dataHandling:** There are no specific handling instructions for this data module.
    *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
    *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
*   **restrictionInfo:**
    *   **copyright:**
        *   *Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD*
        *   *Publishers:*
            *   Aerospace, Security and Defence Industries Association of Europe
            *   Aerospace Industries Association of America
            *   ATA e-Business Program
        *   *Limitations of liability:*
            *   This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
            *   Neither ASD nor any person who has contributed to the creation, revision or maintenance of the material shall be liable for any damages arising from the use of this material.
    *   **applicability:** Not present in the source document.

#### Responsible Partner Company

*   Not present in the source document

## Content

### Referenced Applic Group Ref

*   **applicRef:**
    *   **applicIdentValue:** app-00000000AA058A-0001
    *   **id:** app-0001

### Wiring Data

#### Harness Group

##### Harness 1

*   **applicRefId:** app-0001
*   **harnessIdent:** Batt_01
*   **harnessInfo:**
    *   **partNumber:** Battery_123
    *   **harnessVariantIdent:** 123
    *   **harnessVariantIssue:** A
    *   **harnessName:** Battery harness
    *   **emcCode:** LS1
    *   **temperature:**
        *   **maxTemperature:** 500 (unit: degF)
    *   **harnessEnvironment:**
        *   **highVibrationFlag:** 1
        *   **hydraulicFlag:** 1
    *   **sleeveGroup:**
        *   **sleeve:**
            *   **sleeveMaterial:** Teflon
            *   **partNumber:** SPN1234
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** U8025
    *   **enterpriseName:** UK MoD

##### Harness 2

*   **applicRefId:** app-0001
*   **harnessIdent:** Tacho
*   **harnessInfo:**
    *   **partNumber:** Tachometer_101
    *   **harnessVariantIdent:** 101
    *   **harnessVariantIssue:** A
    *   **harnessName:** Tachometer harness
    *   **emcCode:** LS2
    *   **temperature:**
        *   **minTemperature:** -10 (unit: degC)
        *   **maxTemperature:** 60 (unit: degC)
    *   **harnessEnvironment:**
        *   **highVibrationFlag:** 1
    *   **sleeveGroup:**
        *   **sleeve:**
            *   **sleeveMaterial:** Silicon
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** U8025
    *   **enterpriseName:** UK MoD

##### Harness 3

*   **applicRefId:** app-0001
*   **harnessIdent:** Lamp1
*   **harnessInfo:**
    *   **partNumber:** Front light_501
    *   **harnessVariantIdent:** 501
    *   **harnessVariantIssue:** A
    *   **harnessName:** Front light harness
    *   **emcCode:** LS3
    *   **temperature:**
        *   **minTemperature:** -10 (unit: degC)
    *   **sleeveGroup:**
        *   **sleeve:**
            *   **partNumber:** SPN1234
        *   **sleeve:**
            *   **partNumber:** SPN4321
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** U8025
    *   **enterpriseName:** UK MoD

##### Harness 4

*   **applicRefId:** app-0001
*   **harnessIdent:** Lamp2
*   **harnessInfo:**
    *   **partNumber:** Rear light_503
    *   **harnessVariantIdent:** 503
    *   **harnessVariantIssue:** A
    *   **harnessName:** Rear light harness
    *   **emcCode:** LS3
    *   **harnessEnvironment:**
        *   **hydraulicFlag:** 1
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** U8025
    *   **enterpriseName:** UK MoD

##### Harness Alternatives

*   **harnessAlts:**
    *   **id:** SPEC-0001
    *   **harness:**
        *   **harnessIdent:** 1310VB
        *   **harnessInfo:**
            *   **harnessVariantIdent:** 410
            *   **harnessVariantIssue:** A
            *   **harnessName:** FCS LANE 1 FORWARD EQUIPMENT BAY
            *   **emcCode:** E
            *   **temperature:**
                *   **minTemperature:** -10 (unit: degC)
                *   **maxTemperature:** 60 (unit: degC)
            *   **harnessEnvironment:**
                *   **highVibrationFlag:** 1
                *   **hydraulicFlag:** 0
            *   **sleeveGroup:**
                *   **sleeve:**
                    *   **sleeveMaterial:** Teflon
                    *   **partNumber:** SLV-5678
        *   **routing:**
            *   **clippingPoint:** 271-11
            *   **clippingPoint:** 273-2
        *   **responsiblePartnerCompany:**
            *   **enterpriseCode:** K0378
```