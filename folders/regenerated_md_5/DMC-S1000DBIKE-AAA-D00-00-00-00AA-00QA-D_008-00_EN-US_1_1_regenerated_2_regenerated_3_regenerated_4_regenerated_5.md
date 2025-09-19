# DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US_1_1 - Mountain Bicycle Conditions Cross-Reference Table

## DM Title

*   **Tech Name:** Mountain bicycle
*   **Info Name:** Conditions cross-reference table

## DM Ident

*   **Model Ident Code:** S1000DBIKE
*   **System Diff Code:** AAA
*   **System Code:** D00
*   **Sub System Code:** 0
*   **Sub SubSystem Code:** 0
*   **Assy Code:** 00
*   **Disassy Code:** 00
*   **Disassy Code Variant:** AA
*   **Info Code:** 00Q
*   **Info Code Variant:** A
*   **Item Location Code:** D
*   **Language:**
    *   **Country Iso Code:** US
    *   **Language Iso Code:** en
*   **Issue Info:**
    *   **Issue Number:** 008
    *   **In Work:** 00
*   **Issue Date:**
    *   **Year:** 2024
    *   **Month:** 06
    *   **Day:** 19

## DM Status

*   **Issue Type:** changed
*   **Security:**
    *   **Security Classification:** 01
    *   **Data Restrictions:**
        *   **Restriction Instructions:**
            *   **Export Registration Stmt:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
            *   **Data Handling:** There are no specific handling instructions for this data module.
            *   **Data Destruction:** Users may destroy this data module in accordance with their own local procedures.
            *   **Data Disclosure:** There are no dissemination limitations that apply to this data module.
        *   **Restriction Info:**
            *   **Copyright:** Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   **Publishers:**
                *   Aerospace, Security and Defence Industries Association of Europe
                *   Aerospace Industries Association of America
                *   ATA e-Business Program
            *   **Limitations of Liability:**
                *   **Limitation:** This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                *   **Limitation:** Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability.
*   **Responsible Department:**
    *   **Value:** Engineering

## Dependencies

*   **For Cond Values:** POST-001
*   **Dependency Test:** A-1

## Content

### Referenced Applic Group

#### Applic A_1

*   **Assert:**
    *   **Applic Property Type:** condition
    *   **Applic Property Ident:** SB-S001
    *   **Applic Property Values:** POST-001~POST-999

#### Applic A_2

*   **Evaluate:**
    *   **And Or:** and
*   **Assert 1:**
    *   **Applic Property Type:** condition
    *   **Applic Property Ident:** SB-S001
    *   **Applic Property Values:** POST-001~POST-999
*   **Assert 2:**
    *   **Applic Property Type:** condition
    *   **Applic Property Ident:** SB-S009
    *   **Applic Property Values:** PRE

### Cond Cross Reference Table

#### Cond Type List

*   **Cond Type SB:**
    *   **Id:** SB
    *   **Value Data Type:** string
    *   **Name:** Service bulletin
    *   **Descr:** Generic service bulletin type
    *   **Enumeration:** PRE
*   **Cond Type Boolean:**
    *   **Id:** Boolean
    *   **Name:** generic Boolean condition
    *   **Descr:** Boolean condition
    *   **Enumeration:** True|False

#### Cond List

*   **Cond SB_S001:**
    *   **Cond Type Ref Id:** SB
    *   **Id:** SB-S001
    *   **Name:** Service bulletin 1
    *   **Descr:** Service bulletin description 1
    *   **Refs:**
        *   **Dm Ref:**
            *   **Dm Ident:**
                *   **Model Ident Code:** S1000DBIKE
                *   **System Diff Code:** AAA
                *   **System Code:** DA0
                *   **Sub System Code:** 2
                *   **Sub SubSystem Code:** 0
                *   **Assy Code:** 00
                *   **Disassy Code:** 00
                *   **Disassy Code Variant:** AA
                *   **Info Code:** 520
                *   **Info Code Variant:** A
                *   **Item Location Code:** A
*   **Cond SB_S009:**
    *   **Cond Type Ref Id:** SB
    *   **Id:** SB-S009
    *   **Name:** Service bulletin 9
    *   **Descr:** Service bulletin description 9
    *   **Refs:**
        *   **Dm Ref:**
            *   **Dm Ident:**
                *   **Model Ident Code:** S1000DBIKE
                *   **System Diff Code:** AAA
                *   **System Code:** DA0
                *   **Sub System Code:** 2
                *   **Sub SubSystem Code:** 0
                *   **Assy Code:** 00
                *   **Disassy Code:** 00
                *   **Disassy Code Variant:** AA
                *   **Info Code:** 520
                *   **Info Code Variant:** A
                *   **Item Location Code:** A

#### Cond Incorporation List

*   **Cond Incorporation SB_S001_00:**
    *   **Cond Ref Id:** SB-S001
    *   **Incorporation Status:**
        *   **Incorporation Status:** noeffect
*   **Cond Incorporation SB_S001_00:**
    *   **Cond Ref Id:** SB-S001
    *   **Incorporation Status:**
        *   **Incorporation Status:** noeffect