# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US

## Identification

*   **dmId:** DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US

## IdentAndStatusSection

### DmAddress

#### DmIdent

*   **modelIdentCode:** S1000DBIKE
*   **systemDiffCode:** AAA
*   **systemCode:** DA0
*   **subSystemCode:** 1
*   **subSubSystemCode:** 0
*   **assyCode:** 20
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **language:** EN
*   **country:** US

#### DmStatus

*   **firstVerification:** tabtop
*   **qualityAssurance:** tabtop
*   **systemBreakdownCode:** BY112
*   **skillLevel:** sk01
*   **reasonForUpdate:** S1000D upissued

### Content

#### References

*   **DmRef 1:**
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
*   **DmRef 2:**
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
*   **DmRef 3:**
    *   **modelIdentCode:** S1000DBIKE
    *   **systemDiffCode:** AAA
    *   **systemCode:** DA0
    *   **subSystemCode:** 1
    *   **subSubSystemCode:** 0
    *   **assyCode:** 20
    *   **disassyCode:** 00
    *   **disassyCodeVariant:** AA
    *   **infoCode:** 921
    *   **infoCodeVariant:** A
    *   **itemLocationCode:** A

#### FaultIsolation

*   **FaultIsolationProcedure:**
    *   **faultCode:** NYCJD04
    *   **faultDescription:** Tire does not function correctly
    *   **preliminaryRequirements:**
        *   **supportEquipment 1:**
            *   **name:** Tire pressure gauge
            *   **manufacturerCode:** KZ666
            *   **partNumber:** BSK-TLST-001-01
            *   **quantity:** 1 EA
        *   **supportEquipment 2:**
            *   **name:** Specialist toolset
            *   **manufacturerCode:** KZ666
            *   **partNumber:** BSK-TLST-001
            *   **quantity:** 1 EA
    *   **isolationMainProcedure:**
        *   **Step 1 (id: stp-0001):**
            *   **action:** Use the tire pressure gauge to check the pressure.
            *   **question:** What is the tire pressure reading?
            *   **choices:**
                *   More than 2700 hPa (nextAction: stp-0002)
                *   Between 100 hPa and 2700 hPa (nextAction: stp-0003)
                *   Less than 100 hPa (nextAction: stp-0004)
        *   **End Step (id: stp-0002):** Deflate the tire until the pressure is 2700 hPa
        *   **End Step (id: stp-0003):** Inflate the tire as given in DM Ref.
        *   **Step 2 (id: stp-0004):**
            *   **action:** Check the tire for damage.
            *   **question:** Is there damage to the tire?
            *   **choices:**
                *   Yes (nextAction: stp-0005)
                *   No (nextAction: stp-0006)
        *   **End Step (id: stp-0005):** Replace the tire (refer to DM Ref).
        *   **End Step (id: stp-0006):** Replace the inner-tube (refer to DM Ref).