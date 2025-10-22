# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US

## identAndStatusSection

### dmAddress

#### dmIdent

*   modelIdentCode: S1000DBIKE
*   systemDiffCode: AAA
*   systemCode: DA0
*   subSystemCode: 1
*   subSubSystemCode: 0
*   assyCode: 20
*   disassyCode: 00
*   disassyCodeVariant: AA
*   language: EN
*   country: US

#### dmStatus

*   firstVerification: tabtop
*   qualityAssurance: tabtop
*   systemBreakdownCode: BY112
*   skillLevel: sk01
*   reasonForUpdate: S1000D upissued

### content

#### references

*   dmRef:
    *   modelIdentCode: S1000DBIKE
    *   systemDiffCode: AAA
    *   systemCode: DA0
    *   subSystemCode: 1
    *   subSubSystemCode: 0
    *   assyCode: 10
    *   disassyCode: 00
    *   disassyCodeVariant: AA
    *   infoCode: 921
    *   infoCodeVariant: A
    *   itemLocationCode: A
*   dmRef:
    *   modelIdentCode: S1000DBIKE
    *   systemDiffCode: AAA
    *   systemCode: DA0
    *   subSystemCode: 1
    *   subSubSystemCode: 0
    *   assyCode: 20
    *   disassyCode: 00
    *   disassyCodeVariant: AA
    *   infoCode: 215
    *   infoCodeVariant: A
    *   itemLocationCode: A
*   dmRef:
    *   modelIdentCode: S1000DBIKE
    *   systemDiffCode: AAA
    *   systemCode: DA0
    *   subSystemCode: 1
    *   subSubSystemCode: 0
    *   assyCode: 20
    *   disassyCode: 00
    *   disassyCodeVariant: AA
    *   infoCode: 921
    *   infoCodeVariant: A
    *   itemLocationCode: A

#### faultIsolation

*   faultIsolationProcedure:
    *   faultCode: NYCJD04
    *   faultDescription: Tire does not function correctly
    *   preliminaryRequirements:
        *   supportEquipment:
            *   name: Tire pressure gauge
            *   manufacturerCode: KZ666
            *   partNumber: BSK-TLST-001-01
            *   quantity: 1 EA
        *   supportEquipment:
            *   name: Specialist toolset
            *   manufacturerCode: KZ666
            *   partNumber: BSK-TLST-001
            *   quantity: 1 EA
    *   isolationMainProcedure:
        *   step id="stp-0001":
            *   action: Use the tire pressure gauge to check the pressure.
            *   question: What is the tire pressure reading?
            *   choices:
                *   choice nextAction="stp-0002": More than 2700 hPa
                *   choice nextAction="stp-0003": Between 100 hPa and 2700 hPa
                *   choice nextAction="stp-0004": Less than 100 hPa
        *   endStep id="stp-0002": Deflate the tire until the pressure is 2700 hPa
        *   endStep id="stp-0003": Inflate the tire as given in DM Ref.
        *   step id="stp-0004":
            *   action: Check the tire for damage.
            *   question: Is there damage to the tire?
            *   choices:
                *   choice nextAction="stp-0005": Yes
                *   choice nextAction="stp-0006": No
        *   endStep id="stp-0005": Replace the tire (refer to DM Ref).
        *   endStep id="stp-0006": Replace the inner-tube (refer to DM Ref).