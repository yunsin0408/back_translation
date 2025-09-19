# DMC-S1000DLIGHTING - Wiring Loom List (AAA-D00-00-00-00AA-058A-A_011-00_EN-US_1_1)

This document represents the wiring loom list as defined by the provided XML data.

## 1. Identification and Status Section

### 1.1 DM Address

#### 1.1.1 DM Ident

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

#### 1.1.2 Language

*   **countryIsoCode:** US
*   **languageIsoCode:** en

#### 1.1.3 Issue Info

*   **issueNumber:** 011
*   **inWork:** 00

#### 1.1.4 DM Address Items

*   **issueDate:**
    *   **year:** 2024
    *   **month:** 06
    *   **day:** 19
*   **DM Title:**
    *   **techName:** Wiring
    *   **infoName:** Loom list

### 1.2 DM Status

*   **issueType:** changed
*   **Security:**
    *   **securityClassification:** 01
    *   **commercialClassification:** cc51
    *   **caveat:** cv51
*   **Data Restrictions:**
    *   **Restriction Instructions:**
        *   **dataDistribution:** To be made available to all S1000D users.
        *   **exportControl:**
            *   **exportRegistrationStmt:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   **dataHandling:** There are no specific handling instructions for this data module.
        *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
        *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
    *   **Restriction Info:**
        *   **copyright:**
            *Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD*
            *Publishers:*
                * Aerospace, Security and Defence Industries Association of Europe
                * Aerospace Industries Association of America
                * ATA e-Business Program
            *Limitations of liability:*
                * This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                * Neither ASD nor any person who has contributed to the creation, revision or maintenance of the material shall be liable for any damages arising from the use of this material.
        *   **applicability:** Not present in the source document.
*   **responsiblePartnerCompany:** Not present in the source document.

## 2. Content

### 2.1 Referenced Applic Group Ref

*   **applicRef:**
    *   **applicIdentValue:** app-00000000AA058A-0001
    *   **id:** app-0001

### 2.2 Wiring Data

#### 2.2.1 Harness Group

##### 2.2.1.1 Harness 1: Batt_01

*   **harnessIdent:** Batt_01
*   **harnessInfo:**
    *   **partNumber:** Battery_123
    *   **harnessVariantIdent:** 123
    *   **harnessVariantIssue:** A
    *   **harnessName:** Battery harness
    *   **emcCode:** LS1
    *   **temperature:**
        *   **maxTemperature:** 500
        *   **maxTemperatureUnit:** degF
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

##### 2.2.1.2 Harness 2: Tacho

*   **harnessIdent:** Tacho
*   **harnessInfo:**
    *   **partNumber:** Tachometer_101
    *   **harnessVariantIdent:** 101
    *   **harnessVariantIssue:** A
    *   **harnessName:** Tachometer harness
    *   **emcCode:** LS2
    *   **temperature:**
        *   **minTemperature:** -10
        *   **minTemperatureUnit:** degC
        *   **maxTemperature:** 60
        *   **maxTemperatureUnit:** degC
    *   **harnessEnvironment:**
        *   **highVibrationFlag:** 1
    *   **sleeveGroup:**
        *   **sleeve:**
            *   **sleeveMaterial:** Silicon
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** U8025
    *   **enterpriseName:** UK MoD

##### 2.2.1.3 Harness 3: Lamp1

*   **harnessIdent:** Lamp1
*   **harnessInfo:**
    *   **partNumber:** Front light_501
    *   **harnessVariantIdent:** 501
    *   **harnessVariantIssue:** A
    *   **harnessName:** Front light harness
    *   **emcCode:** LS3
    *   **temperature:**
        *   **minTemperature:** -10
        *   **minTemperatureUnit:** degC
    *   **harnessEnvironment:**
        *   **highVibrationFlag:** 1
        *   **hydraulicFlag:** 1
    *   **sleeveGroup:**
        *   **sleeve:**
            *   **sleeveMaterial:** Teflon
            *   **partNumber:** SLV-5678
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** U8025
    *   **enterpriseName:** UK MoD

#### 2.2.2 Harness: Routing

*   **routing:**
    *   **clippingPoint:** 271-11
    *   **clippingPoint:** 273-2
*   **responsiblePartnerCompany:**
    *   **enterpriseCode:** K0378

---