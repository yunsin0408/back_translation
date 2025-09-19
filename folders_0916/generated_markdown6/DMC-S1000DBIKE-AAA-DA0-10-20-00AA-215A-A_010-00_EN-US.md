# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-215A-A_010-00_EN-US
## Ident and Status Section
### DM Address
The `dmAddress` section contains the following information:
* **DM Ident**: 
  + Model Ident Code: S1000DBIKE
  + System Diff Code: AAA
  + System Code: DA0
  + Sub System Code: 1
  + Sub Sub System Code: 0
  + Assy Code: 20
  + Disassy Code: 00
  + Disassy Code Variant: AA
  + Info Code: 215
  + Info Code Variant: A
  + Item Location Code: A
* **Language**: 
  + Country Iso Code: US
  + Language Iso Code: en
* **Issue Info**: 
  + Issue Number: 010
  + In Work: 00

### DM Address Items
The `dmAddressItems` section contains the following information:
* **Issue Date**: 
  + Year: 2024
  + Month: 06
  + Day: 19
* **DM Title**: 
  + Tech Name: Tire
  + Info Name: Fill with air

### DM Status
The `dmStatus` section contains the following information:
* **Issue Type**: changed
* **Security**: 
  + Security Classification: 01
  + Commercial Classification: cc51
  + Caveat: cv51
* **Data Restrictions**:
  + Restriction Instructions:
    - Data Distribution: To be made available to all S1000D users.
    - Export Control:
      * Export Registration Stmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
    - Data Handling: There are no specific handling instructions for this data module.
    - Data Destruction: Users may destroy this data module in accordance with their own local procedures.
    - Data Disclosure: There are no dissemination limitations that apply to this data module.
  + Restriction Info:
    - Copyright:
      * Copyright Para: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
      * Publishers:
        * Aerospace, Security and Defence Industries Association of Europe
        * Aerospace Industries Association of America
        * ATA e-Business Program
      * Limitations of liability:
        * This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
        * Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
        * Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
      * Copyright details can be found in the S1000D Specification.
    - Policy Statement: S1000D-SC-2016-017-002-00 Steering Committee TOR
    - Data Conds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Responsible Partner Company and Originator
* **Responsible Partner Company**: 
  + Enterprise Code: B6865
  + Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
* **Originator**: 
  + Enterprise Code: B6865
  + Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Applic Cross Ref Table Ref and Applic
The `applicCrossRefTableRef` section contains a reference to another data module:
* **DM Ref Ident**: 
  + Model Ident Code: S1000DBIKE
  + System Diff Code: AAA
  + System Code: D00
  + Sub System Code: 0
  + Sub Sub System Code: 0
  + Assy Code: 00
  + Disassy Code: 00
  + Disassy Code Variant: AA
  + Info Code: 00W
  + Info Code Variant: A
  + Item Location Code: D

The `applic` section contains the following information:
* **Display Text**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Evaluate**:
  * Assert Applic Property Ident: type, Applic Property Type: prodattr, Applic Property Values: Mountain bicycle
  * Evaluate And Or: and
    - Assert Applic Property Ident: model, Applic Property Type: prodattr, Applic Property Values: Mountain storm
    - Assert Applic Property Ident: version, Applic Property Type: prodattr, Applic Property Values: Mk1
  * Evaluate And Or: or
    - Assert Applic Property Ident: model, Applic Property Type: prodattr, Applic Property Values: Brook trekker
    - Assert Applic Property Ident: version, Applic Property Type: prodattr, Applic Property Values: Mk9

### Tech Standard and BrexDm Ref
The `techStandard` section contains the following information:
* **Authority Info And Tp**: 
  + Authority Info: 20010131
  + Tech Pub Base: Bike book
* **Authority Exceptions**:
* **Authority Notes**:

The `brexDmRef` section contains a reference to another data module:
* **DM Ref Ident**: 
  + Model Ident Code: S1000DBIKE
  + System Diff Code: AAA
  + System Code: D00
  + Sub System Code: 0
  + Sub Sub System Code: 0
  + Assy Code: 00
  + Disassy Code: 00
  + Disassy Code Variant: AA
  + Info Code: 00W
  + Info Code Variant: A
  + Item Location Code: D

### Quality and Reason
* **Quality**:
* **Reason**:

## Content
The `content` section contains the following information:
### Preliminary Requirements
The `preliminaryRqmts` section contains the following information:
* **Req Conds**: No conditions required.
* **Req Persons**:
  + Person: A, Person Category Code: Basic user, Trade: Operator
* **Req Support Equips**:
  | Name | Ident Number | Req Quantity |
  | --- | --- | --- |
  | Specialist toolset | KZ666 BSK-TLST-001 | 1 EA |
  | Foot pump | KZ666 BSK-TLST-001-05 | 1 EA |
  | Tire pressure gauge | KZ666 BSK-TLST-001-01 | 1 EA |
* **Req Supplies**: No supplies required.
* **Req Spares**: No spares required.
* **Req Safety**: No safety requirements.

### Main Procedure
The `mainProcedure` section contains the following steps:
1. Ensure bicycle is on the repair stand.
2. Locate the deflated tire.
3. Attach the outlet valve of the foot pump to the valve of the deflated tire.
4. Inflate the tire.
   * Operate the foot pump to pump air into the tire.
   * Check tire pressure.

### Close Requirements
The `closeRqmts` section contains the following information:
* **Req Conds**: No conditions required.

This document follows the structure and content of the provided XML file, using markdown formatting for readability.