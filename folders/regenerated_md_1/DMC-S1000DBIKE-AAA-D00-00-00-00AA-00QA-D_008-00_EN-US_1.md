# DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US

## Ident and Status Section

### DM Address

#### DM Ident

*   **modelIdentCode:** `S1000DBIKE`
*   **systemDiffCode:** `AAA`
*   **systemCode:** `D00`
*   **subSystemCode:** `0`
*   **subSubSystemCode:** `0`
*   **assyCode:** `00`
*   **disassyCode:** `00`
*   **disassyCodeVariant:** `AA`
*   **infoCode:** `00Q`
*   **infoCodeVariant:** `A`
*   **itemLocationCode:** `D`

**Language:**
*   **countryIsoCode:** `US`
*   **languageIsoCode:** `en`

**Issue Info:**
*   **issueNumber:** `008`
*   **inWork:** `00`

#### DM Address Items

*   **issueDate:**
    *   **year:** `2024`
    *   **month:** `06`
    *   **day:** `19`
*   **DM Title:**
    *   **techName:** `Mountain bicycle`
    *   **infoName:** `Conditions cross-reference table`

### DM Status

*   **issueType:** `changed`
*   **security:**
    *   **securityClassification:** `01`
*   **Data Restrictions:**
    *   **Restriction Instructions:**
        *   **dataDistribution:** `To be made available to all S1000D users.`
        *   **exportControl:**
            *   **exportRegistrationStmt:**
                *   `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
            *   **dataHandling:** `There are no specific handling instructions for this data module.`
            *   **dataDestruction:** `Users may destroy this data module in accordance with their own local procedures.`
            *   **dataDisclosure:** `There are no dissemination limitations that apply to this data module.`
    *   **Restriction Info:**
        *   **copyright:**
            *   `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
            *   **Publishers:**
                *   `Aerospace, Security and Defence Industries Association of Europe`
                *   `Aerospace Industries Association of America`
                *   `ATA e-Business Program`
            *   **Limitations of liability:**
                *   `This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.`
                *   `Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability.`
        *   **policy:**
            *   `The content of this document is confidential and proprietary.`
*   **Responsible Department:**
    *   `Engineering`

### Dependencies

*   **forCondValues:** `POST-001`
*   **dependencyTest:** `A-1`

## Content

### Referenced Applic Group

#### Applic (A-1)

*   **assert:**
    *   **applicPropertyType:** `condition`
    *   **applicPropertyIdent:** `SB-S001`
    *   **applicPropertyValues:** `POST-001~POST-999`

#### Applic (A-2)

*   **Evaluate:**
    *   **andOr:** `and`
    *   **Assert 1:**
        *   **applicPropertyType:** `condition`
        *   **applicPropertyIdent:** `SB-S001`
        *   **applicPropertyValues:** `POST-001~POST-999`
    *   **Assert 2:**
        *   **applicPropertyType:** `condition`
        *   **applicPropertyIdent:** `SB-S009`
        *   **applicPropertyValues:** `PRE`

### Cond Cross-Reference Table

#### Cond Type List

*   **Cond Type (SB):**
    *   **id:** `SB`
    *   **valueDataType:** `string`
    *   **name:** `Service bulletin`
    *   **descr:** `Generic service bulletin type`
    *   **enumeration:** `PRE`
*   **Cond Type (Boolean):**
    *   **id:** `Boolean`
    *   **name:** `generic Boolean condition`
    *   **descr:** `Boolean condition`
    *   **enumeration:** `True|False`

#### Cond List

*   **Cond (SB-S001):**
    *   **condTypeRefId:** `SB`
    *   **id:** `SB-S001`
    *   **name:** `Service bulletin S001 - Chain guard`
    *   **descr:** `Service bulletin S001 for the installation of the chain guard`
    *   **refs:**
        *   **dmRef:**
            *   **dmRefIdent:**
                *   **dmCode:**
                    *   **modelIdentCode:** `S1000DBIKE`
                    *   **systemDiffCode:** `AAA`
                    *   **systemCode:** `DA0`
                    *   **subSystemCode:** `2`
                    *   **subSubSystemCode:** `0`
                    *   **assyCode:** `00`
                    *   **disassyCode:** `00`
                    *   **disassyCodeVariant:** `AA`
                    *   **infoCode:** `520`
                    *   **infoCodeVariant:** `A`
                    *   **itemLocationCode:** `A`
*   **Cond (SB-S009):**
    *   **condTypeRefId:** `SB`
    *   **id:** `SB-S009`
    *   **name:** `Service bulletin 9 - Chain guard (2)`
    *   **descr:** `Service bulletin 9 for the installation of the chain guard (2)`
    *   **refs:**
        *   **dmRef:**
            *   **dmRefIdent:**
                *   **dmCode:**
                    *   **modelIdentCode:** `S1000DBIKE`
                    *   **systemDiffCode:** `AAA`
                    *   **systemCode:** `DA0`
                    *   **subSystemCode:** `2`
                    *   **subSubSystemCode:** `0`
                    *   **assyCode:** `01`
                    *   **disassyCode:** `00`
                    *   **disassyCodeVariant:** `AA`
                    *   **infoCode:** `520`
                    *   **infoCodeVariant:** `A`
                    *   **itemLocationCode:** `A`
*   **Cond (tourFinished):**
    *   **condTypeRefId:** `Boolean`
    *   **id:** `tourFinished`
    *   **name:** `tour finished`
    *   **descr:** `finished tour`

#### Incorporation

*   **CondIncorporation (SB-S001 - 00):**
    *   **condRefId:** `SB-S001`
    *   **condIssueNumber:** `00`
    *   **documentIncorporation:**
        *   **refs:**
            *   **dmRef:**
                *   **dmRefIdent:**
                    *   **dmCode:**
                        *   **modelIdentCode:** `S1000DBIKE`
                        *   **systemDiffCode:** `AAA`
                        *   **systemCode:** `DA0`
                        *   **subSystemCode:** `2`
                        *   **subSubSystemCode:** `0`
                        *   **assyCode:** `00`
                        *   **disassyCode:** `00`
                        *   **disassyCodeVariant:** `AA`
                        *   **infoCode:** `520`
                        *   **infoCodeVariant:** `A`
                        *   **itemLocationCode:** `A`
        *   **incorporationStatus:**
            *   **incorporationStatus:** `incorporated`
            *   **year:** `2007`
            *   **month:** `07`
            *   **day:** `31`
*   **CondIncorporation (SB-S001 - 01):**
    *   **condRefId:** `SB-S001`
    *   **condIssueNumber:** `01`
    *   **documentIncorporation:**
        *   **refs:**
            *   **dmRef:**
                *   **dmRefIdent:**
                    *   **dmCode:**
                        *   **modelIdentCode:** `S1000DBIKE`
                        *   **systemDiffCode:** `AAA`
                        *   **systemCode:** `DA0`
                        *   **subSystemCode:** `2`
                        *   **subSubSystemCode:** `0`
                        *   **assyCode:** `00`
                        *   **disassyCode:** `00`
                        *   **disassyCodeVariant:** `AA`
                        *   **infoCode:** `520`
                        *   **infoCodeVariant:** `A`
                        *   **itemLocationCode:** `A`
        *   **incorporationStatus:**
            *   **incorporationStatus:** `noeffect`