# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US
## Introduction
The following document provides guidelines for the conversion of XML documents to markdown format.

### Ident and Status Section
#### DM Address
##### DM Ident
* Model Ident Code: `S1000DBIKE`
* System Diff Code: `AAA`
* System Code: `DA0`
* Sub System Code: `1`
* Sub Sub System Code: `0`
* Assy Code: `20`
* Disassy Code: `00`
* Disassy Code Variant: `AA`
* Info Code: `400`
* Info Code Variant: `A`
* Item Location Code: `A`

##### Language
* Country Iso Code: `US`
* Language Iso Code: `en`

##### Issue Info
* Issue Number: `010`
* In Work: `00`

#### DM Address Items
##### Issue Date
* Year: `2024`
* Month: `06`
* Day: `19`

##### DM Title
* Tech Name: `Front wheel`
* Info Name: `Fault reports and isolation procedures`

### DM Status
#### Issue Type
* Changed

#### Security
* Security Classification: `01`
* Commercial Classification: `cc51`
* Caveat: `cv51`

#### Data Restrictions
##### Restriction Instructions
* Data Distribution: `To be made available to all S1000D users.`
* Export Control:
  + Export Registration Stmt: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
* Data Handling: `There are no specific handling instructions for this data module.`
* Data Destruction: `Users may destroy this data module in accordance with their own local procedures.`
* Data Disclosure: `There are no dissemination limitations that apply to this data module.`

##### Restriction Info
* Copyright:
  + Copyright Para: `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
  + Publishers:
    * Aerospace, Security and Defence Industries Association of Europe
    * Aerospace Industries Association of America
    * ATA e-Business Program
  + Limitations of Liability:
    * This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
    * Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
    * Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* Policy Statement: `S1000D-SC-2016-017-002-00 Steering Committee TOR`
* Data Conds: `There are no known conditions that would change the data restrictions for this data module.`

#### Responsible Organizations
* Enterprise: Not specified
* Organization: Not specified

### Content
#### References
The following references are applicable to this document:
1. `DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US`
2. `DMC-S1000DBIKE-AAA-DA0-10-20-00AA-215-A_010-00_EN-US`
3. `DMC-S1000DBIKE-AAA-DA0-10-20-00AA-921-A_010-00_EN-US`

#### Fault Isolation
##### Fault Isolation Procedure
* Fault: `NYCJD04`
* Fault Description: `Tire does not function correctly`

###### Preliminary Requirements
* Required Condition Group: Not applicable
* Required Support Equipment:
  + Tire pressure gauge (KZ666, BSK-TLST-001-01) - 1 EA
  + Specialist toolset (KZ666, BSK-TLST-001) - 1 EA
* Required Supplies: Not applicable
* Required Spares: Not applicable
* Required Safety: Not applicable

###### Isolation Main Procedure
1. **Step 1**: Use the tire pressure gauge to check the pressure.
	* What is the tire pressure reading?
	+ More than 2700 hPa: Go to Step 2
	+ Between 100 hPa and 2700 hPa: Go to Step 3
	+ Less than 100 hPa: Go to Step 4
2. **Step 2**: Deflate the tire until the pressure is 2700 hPa.
3. **Step 3**: Inflate the tire as given in `DMC-S1000DBIKE-AAA-DA0-10-20-00AA-215-A_010-00_EN-US`.
4. **Step 4**: Check the tire for damage.
	* Is there damage to the tire?
	+ Yes: Go to Step 5
	+ No: Go to Step 6
5. **Step 5**: Replace the tire (refer to `DMC-S1000DBIKE-AAA-DA0-10-20-00AA-921-A_010-00_EN-US`).
6. **Step 6**: Replace the inner-tube (refer to `DMC-S1000DBIKE-AAA-DA0-10-10-00AA-921-A_010-00_EN-US`).

###### Close Requirements
* Required Condition Group: Not applicable

Note: This markdown document is a direct conversion of the provided XML file and may require further formatting for better readability.