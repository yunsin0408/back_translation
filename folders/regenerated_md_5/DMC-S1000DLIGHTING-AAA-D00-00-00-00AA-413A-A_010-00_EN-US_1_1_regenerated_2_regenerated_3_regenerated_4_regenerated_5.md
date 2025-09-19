# DMC-S1000DLIGHTING - Data Module

This document represents the data module `DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-413A-A_010-00_EN-US_1_1_regenerated_2_regenerated_3_regenerated_4_regenerated.XML`. It adheres to the S1000D standard and references the schema located at `http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd`.

## 1. DM Ident

### 1.1 DM Address

*   `modelIdentCode`: `S1000DLIGHTING`
*   `systemDiffCode`: `AAA`
*   `systemCode`: `D00`
*   `subSystemCode`: `0`
*   `subSubSystemCode`: `0`
*   `assyCode`: `00`
*   `disassyCode`: `00`
*   `disassyCodeVariant`: `AA`
*   `infoCode`: `413`
*   `infoCodeVariant`: `A`
*   `itemLocationCode`: `A`

### 1.2 DM Address Items

*   `issueDate`:
    *   `year`: `2024`
    *   `month`: `06`
    *   `day`: `19`
*   `techName`: `Lights`
*   `infoName`: `Observed fault`

## 2. DM Status

*   `issueType`: `changed`

### 2.1 Security

*   `securityClassification`: `01`
*   `commercialClassification`: `cc51`
*   `caveat`: `cv51`

### 2.2 Data Restrictions

#### 2.2.1 Restriction Instructions

*   `dataDistribution`: `To be made available to all S1000D users.`
*   `exportControl`:
    *   `exportRegistrationStatement`: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
*   `dataHandling`: `There are no specific handling instructions for this data module.`
*   `dataDestruction`: `Users may destroy this data module in accordance with their own local procedures.`
*   `dataDisclosure`: `There are no dissemination limitations that apply to this data module.`

#### 2.2.2 Restriction Info

*   `copyright`: `*Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD`

*   `remarks`: `random remark`
*   `applicability`: `random applicability`
*   `remarks`: `random remark`

## 3. Content

### 3.1 References

*   `dmRef` (1):
    *   `modelIdentCode`: `S1000DLIGHTING`
    *   `systemDiffCode`: `AAA`
    *   `systemCode`: `D00`
    *   `subSystemCode`: `0`
    *   `subSubSystemCode`: `0`
    *   `assyCode`: `00`
    *   `disassyCode`: `0A5`
    *   `disassyCodeVariant`: `AA`
    *   `infoCode`: `A`
    *   `itemLocationCode`: `A`

*   `dmRef` (2):
    *   `modelIdentCode`: `S1000DLIGHTING`
    *   `systemDiffCode`: `AAA`
    *   `systemCode`: `D00`
    *   `subSystemCode`: `0`
    *   `subSubSystemCode`: `0`
    *   `assyCode`: `00`
    *   `disassyCode`: `0A4`
    *   `disassyCodeVariant`: `AA`
    *   `infoCode`: `A`
    *   `itemLocationCode`: `A`

### 3.2 Warnings and Cautions References

*   `warningRef` (1):
    *   `id`: `w001`
    *   `warningIdentNumber`: `warning-001`
    *   `dmRef`:
        *   `modelIdentCode`: `S1000DLIGHTING`
        *   `systemDiffCode`: `AAA`
        *   `systemCode`: `D00`
        *   `subSystemCode`: `0`
        *   `subSubSystemCode`: `0`
        *   `assyCode`: `00`
        *   `disassyCode`: `0A4`
        *   `disassyCodeVariant`: `AA`
        *   `infoCode`: `A`
        *   `itemLocationCode`: `A`

*   `warningRef` (2):
    *   `id`: `w002`
    *   `warningIdentNumber`: `warning-002`
    *   `dmRef`:
        *   `modelIdentCode`: `S1000DLIGHTING`
        *   `systemDiffCode`: `AAA`
        *   `systemCode`: `D00`
        *   `subSystemCode`: `0`
        *   `subSubSystemCode`: `0`
        *   `assyCode`: `00`
        *   `disassyCode`: `0A4`
        *   `disassyCodeVariant`: `AA`
        *   `infoCode`: `A`
        *   `itemLocationCode`: `A`

*   `cautionRef`:
    *   `id`: `c001`
    *   `cautionIdentNumber`: `caution-001`
    *   `dmRef`:
        *   `modelIdentCode`: `S1000DLIGHTING`
        *   `systemDiffCode`: `AAA`
        *   `systemCode`: `D00`
        *   `subSystemCode`: `0`
        *   `subSubSystemCode`: `0`
        *   `assyCode`: `00`
        *   `disassyCode`: `0A5`
        *   `disassyCodeVariant`: `AA`
        *   `infoCode`: `A`
        *   `itemLocationCode`: `A`

### 3.3 Fault Diagnosis

*   `requirements`:
    *   `lReq`:
        *   `reqType`: `mandatory`
        *   `reqNumber`: `1`
*   `faultDescription`: `The lights do not operate correctly.`

### 3.4 Corrective Maintenance

*   `requirements`:
    *   `lReq`:
        *   `reqType`: `mandatory`
        *   `reqNumber`: `1`
*   `steps`:
    1.  `stepNumber`: `1`
        `stepText`: `Disconnect the power supply.`
    2.  `stepNumber`: `2`
        `stepText`: `Install the new component.`
    3.  `stepNumber`: `3`
        `stepText`: `Install the new component.`
    4.  `stepNumber`: `4`
        `stepText`: `Reconnect the power supply.`

### 3.5 Symptoms

`The lights do not operate correctly.`

## 4. Remarks

`This is the data module you would visit when you notice that the lights do not operate correctly.`