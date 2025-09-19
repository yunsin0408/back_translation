# DMC-S1000DBIKE-AAA-D05-10-00-00AA-000A-A_011-00_EN-US_1_1

This document represents the converted markdown from the provided XML file, adhering to S1000D standards.

## 1. DM Ident

### 1.1 DM Address

#### 1.1.1 Model Identification

*   `modelIdentCode`: `S1000DBIKE`
*   `systemDiffCode`: `AAA`
*   `systemCode`: `D05`
*   `subSystemCode`: `1`
*   `subSubSystemCode`: `0`
*   `assyCode`: `00`
*   `disassyCode`: `00`
*   `disassyCodeVariant`: `AA`
*   `infoCode`: `000`
*   `infoCodeVariant`: `A`
*   `itemLocationCode`: `A`

#### 1.1.2 Language

*   `countryIsoCode`: `US`
*   `languageIsoCode`: `en`

#### 1.1.3 Issue Information

*   `issueNumber`: `011`
*   `inWork`: `00`

### 1.2 DM Address Items

#### 1.2.1 Issue Date

*   `year`: `2024`
*   `month`: `06`
*   `day`: `19`

#### 1.2.2 DM Title

*   `techName`: `Bicycle`
*   `infoName`: `Time limits`

### 1.3 DM Status

#### 1.3.1 Issue Type

*   `changed`

#### 1.3.2 Security

*   `securityClassification`: `01`
*   `commercialClassification`: `cc51`
*   `caveat`: `cv51`

#### 1.3.3 Data Restrictions

*   **Restriction Instructions**
    *   `dataDistribution`: `To be made available to all S1000D users.`
    *   `exportControl`:
        *   `exportRegistrationStmt`:
            *   `simplePara`: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
    *   `dataHandling`: `There are no specific handling instructions for this data module.`
    *   `dataDestruction`: `Users may destroy this data module in accordance with their own local procedures.`
    *   `dataDisclosure`: `There are no dissemination limitations that apply to this data module.`

*   **Restriction Info**
    *   `copyright`:
        *   `copyrightPara`: `*Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD`
        *   `copyrightPara`: `*Publishers:*`
        *   `randomList`:
            *   `Aerospace, Security and Defence Industries Association of Europe`
            *   `Aerospace Industries Association of America`
            *   `ATA e-Business Program`
        *   `copyrightPara`: `*Limitations of liability:*`
        *   `randomList`:
            *   `This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.`
            *   `Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages arising out of the use of this material.`
            *   `The use of this material is at your own risk.`
        *   `policyStatement`:
            *   `simplePara`: `The user agrees to indemnify and hold harmless ASD, its officers, directors, employees and agents from any and all claims, damages, liabilities, costs and expenses, including attorneys' fees, arising out of or relating to the use of this material.`
        *   `policyStatement`:
            *   `simplePara`: `This material is subject to change without notice.`

#### 1.3.4 Responsible Person

*   `name`: `John Doe`
*   `organization`: `Example Org.`

#### 1.3.5 Applicability

*   `applicabilityCode`: `A`
*   `applicabilityDescription`: `Applicable to all models`

#### 1.3.6 System Breakdown Code

*   `BY`

#### 1.3.7 Skill Level

*   `sk01`

#### 1.3.8 Reason For Update

*   `id`: `rfu_general`
*   `updateReasonType`: `urt03`
*   `simplePara`: `S1000D upissued`

## 2. Content

### 2.1 Referenced Applic Group

#### 2.1.1 Applic

*   `id`: `MK1MK9`
*   `displayText`:
    *   `simplePara`: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)`
*   `evaluate`:
    *   `assert`:
        *   `applicPropertyIdent`: `type`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Mountain bicycle`
    *   `evaluate`:
        *   `assert`:
            *   `applicPropertyIdent`: `model`
            *   `applicPropertyType`: `prodattr`
            *   `applicPropertyValues`: `Mountain storm`
        *   `assert`:
            *   `applicPropertyIdent`: `version`
            *   `applicPropertyType`: `prodattr`
            *   `applicPropertyValues`: `Mk1`
        *   `evaluate`:
            *   `assert`:
                *   `applicPropertyIdent`: `model`
                *   `applicPropertyType`: `prodattr`
                *   `applicPropertyValues`: `Brook trekker`
            *   `assert`:
                *   `applicPropertyIdent`: `version`
                *   `applicPropertyType`: `prodattr`
                *   `applicPropertyValues`: `Mk9`

### 2.2 Time Limit

#### 2.2.1 Time Limit Item 1

*   `applicRef`: `MK1MK9`
*   `equip`:
    *   `name`: `Bicycle`
    *   `ident`:
        *   `manufacturerCode`: `KZ555`
        *   `partNumber`: `Ch-001`
*   `timeLimit`:
    *   `limitType`: `lt05`
    *   `threshold`:
        *   `unitMeas`: `th03`
        *   `value`: `1`

#### 2.2.2 Time Limit Item 2

*   `applicRef`: `MK1MK9`
*   `equip`:
    *   `name`: `Hub bearings`
    *   `ident`:
        *   `manufacturerCode`: `KZ555`
        *   `partNumber`: `HB-001`
*   `timeLimit`:
    *   `limitType`: `lt06`
    *   `threshold`:
        *   `unitMeas`: `th03`
        *   `value`: `6`
    *   `tolerance`:
        *   `toleranceType`: `plusorminus`
        *   `toleranceValue`: `1`