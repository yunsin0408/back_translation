# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US - Procedure Document

This document represents the procedure defined in the provided XML file, adhering to the S1000D standard.

## 1. Identification

*   **Identification:** `DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US`

## 2. Ident And Status Section

### 2.1 DM Address

#### 2.1.1 DM Ident

*   **modelIdentCode:** `S1000DBIKE`
*   **systemDiffCode:** `AAA`
*   **systemCode:** `DA0`
*   **subSystemCode:** `1`
*   **subSubSystemCode:** `0`
*   **assyCode:** `20`
*   **disassyCode:** `00`
*   **disassyCodeVariant:** `AA`
*   **language:** `EN`
*   **country:** `US`

#### 2.1.2 DM Status

*   **First Verification:** `tabtop`
*   **Quality Assurance:** `tabtop`
*   **System Breakdown Code:** `BY112`
*   **Skill Level:** `sk01`
*   **Reason For Update:** `S1000D upissued`

### 2.2 Content

#### 2.2.1 References

*   **DM Ref 1:**
    *   **modelIdentCode:** `S1000DBIKE`
    *   **systemDiffCode:** `AAA`
    *   **systemCode:** `DA0`
    *   **subSystemCode:** `1`
    *   **subSubSystemCode:** `0`
    *   **assyCode:** `10`
    *   **disassyCode:** `00`
    *   **disassyCodeVariant:** `AA`
    *   **infoCode:** `921`
    *   **infoCodeVariant:** `A`
    *   **itemLocationCode:** `A`

*   **DM Ref 2:**
    *   **modelIdentCode:** `S1000DBIKE`
    *   **systemDiffCode:** `AAA`
    *   **systemCode:** `DA0`
    *   **subSystemCode:** `1`
    *   **subSubSystemCode:** `0`
    *   **assyCode:** `20`
    *   **disassyCode:** `00`
    *   **disassyCodeVariant:** `AA`
    *   **infoCode:** `215`
    *   **infoCodeVariant:** `A`
    *   **itemLocationCode:** `A`

*   **DM Ref 3:**
    *   **modelIdentCode:** `S1000DBIKE`
    *   **systemDiffCode:** `AAA`
    *   **systemCode:** `DA0`
    *   **subSystemCode:** `1`
    *   **subSubSystemCode:** `0`
    *   **assyCode:** `20`
    *   **disassyCode:** `00`
    *   **disassyCodeVariant:** `AA`
    *   **infoCode:** `921`
    *   **infoCodeVariant:** `A`
    *   **itemLocationCode:** `A`

#### 2.2.2 Fault Isolation

##### 2.2.2.1 Fault Isolation Procedure

*   **faultCode:** `NYCJD04`
*   **faultDescription:** `Tire does not function correctly`

##### 2.2.2.2 Preliminary Requirements

*   **supportEquipment 1:**
    *   **name:** `Tire pressure gauge`
    *   **manufacturerCode:** `KZ666`
    *   **partNumber:** `BSK-TLST-001-01`
    *   **quantity:** `1 EA`

*   **supportEquipment 2:**
    *   **name:** `Specialist toolset`
    *   **manufacturerCode:** `KZ666`
    *   **partNumber:** `BSK-TLST-001`
    *   **quantity:** `1 EA`

##### 2.2.2.3 Isolation Main Procedure

*   **Step 1 (stp-0001):**
    *   **action:** `Use the tire pressure gauge to check the pressure.`
    *   **question:** `What is the tire pressure reading?`
    *   **choices:**
        *   `More than 2700 hPa` (nextAction: `stp-0002`)
        *   `Between 100 hPa and 2700 hPa` (nextAction: `stp-0003`)
        *   `Less than 100 hPa` (nextAction: `stp-0004`)

*   **End Step (stp-0002):** `Deflate the tire until the pressure is 2700 hPa`

*   **End Step (stp-0003):** `Inflate the tire as given in DM Ref.`

*   **Step 2 (stp-0004):**
    *   **action:** `Check the tire for damage.`
    *   **question:** `Is there damage to the tire?`
    *   **choices:**
        *   `Yes` (nextAction: `stp-0005`)
        *   `No` (nextAction: `stp-0006`)

*   **End Step (stp-0005):** `Replace the tire (refer to DM Ref).`

*   **End Step (stp-0006):** `Replace the inner-tube (refer to DM Ref).`