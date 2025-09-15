DMC-S1000DBIKE-AAA-DA0-10-20-00AA-362B-A_010-00_EN-US
==============================================

### Ident and Status Section

#### DM Address

*   **DM Ident**
    *   Model Ident Code: S1000DBIKE
    *   System Diff Code: AAA
    *   System Code: DA0
    *   Sub System Code: 1
    *   Sub Sub System Code: 0
    *   Assy Code: 20
    *   Disassy Code: 00
    *   Disassy Code Variant: AA
    *   Info Code: 362
    *   Info Code Variant: B
    *   Item Location Code: A
*   **Language**
    *   Country Iso Code: US
    *   Language Iso Code: en
*   **Issue Info**
    *   Issue Number: 010
    *   In Work: 00

#### DM Address Items

*   **Issue Date**
    *   Year: 2024
    *   Month: 06
    *   Day: 19
*   **DM Title**
    *   Tech Name: Tire
    *   Info Name: Check pressure
    *   Info Name Variant: Use pressure gauge

#### DM Status

*   **Issue Type**: changed
*   **Security**
    *   Security Classification: 01
    *   Commercial Classification: cc51
    *   Caveat: cv51
*   **Data Restrictions**
    *   **Restriction Instructions**
        *   Data Distribution: To be made available to all S1000D users.
        *   Export Control:
            *   Export Registration Stmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   Data Handling: There are no specific handling instructions for this data module.
        *   Data Destruction: Users may destroy this data module in accordance with their own local procedures.
        *   Data Disclosure: There are no dissemination limitations that apply to this data module.
    *   **Restriction Info**
        *   **Copyright**
            *   Copyright Para:
                *   Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   Publishers:
                *   Aerospace, Security and Defence Industries Association of Europe
                *   Aerospace Industries Association of America
                *   ATA e-Business Program
            *   Limitations of Liability:
                *   This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                *   Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
                *   Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
            *   Copyright Details: The details for copyright can be found in the S1000D Specification.
        *   Policy Statement: S1000D-SC-2016-017-002-00 Steering Committee TOR
        *   Data Conds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company

*   Enterprise Code: B6865
*   Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Originator

*   Enterprise Code: B6865
*   Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Applic Cross Ref Table Ref

*   **DM Ref**
    *   Model Ident Code: S1000DBIKE
    *   System Diff Code: AAA
    *   System Code: D00
    *   Sub System Code: 0
    *   Sub Sub System Code: 0
    *   Assy Code: 00
    *   Disassy Code: 00
    *   Disassy Code Variant: AA
    *   Info Code: 00W
    *   Info Code Variant: A
    *   Item Location Code: D

#### Applic

*   **Display Text**
    *   Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   Evaluate:
    +   Assert:
        -   Applic Property Ident: type
        -   Applic Property Type: prodattr
        -   Applic Property Values: Mountain bicycle
    +   Evaluate (or):
        -   Evaluate (and):
            -   Assert:
                -   Applic Property Ident: model
                -   Applic Property Type: prodattr
                -   Applic Property Values: Mountain storm
            -   Assert:
                -   Applic Property Ident: version
                -   Applic Property Type: prodattr
                -   Applic Property Values: Mk1
        -   Evaluate (and):
            -   Assert:
                -   Applic Property Ident: model
                -   Applic Property Type: prodattr
                -   Applic Property Values: Brook trekker
            -   Assert:
                -   Applic Property Ident: version
                -   Applic Property Type: prodattr
                -   Applic Property Values: Mk9

#### Tech Info

No technical information is provided in this section.

### Content

#### Refs

*   **DM Ref**
    *   Model Ident Code: S1000DBIKE
    *   System Diff Code: AAA
    *   System Code: DA0
    *   Sub System Code: 1
    *   Sub Sub System Code: 0
    *   Assy Code: 20
    *   Disassy Code: 00
    *   Disassy Code Variant: AA
    *   Info Code: 215
    *   Info Code Variant: A
    *   Item Location Code: A
*   **DM Ref**
    *   Model Ident Code: S1000DBIKE
    *   System Diff Code: AAA
    *   System Code: DA0
    *   Sub System Code: 1
    *   Sub Sub System Code: 0
    *   Assy Code: 10
    *   Disassy Code: 00
    *   Disassy Code Variant: AA
    *   Info Code: 921
    *   Info Code Variant: A
    *   Item Location Code: A

#### Procedure

*   **Preliminary Rqmts**
    +   No Conds
    +   **Person**
        -   Man: A
        -   Person Category: Basic user
        -   Trade: Operator
        -   Estimated Time:
            -   Unit of Measure: h
            -   Value: 0.3
    +   **Support Equip Descr Group**
        -   Support Equip Descr:
            -   Id: seq-0003
            -   Name: Tire pressure gauge
            -   Ident Number:
                -   Manufacturer Code: KZ666
                -   Part and Serial Number:
                    -   Part Number: BSK-TLST-001-01
            -   Req Quantity:
                -   Unit of Measure: EA
                -   Value: 1
    +   No Supplies
    +   No Spares
    +   No Safety

*   **Main Procedure**
    1.  Locate the valve stem of tire.
    2.  Use the tire pressure gauge to check the tire pressure.
    3.  Tire pressure should be between 2000 hPa and 2700 hPa.
        *   If tire pressure is less than 2000 hPa, inflate tire. Refer to the relevant DM Ref for instructions.
        *   If the tire cannot maintain pressure or the tire pressure is greater than 2700 hPa, replace the inner tube. Refer to the relevant DM Ref for instructions.

*   **Close Rqmts**
    +   No Conds