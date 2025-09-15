DMC-S1000DBIKE-AAA-D00-00-00-00AA-00MA-D_001-00_EN-US
=============================================

### Ident and Status Section
The ident and status section contains information about the data module's identification and status.

#### DM Address
The dm address section contains the following information:
* **DM Ident**: 
  + Model Ident Code: `S1000DBIKE`
  + System Diff Code: `AAA`
  + System Code: `D00`
  + Sub System Code: `0`
  + Sub Sub System Code: `0`
  + Assy Code: `00`
  + Disassy Code: `00`
  + Disassy Code Variant: `AA`
  + Info Code: `00M`
  + Info Code Variant: `A`
  + Item Location Code: `D`
* **Language**: 
  + Language Iso Code: `en`
  + Country Iso Code: `US`
* **Issue Info**: 
  + Issue Number: `001`
  + In Work: `00`

#### DM Address Items
The dm address items section contains the following information:
* **Issue Date**: 
  + Year: `2024`
  + Month: `06`
  + Day: `19`
* **DM Title**: 
  + Tech Name: `Mountain bicycle`
  + Info Name: `Supplies - List of requirements common information repository`

#### DM Status
The dm status section contains the following information:
* **Issue Type**: `new`
* **Security**: 
  + Security Classification: `01`
  + Commercial Classification: `cc51`
  + Caveat: `cv51`
* **Data Restrictions**:
  + **Restriction Instructions**:
    - Data Distribution: `To be made available to all S1000D users.`
    - Export Control: 
      * Export Registration Stmt: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
    - Data Handling: `There are no specific handling instructions for this data module.`
    - Data Destruction: `Users may destroy this data module in accordance with their own local procedures.`
    - Data Disclosure: `There are no dissemination limitations that apply to this data module.`
  + **Restriction Info**:
    - **Copyright**:
      * Copyright Para: `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
      * Publishers: 
        * Aerospace, Security and Defence Industries Association of Europe
        * Aerospace Industries Association of America
        * ATA e-Business Program
      * Limitations of Liability:
        * This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
        * Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
        * Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
    - Policy Statement: `S1000D-SC-2016-017-002-00 Steering Committee TOR`
    - Data Conds: `There are no known conditions that would change the data restrictions for, or security classification of, this data module.`
* **Responsible Partner Company**:
  + Enterprise Code: `B6865`
  + Enterprise Name: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`
* **Originator**:
  + Enterprise Code: `B6865`
  + Enterprise Name: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`
* **Applic Cross Ref Table Ref**:
  + DM Ref Ident:
    - Model Ident Code: `S1000DBIKE`
    - System Diff Code: `AAA`
    - System Code: `D00`
    - Sub System Code: `0`
    - Sub Sub System Code: `0`
    - Assy Code: `00`
    - Disassy Code: `00`
    - Disassy Code Variant: `AA`
    - Info Code: `00W`
    - Info Code Variant: `A`
    - Item Location Code: `D`
* **Applic**:
  + Display Text: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)`
  + Evaluate:
    * And Or: `and`
    * Assert:
      - Applic Property Ident: `type`
      - Applic Property Type: `prodattr`
      - Applic Property Values: `Mountain bicycle`
    * Evaluate:
      - And Or: `or`
      - Evaluate:
        * And Or: `and`
        * Assert:
          - Applic Property Ident: `model`
          - Applic Property Type: `prodattr`
          - Applic Property Values: `Mountain storm`
          - Applic Property Ident: `version`
          - Applic Property Type: `prodattr`
          - Applic Property Values: `Mk1`
          - Applic Property Ident: `versrank`
          - Applic Property Type: `prodattr`
          - Applic Property Values: `1~3`
      - Evaluate:
        * And Or: `and`
        * Assert:
          - Applic Property Ident: `model`
          - Applic Property Type: `prodattr`
          - Applic Property Values: `Brook trekker`
          - Applic Property Ident: `version`
          - Applic Property Type: `prodattr`
          - Applic Property Values: `Mk9`
          - Applic Property Ident: `versrank`
          - Applic Property Type: `prodattr`
          - Applic Property Values: `1~3`
* **Tech Status**:
  Not available in the provided XML.
* **Brethren List**:
  Not available in the provided XML.

### Content
The content section contains information about the data module's content.

#### Common Repository
The common repository section contains a supply request repository with the following information:

* **Supply Rqmt Spec**:
  + Id: `supr-0001`
  + Supply Rqmt Ident:
    - Material Category: `05`
    - Supply Rqmt Number: `EU-OIL3212`
  + Supply Rqmt Status:
    - Supply Rqmt Status Value: `superseded`
    - Supply Rqmt Ref:
      - Supply Rqmt Number: `EU-OIL3212-1`
  + Supply Rqmt Alts:
    * Supply Rqmt:
      - Id: `SPEC-0007`
      - Supply Rqmt Alt Ident:
        * Id: `SPEC-0002`
        * Material Category: `05`
        * Supply Rqmt Number: `EU-OIL3212`
        * Vendor Flag: `0`
      - Supply Set Group:
        * Supply Set:
          - Supply Ref:
            * Supply Number: `BKO200`
            * Supply Number Type: `sp01`
          - Supply Ref:
            * Supply Number: `OIL135`
            * Supply Number Type: `sp01`
      - Supply Rqmt Alt Status:
        * Authorization Status:
          * Authorization Status Date: `20100801`
          * Value: `REACH banned`
      - Name: `OIL FOR BIKE`
      - Safety Category:
        * Safety Category Value: `C`
      - Usage: `removal of strongly fixed parts`

* **Supply Rqmt Spec**:
  + Id: `supr-0002`
  + Supply Rqmt Ident:
    - Material Category: `05`
    - Supply Rqmt Number: `EU-OIL3212-1`
  + Supply Rqmt Alts:
    * Supply Rqmt:
      - Supply Rqmt Alt Ident:
        * Material Category: `05`
        * Supply Rqmt Number: `EU-OIL3212-1`
        * Vendor Flag: `0`
      - Supply Set Group:
        * Supply Set:
          - Supply Ref:
            * Supply Number: `BKO2000`
            * Supply Number Type: `sp01`
          - Supply Ref:
            * Supply Number: `OIL1355`
            * Supply Number Type: `sp01`
      - Name: `OIL FOR BIKE`
      - Safety Category:
        * Safety Category Value: `C`
      - Usage: `removal of strongly fixed parts`

* **Supply Rqmt Spec**:
  + Id: `inv0105029-`
  + Supply Rqmt Ident:
    - Id: `SPEC-0004`
    - Material Category: `05`
    - Supply Rqmt Number: `029`
  + Supply Rqmt Alts:
    * Supply Rqmt:
      - Id: `SPEC-0001`
      - Supply Rqmt Alt Ident:
        * Material Category: `05`
        * Supply Rqmt Number: `029`
        * Vendor Flag: `0`
      - Supply Set Group:
        * Id: `SPEC-0006`
        * Supply Set:
          - Id: `SPEC-0005`
          - Supply Ref:
            * Supply Number: `BSB-DUROFIX_FIXATIF_UW_SPECIAL`
            * Supply Number Type: `sp01`
          - Supply Ref:
            * Supply Number: `BSB-DUROFIX_FIXATIF_UW`
            * Supply Number Type: `sp01`
      - Name: `FIXATIVE FOR PLACARD INSTALLATION`
      - Safety Category:
        * Safety Category Value: `C`
      - Usage: `IMMERSION OF BSB LABEL`