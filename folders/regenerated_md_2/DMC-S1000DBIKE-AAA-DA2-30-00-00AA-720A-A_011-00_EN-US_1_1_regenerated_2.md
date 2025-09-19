```markdown
# DMC-S1000DBIKE-AAA-DA2-30-00-00AA-720A-A_011-00_EN-US - Headset Install Procedures

This document details the installation procedures for the Headset, as per the provided XML data.

## 1. Ident And Status Section

### 1.1 DM Address

#### 1.1.1 DM Ident

*   **modelIdentCode**: S1000DBIKE
*   **systemDiffCode**: AAA
*   **systemCode**: DA2
*   **subSystemCode**: 3
*   **subSubSystemCode**: 0
*   **assyCode**: 00
*   **disassyCode**: 00
*   **disassyCodeVariant**: AA
*   **infoCode**: 720
*   **infoCodeVariant**: A
*   **itemLocationCode**: A
*   **language**:
    *   **countryIsoCode**: US
    *   **languageIsoCode**: en
*   **issueInfo**:
    *   **issueNumber**: 011
    *   **inWork**: 00

#### 1.1.2 DM Address Items

*   **issueDate**:
    *   **year**: 2024
    *   **month**: 06
    *   **day**: 19
*   **dmTitle**:
    *   **techName**: Headset
    *   **infoName**: Install procedures

### 1.2 DM Status

*   **issueType**: changed
*   **security**:
    *   **securityClassification**: 01
    *   **commercialClassification**: cc51
    *   **caveat**: cv51
*   **dataRestrictions**:
    *   **restrictionInstructions**:
        *   **dataDistribution**:
        *   **dataUse**:
    *   **dataSupport**:
*   **qualityAssurance**:
*   **systemBreakdownCode**: BY143
*   **skillLevel**: sk02
*   **reasonForUpdate**:
    *   **id**: rfu_general
    *   **updateReasonType**: urt03
    *   **simplePara**: S1000D upissued

## 2. Content

### 2.1 References

#### 2.1.1 DM Ref

*   **modelIdentCode**: S1000DBIKE
*   **systemDiffCode**: AAA
*   **systemCode**: DA2
*   **subSystemCode**: 1
*   **subSubSystemCode**: 0
*   **assyCode**: 00
*   **disassyCode**: 00
*   **disassyCodeVariant**: AA
*   **infoCode**: 720
*   **infoCodeVariant**: A
*   **itemLocationCode**: A

### 2.2 Procedure

#### 2.2.1 Preliminary Requirements

*   **requiredConditions**:
    *   **simplePara**: The bicycle is safely held on a work stand
*   **requiredPersonnel**:
    *   **person**:
        *   **personCategory**: Bike Rider
        *   **personSkill**: sk02
        *   **trade**: Operator
        *   **estimatedTime**: 1.5 h
*   **requiredSupportEquipment**:
    *   **supportEquipDescription**:
        *   **name**: Work stand
        *   **identNumber**:
            *   **manufacturerCode**: Stand
            *   **partAndSerialNumber**:
                *   **partNumber**: Stand-001
        *   **reqQuantity**: 1 EA
*   **requiredSupplies**:
*   **requiredSpares**:
    *   **spareDescription (spa-0001)**:
        *   **name**: Frame fork
        *   **identNumber**:
            *   **manufacturerCode**: KZ555
            *   **partAndSerialNumber**:
                *   **partNumber**: St-001-02
        *   **reqQuantity**: 1 EA
    *   **spareDescription (spa-0002)**:
        *   **name**: Upper bearing cup
        *   **identNumber**:
            *   **manufacturerCode**: KZ555
            *   **partAndSerialNumber**:
                *   **partNumber**: St-001-03
        *   **reqQuantity**: 1 EA
    *   **spareDescription (spa-0003)**:
        *   **name**: Brake cable hangar
        *   **identNumber**:
            *   **manufacturerCode**: KT444
            *   **partAndSerialNumber**:
                *   **partNumber**: BR-LVRS-002
        *   **reqQuantity**: 1 EA
    *   **spareDescription (spa-0004)**:
        *   **name**: Dust seal
        *   **identNumber**:
            *   **manufacturerCode**: KZ555
            *   **partAndSerialNumber**:
                *   **partNumber**: St-001-04
        *   **reqQuantity**: 1 EA
    *   **spareDescription (spa-0005)**:
        *   **name**: Conical expansion washer
        *   **identNumber**:
            *   **manufacturerCode**: KZ555
            *   **partAndSerialNumber**:
                *   **partNumber**: St-001-05
        *   **reqQuantity**: 1 EA
*   **requiredSafety**:

#### 2.2.2 Main Procedure

*   Install the `<internalRef internalRefId="spa-0001" internalRefTargetType="irtt06"/>` on the frame.
*   Install the `<internalRef internalRefId="spa-0002" internalRefTargetType="irtt06"/>`.
*   Install the components that follow on the steering tube:
    *   the `<internalRef internalRefId="spa-0003" internalRefTargetType="irtt06"/>`
    *   the `<internalRef internalRefId="spa-0004" internalRefTargetType="irtt06"/>`
    *   the `<internalRef internalRefId="spa-0005" internalRefTargetType="irtt06"/>`
*   Install the stem (refer to
   ```xml
   <dmRef>
        <modelIdentCode>S1000DBIKE</modelIdentCode>
        <systemDiffCode>AAA</systemDiffCode>
        <systemCode>DA2</systemCode>
        <subSystemCode>1</subSystemCode>
        <subSubSystemCode>0</subSubSystemCode>
        <assyCode>00</assyCode>
        <disassyCode>00</disassyCode>
        <disassyCodeVariant>AA</disassyCodeVariant>
        <infoCode>720</infoCode>
        <infoCodeVariant>A</infoCodeVariant>
        <itemLocationCode>A</itemLocationCode>
    </dmRef>
   ```
   ).

#### 2.2.3 Close Requirements

*   **simplePara**: No conditions.
```