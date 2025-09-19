# DMC-S1000DBIKE-AAA-DA4-10-00-00AA-414A-A_008-00_EN-US
## Introduction
The following is a conversion of the provided XML file to a markdown format for better readability and understanding.

## Ident and Status Section
This section contains information about the identification and status of the document.
### DM Address
The DM address section provides details about the document's identity and location.
#### DM Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** DA4
* **Sub System Code:** 1
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 414
* **Info Code Variant:** A
* **Item Location Code:** A
#### Language and Issue Info
* **Country ISO Code:** US
* **Language ISO Code:** en
* **Issue Number:** 008
* **In Work:** 00

### DM Address Items
This section contains additional information about the document.
#### Issue Date
* **Year:** 2024
* **Month:** 06
* **Day:** 19
#### DM Title
* **Tech Name:** Drive train
* **Info Name:** Correlated fault

## DM Status
The DM status section provides details about the document's current state and restrictions.
### Issue Type
* **Issue Type:** changed
### Security
* **Security Classification:** 01
* **Commercial Classification:** cc51
* **Caveat:** cv51
### Data Restrictions
This section outlines the restrictions and guidelines for handling the document.
#### Restriction Instructions
* **Data Distribution:** To be made available to all S1000D users.
* **Export Control:**
  + Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted.
  + Storage of this data module is to be at the discretion of the organization.
* **Data Handling:** There are no specific handling instructions for this data module.
* **Data Destruction:** Users may destroy this data module in accordance with their own local procedures.
* **Data Disclosure:** There are no dissemination limitations that apply to this data module.

#### Restriction Info
* **Copyright:**
  + Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
  + Publishers:
    - Aerospace, Security and Defence Industries Association of Europe
    - Aerospace Industries Association of America
    - ATA e-Business Program
  + Limitations of liability:
    - This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
    - Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
    - Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* **Policy Statement:** S1000D-SC-2016-017-002-00 Steering Committee TOR
* **Data Conds:** There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Responsible Partner Company
* **Enterprise Code:** B6865
* **Enterprise Name:** AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Originator
* **Enterprise Code:** B6865
* **Enterprise Name:** AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Applic Cross Ref Table Ref
This section contains a reference to another data module.
#### DM Ref Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** D00
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 00W
* **Info Code Variant:** A
* **Item Location Code:** D

### Applic
This section describes the application of the document.
#### Display Text
The mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
#### Evaluate
* **And/Or:** and
* **Assert:**
  + **Applic Property Ident:** type
  + **Applic Property Type:** prodattr
  + **Applic Property Values:** Mountain bicycle
* **Evaluate:**
  + **And/Or:** or
  + **Evaluate:**
    - **And/Or:** and
    - **Assert:**
      - **Applic Property Ident:** model
      - **Applic Property Type:** prodattr
      - **Applic Property Values:** Mountain storm
    - **Assert:**
      - **Applic Property Ident:** version
      - **Applic Property Type:** prodattr
      - **Applic Property Values:** Mk1
  + **Evaluate:**
    - **And/Or:** and
    - **Assert:**
      - **Applic Property Ident:** model
      - **Applic Property Type:** prodattr
      - **Applic Property Values:** Brook trekker
    - **Assert:**
      - **Applic Property Ident:** version
      - **Applic Property Type:** prodattr
      - **Applic Property Values:** Mk9

### Tech Standard
This section provides information about the technical standard used in the document.
#### Authority Info and TP
* **Authority Info:** 20010131
* **Tech Pub Base:** Bike book

### Brex DM Ref
This section contains a reference to another data module.
#### DM Ref Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** D00
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 022
* **Info Code Variant:** A
* **Item Location Code:** D

### Quality Assurance
This section provides information about the quality assurance process.
#### First Verification
* **Verification Type:** tabtop

### System Breakdown Code
* **System Breakdown Code:** BY151

### Skill Level
* **Skill Level Code:** sk01

### Reason for Update
* **ID:** rfu_general
* **Update Reason Type:** urt03
* **Simple Para:** S1000D upissued

## Content
This section contains the main content of the document.
### Fault Reporting
This section describes a correlated fault in the system.
#### Correlated Fault
* **ID:** cflt-0001
##### Basic Correlated Faults
* **Bit Message:**
  + **Fault Code:** 100FC01
  + **Fault Description:** The pedal mechanism is jammed
* **Bit Message:**
  + **Fault Code:** 200FC01
  + **Fault Description:** The derailleur is jammed

##### Isolate Detected Fault
* **LRU Item:**
  + **Name:** Bicycle chain
  + **Ident Number:**
    - **Manufacturer Code:** KZ120
    - **Part and Serial Number:**
      - **Part Number:** Tchain-120

##### Remarks
* **Simple Para:** Prepare the derailleur to put transmission chain back on pedal mechanism.