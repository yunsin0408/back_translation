# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US

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
*   **language:** EN
*   **country:** US

#### DM Status

*   **First Verification:** tabtop
*   **Quality Assurance:** tabtop
*   **System Breakdown Code:** BY112
*   **Skill Level:** sk01
*   **Reason For Update:** S1000D upissued

### Content

#### References

*   **DM Ref 1:**
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

*   **DM Ref 2:**
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

*   **DM Ref 3:**
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

#### Fault Isolation

##### Fault Isolation Procedure

*   **Fault Code:** NYCJD04
*   **Fault Description:** Tire does not function correctly

*   **Preliminary Requirements:**

    *   **Support Equipment:**
        *   **Name:** Tire pressure gauge
        *   **Manufacturer Code:** KZ666
        *   **Part Number:** BSK-TLST-001-01
        *   **Quantity:** 1 EA
        *   **Name:** Specialist toolset
        *   **Manufacturer Code:** KZ666
        *   **Part Number:** BSK-TLST-001
        *   **Quantity:** 1 EA

*   **Isolation Main Procedure:**

    *   **Step 1 (stp-0001):**
        *   **Action:** Use the tire pressure gauge to check the pressure.
        *   **Question:** What is the tire pressure reading?
        *   **Choices:**
            *   More than 2700 hPa (Next Action: stp-0002)
            *   Between 100 hPa and 2700 hPa (Next Action: stp-0003)
            *   Less than 100 hPa (Next Action: stp-0004)

    *   **End Step (stp-0002):** Deflate the tire until the pressure is 2700 hPa

    *   **End Step (stp-0003):** Inflate the tire as given in DM Ref.

    *   **Step 2 (stp-0004):**
        *   **Action:** Check the tire for damage.
        *   **Question:** Is there damage to the tire?
        *   **Choices:**
            *   Yes (Next Action: stp-0005)
            *   No (Next Action: stp-0006)

    *   **End Step (stp-0005):** Replace the tire (refer to DM Ref).

    *   **End Step (stp-0006):** Replace the inner-tube (refer to DM Ref).