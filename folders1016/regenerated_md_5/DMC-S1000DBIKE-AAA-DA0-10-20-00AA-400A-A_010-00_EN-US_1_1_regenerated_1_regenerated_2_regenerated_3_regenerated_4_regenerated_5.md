# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US

## Identification
<dmId>DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US</dmId>
## IdentAndStatusSection

### DmAddress

#### DmIdent
<modelIdentCode>S1000DBIKE</modelIdentCode>
<systemDiffCode>AAA</systemDiffCode>
<systemCode>DA0</systemCode>
<subSystemCode>1</subSystemCode>
<subSubSystemCode>0</subSubSystemCode>
<assyCode>20</assyCode>
<disassyCode>00</disassyCode>
<disassyCodeVariant>AA</disassyCodeVariant>
<language>EN</language>
<country>US</country>
#### DmStatus
<firstVerification>tabtop</firstVerification>
<qualityAssurance>tabtop</qualityAssurance>
<systemBreakdownCode>BY112</systemBreakdownCode>
<skillLevel>sk01</skillLevel>
<reasonForUpdate>S1000D upissued</reasonForUpdate>
### Content

#### References

##### DmRef
<modelIdentCode>S1000DBIKE</modelIdentCode>
<systemDiffCode>AAA</systemDiffCode>
<systemCode>DA0</systemCode>
<subSystemCode>1</subSystemCode>
<subSubSystemCode>0</subSubSystemCode>
<assyCode>10</assyCode>
<disassyCode>00</disassyCode>
<disassyCodeVariant>AA</disassyCodeVariant>
<infoCode>921</infoCode>
<infoCodeVariant>A</infoCodeVariant>
<itemLocationCode>A</itemLocationCode>
##### DmRef
<modelIdentCode>S1000DBIKE</modelIdentCode>
<systemDiffCode>AAA</systemDiffCode>
<systemCode>DA0</systemCode>
<subSystemCode>1</subSubSystemCode>
<subSubSystemCode>0</subSubSystemCode>
<assyCode>20</assyCode>
<disassyCode>00</disassyCode>
<disassyCodeVariant>AA</disassyCodeVariant>
<infoCode>215</infoCode>
<infoCodeVariant>A</infoCodeVariant>
<itemLocationCode>A</itemLocationCode>
##### DmRef
<modelIdentCode>S1000DBIKE</modelIdentCode>
<systemDiffCode>AAA</systemDiffCode>
<systemCode>DA0</systemCode>
<subSystemCode>1</subSubSystemCode>
<subSubSystemCode>0</subSubSystemCode>
<assyCode>20</assyCode>
<disassyCode>00</disassyCode>
<disassyCodeVariant>AA</disassyCodeVariant>
<infoCode>921</infoCode>
<infoCodeVariant>A</infoCodeVariant>
<itemLocationCode>A</itemLocationCode>
#### FaultIsolation

##### FaultIsolationProcedure

*   **Fault Code:** NYCJD04
*   **Fault Description:** Tire does not function correctly

*   **Preliminary Requirements:**

    *   **Support Equipment:**
        *   **Name:** Tire pressure gauge
        *   **Manufacturer Code:** KZ666
        *   **Part Number:** BSK-TLST-001-01
        *   **Quantity:** 1 EA

    *   **Support Equipment:**
        *   **Name:** Specialist toolset
        *   **Manufacturer Code:** KZ666
        *   **Part Number:** BSK-TLST-001
        *   **Quantity:** 1 EA

*   **Isolation Main Procedure:**

    *   **Step ID:** stp-0001
        *   **Action:** Use the tire pressure gauge to check the pressure.
        *   **Question:** What is the tire pressure reading?
        *   **Choices:**
            *   More than 2700 hPa (Next Action: stp-0002)
            *   Between 100 hPa and 2700 hPa (Next Action: stp-0003)
            *   Less than 100 hPa (Next Action: stp-0004)

    *   **End Step ID:** stp-0002
        *   Deflate the tire until the pressure is 2700 hPa

    *   **End Step ID:** stp-0003
        *   Inflate the tire as given in DM Ref.

    *   **Step ID:** stp-0004
        *   **Action:** Check the tire for damage.
        *   **Question:** Is there damage to the tire?
        *   **Choices:**
            *   Yes (Next Action: stp-0005)
            *   No (Next Action: stp-0006)

    *   **End Step ID:** stp-0005
        *   Replace the tire (refer to DM Ref).

    *   **End Step ID:** stp-0006
        *   Replace the inner-tube (refer to DM Ref).