# DMC-S1000DLIGHTING - Lights - Observed fault

This document represents the data module for observed faults related to lights (DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-413A-A_010-00_EN-US_1_1).

## 1. dmIdent (Data Module Identification)

### 1.1 dmAddress

#### 1.1.1 dmIdent

*   **modelIdentCode:** S1000DLIGHTING
*   **systemDiffCode:** AAA
*   **systemCode:** D00
*   **subSystemCode:** 0
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 413
*   **infoCodeVariant:** A
*   **itemLocationCode:** A

#### 1.1.2 dmAddressItems

*   **issueDate:**
    *   **year:** 2024
    *   **month:** 06
    *   **day:** 19
*   **dmTitle:**
    *   **techName:** Lights
    *   **infoName:** Observed fault

### 1.2 dmStatus

*   **issueType:** changed
*   **security:**
    *   **securityClassification:** 01
    *   **commercialClassification:** cc51
    *   **caveat:** cv51
*   **dataRestrictions:**
    *   **restrictionInstructions:**
        *   **dataDistribution:** To be made available to all S1000D users.
        *   **exportControl:**
            *   **exportRegistrationStmt:**
                *   **simplePara:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   **dataHandling:** There are no specific handling instructions for this data module.
        *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
        *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
    *   **restrictionInfo:**
        *   **copyright:**
            *   **copyrightPara:** *Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   **copyrightPara:** *Publishers*
            *   **random list item:**  (Empty)
        *   **remarks:** random remark
*   **applicability:** random applicability
*   **remarks:** random remark

### 1.3 additionalDmStatusInformation

*   **responsibleParty:** random responsible party
*   **applicability:** random applicability
*   **remarks:** random remark

## 2. Content

### 2.1 references

*   **dmRef (1):**
    *   **modelIdentCode:** S1000DLIGHTING
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 0A5
    *   **disassyCodeVariant:** AA
    *   **infoCode:** A
    *   **itemLocationCode:** A
*   **dmRef (2):**
    *   **modelIdentCode:** S1000DLIGHTING
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 0A4
    *   **disassyCodeVariant:** AA
    *   **infoCode:** A
    *   **itemLocationCode:** A

### 2.2 warningsAndCautionsReferences

*   **warningRef (1):**
    *   **id:** w001
    *   **warningIdentNumber:** warning-001
    *   **dmRef:**
        *   **modelIdentCode:** S1000DLIGHTING
        *   **systemDiffCode:** AAA
        *   **systemCode:** D00
        *   **subSystemCode:** 0
        *   **subSubSystemCode:** 0
        *   **assyCode:** 00
        *   **disassyCode:** 0A4
        *   **disassyCodeVariant:** AA
        *   **infoCode:** A
        *   **itemLocationCode:** A
*   **warningRef (2):**
    *   **id:** w002
    *   **warningIdentNumber:** warning-002
    *   **dmRef:**
        *   **modelIdentCode:** S1000DLIGHTING
        *   **systemDiffCode:** AAA
        *   **systemCode:** D00
        *   **subSystemCode:** 0
        *   **subSubSystemCode:** 0
        *   **assyCode:** 00
        *   **disassyCode:** 0A4
        *   **disassyCodeVariant:** AA
        *   **infoCode:** A
        *   **itemLocationCode:** A
*   **cautionRef (1):**
    *   **id:** c001
    *   **cautionIdentNumber:** caution-001
    *   **dmRef:**
        *   **modelIdentCode:** S1000DLIGHTING
        *   **systemDiffCode:** AAA
        *   **systemCode:** D00
        *   **subSystemCode:** 0
        *   **subSubSystemCode:** 0
        *   **assyCode:** 00
        *   **disassyCode:** 0A5
        *   **disassyCodeVariant:** AA
        *   **infoCode:** A
        *   **itemLocationCode:** A

### 2.3 faultDiagnosis

#### 2.3.1 reqs

*   **req (1):**
    *   **lreq:**
        *   **reqType:** mandatory
        *   **reqNumber:** 1

#### 2.3.2 observedFault

*   **faultDescription:** The lights do not operate correctly.
*   **faultLocation:**
    *   **lLoc:**
        *   **lLocType:** Electrical
*   **faultCause:**
    *   **lCause:**
        *   **causeType:** Component Failure

#### 2.3.3 troubleshooting

*   **step (1):**
    *   **stepNumber:** 1
    *   **stepText:** Check the power supply to the lights.
    *   **stepResult:** If the power supply is good, proceed to step 2.
*   **step (2):**
    *   **stepNumber:** 2
    *   **stepText:** Check the bulbs.
    *   **stepResult:** If the bulbs are good, proceed to step 3.

#### 2.3.4 failedComponent

*   **component:** Bulb

#### 2.3.5 remedialAction

*   **action:** Replace the bulb.

### 2.4 symptoms

*   **symptom:** Lights do not illuminate.

### 2.5 correctiveMaintenance

#### 2.5.1 reqs

*   **req (1):**
    *   **lreq:**
        *   **reqType:** mandatory
        *   **reqNumber:** 1

#### 2.5.2 step (1):**

*   **stepNumber:** 1
*   **stepText:** Disconnect the power supply.

#### 2.5.3 step (2):**

*   **stepNumber:** 2
*   **stepText:** Remove the faulty component.

#### 2.5.4 step (3):**

*   **stepNumber:** 3
*   **stepText:** Install the new component.

#### 2.5.5 step (4):**

*   **stepNumber:** 4
*   **stepText:** Reconnect the power supply.

## 3. Remarks

*   **simplePara:** This is the data module you would visit when you notice that the lights do not operate correctly.