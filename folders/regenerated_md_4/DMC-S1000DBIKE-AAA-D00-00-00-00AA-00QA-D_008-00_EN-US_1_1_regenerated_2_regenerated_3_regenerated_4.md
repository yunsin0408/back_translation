# DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US_1_1 - Mountain bicycle - Conditions cross-reference table

## 1. DM Ident

### 1.1 DM Address

#### 1.1.1 DM Ident

*   modelIdentCode: `S1000DBIKE`
*   systemDiffCode: `AAA`
*   systemCode: `D00`
*   subSystemCode: `0`
*   subSubSystemCode: `0`
*   assyCode: `00`
*   disassyCode: `00`
*   disassyCodeVariant: `AA`
*   infoCode: `00Q`
*   infoCodeVariant: `A`
*   itemLocationCode: `D`

#### 1.1.2 Language

*   countryIsoCode: `US`
*   languageIsoCode: `en`

#### 1.1.3 Issue Info

*   issueNumber: `008`
*   inWork: `00`

#### 1.1.4 DM Address Items

*   Issue Date:
    *   year: `2024`
    *   month: `06`
    *   day: `19`
*   DM Title:
    *   techName: `Mountain bicycle`
    *   infoName: `Conditions cross-reference table`

## 2. DM Status

*   issueType: `changed`

### 2.1 Security

#### 2.1.1 Security Classification

*   securityClassification: `01`

#### 2.1.2 Data Restrictions

##### 2.1.2.1 Restriction Instructions

###### 2.1.2.1.1 Export Control

*   exportRegistrationStmt: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
*   dataHandling: `There are no specific handling instructions for this data module.`
*   dataDestruction: `Users may destroy this data module in accordance with their own local procedures.`
*   dataDisclosure: `There are no dissemination limitations that apply to this data module.`

##### 2.1.2.2 Restriction Info

*   Copyright: `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
*   Publishers:
    *   `Aerospace, Security and Defence Industries Association of Europe`
    *   `Aerospace Industries Association of America`
    *   `ATA e-Business Program`
*   Limitations of Liability:
    *   limitation: `This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.`
    *   limitation: `Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability.`

### 2.2 Responsible Department

*   value: `Engineering`

## 3. Dependencies

*   forCondValues: `POST-001`
*   dependencyTest: `A-1`

## 4. Content

### 4.1 Referenced Applic Group

#### 4.1.1 Applic A_1

*   assert:
    *   applicPropertyType: `condition`
    *   applicPropertyIdent: `SB-S001`
    *   applicPropertyValues: `POST-001~POST-999`

#### 4.1.2 Applic A_2

*   evaluate:
    *   andOr: `and`
*   assert1:
    *   applicPropertyType: `condition`
    *   applicPropertyIdent: `SB-S001`
    *   applicPropertyValues: `POST-001~POST-999`
*   assert2:
    *   applicPropertyType: `condition`
    *   applicPropertyIdent: `SB-S009`
    *   applicPropertyValues: `PRE`

### 4.2 Cond Cross Reference Table

#### 4.2.1 Cond Type List

*   Cond Type SB:
    *   id: `SB`
    *   valueDataType: `string`
    *   name: `Service bulletin`
    *   descr: `Generic service bulletin type`
    *   enumeration: `PRE`
*   Cond Type Boolean:
    *   id: `Boolean`
    *   name: `generic Boolean condition`
    *   descr: `Boolean condition`
    *   enumeration: `True|False`

#### 4.2.2 Cond List

*   Cond SB_S001:
    *   condTypeRefId: `SB`
    *   id: `SB-S001`
    *   name: `Service bulletin 1`
    *   descr: `Service bulletin description 1`
    *   refs:
        *   dmRef:
            *   dmIdent:
                *   modelIdentCode: `S1000DBIKE`
                *   systemDiffCode: `AAA`
                *   systemCode: `DA0`
                *   subSystemCode: `2`
                *   subSubSystemCode: `0`
                *   assyCode: `00`
                *   disassyCode: `00`
                *   disassyCodeVariant: `AA`
                *   infoCode: `520`
                *   infoCodeVariant: `A`
                *   itemLocationCode: `A`
*   Cond SB_S009:
    *   condTypeRefId: `SB`
    *   id: `SB-S009`
    *   name: `Service bulletin 9`
    *   descr: `Service bulletin description 9`
    *   refs:
        *   dmRef:
            *   dmIdent:
                *   modelIdentCode: `S1000DBIKE`
                *   systemDiffCode: `AAA`
                *   systemCode: `DA0`
                *   subSystemCode: `2`
                *   subSubSystemCode: `0`
                *   assyCode: `00`
                *   disassyCode: `00`
                *   disassyCodeVariant: `AA`
                *   infoCode: `520`
                *   infoCodeVariant: `A`
                *   itemLocationCode: `A`

#### 4.2.3 Cond Incorporation List

*   Cond Incorporation SB_S001_00:
    *   condRefId: `SB-S001`
    *   incorporationStatus:
        *   incorporationStatus: `noeffect`
*   Cond Incorporation SB_S001_00:
    *   condRefId: `SB-S001`
    *   incorporationStatus:
        *   incorporationStatus: `noeffect`