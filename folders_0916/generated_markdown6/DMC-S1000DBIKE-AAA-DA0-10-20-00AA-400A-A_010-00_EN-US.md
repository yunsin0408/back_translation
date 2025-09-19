DMC-S1000DBIKE-AAA-DA0-10-20-00AA-400A-A_010-00_EN-US
==============================================

## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** DA0
* **Sub System Code:** 1
* **Sub Sub System Code:** 0
* **Assy Code:** 20
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 400
* **Info Code Variant:** A
* **Item Location Code:** A
* **Language:**
	+ Country ISO Code: US
	+ Language ISO Code: en
* **Issue Info:**
	+ Issue Number: 010
	+ In Work: 00

#### DM Address Items
* **Issue Date:**
	+ Year: 2024
	+ Month: 06
	+ Day: 19
* **DM Title:**
	+ Tech Name: Front wheel
	+ Info Name: Fault reports and isolation procedures

### DM Status
* **Issue Type:** changed
* **Security:**
	+ Security Classification: 01
	+ Commercial Classification: cc51
	+ Caveat: cv51
* **Data Restrictions:**
	+ Restriction Instructions:
		- Data Distribution: To be made available to all S1000D users.
		- Export Control:
			- Export Registration Stmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- Data Handling: There are no specific handling instructions for this data module.
		- Data Destruction: Users may destroy this data module in accordance with their own local procedures.
		- Data Disclosure: There are no dissemination limitations that apply to this data module.
	+ Restriction Info:
		- Copyright:
			- Copyright Para:  Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
			- Publishers:
				1. Aerospace, Security and Defence Industries Association of Europe
				2. Aerospace Industries Association of America
				3. ATA e-Business Program
			- Limitations of liability:
				1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
				2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
				3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
			- Copyright Para: The details for copyright can be found in the S1000D.
		- Policy:
			- Policy Stmt: 
* **Responsible Organization:**
	+ Enterprise: KZ666
	+ Organization: BSK-TLST
* **Applicability:**
	+ Applicable to all users of this data module.

## Content
### References
* **DM Refs:**
	1. Model Ident Code: S1000DBIKE, System Diff Code: AAA, System Code: DA0, Sub System Code: 1, Sub Sub System Code: 0, Assy Code: 20, Disassy Code: 00, Disassy Code Variant: AA, Info Code: 215, Info Code Variant: A, Item Location Code: A
	2. Model Ident Code: S1000DBIKE, System Diff Code: AAA, System Code: DA0, Sub System Code: 1, Sub Sub System Code: 0, Assy Code: 20, Disassy Code: 00, Disassy Code Variant: AA, Info Code: 921, Info Code Variant: A, Item Location Code: A
	3. Model Ident Code: S1000DBIKE, System Diff Code: AAA, System Code: DA0, Sub System Code: 1, Sub Sub System Code: 0, Assy Code: 20, Disassy Code: 00, Disassy Code Variant: AA, Info Code: 921, Info Code Variant: A, Item Location Code: A

### Fault Isolation
#### Fault Isolation Procedure
* **Fault:** NYCJD04 - Tire does not function correctly
* **Isolation Procedure:**
	1. Preliminary Rqmts:
		- No Conds.
		- Support Equip Descr Group:
			1. Name: Tire pressure gauge, Ident Number: KZ666/BSK-TLST-001-01, Req Quantity: 1 EA
			2. Name: Specialist toolset, Ident Number: KZ666/BSK-TLST-001, Req Quantity: 1 EA
		- No Suplies.
		- No Spares.
		- No Safety Rqmts.
	2. Isolation Main Procedure:
		- **Step 1:** Use the tire pressure gauge (seq-0001) to do a check of the pressure.
			+ Question: What is the tire pressure reading?
			+ Answer:
				1. More than 2700 hPa -> Go to step 2
				2. Between 100 hPa and 2700 hPa -> Go to step 3
				3. Less than 100 hPa -> Go to step 4
		- **Step 2:** Deflate the tire until the pressure is 2700 hPa.
		- **Step 3:** Inflate the tire as given in DM Ref: Model Ident Code: S1000DBIKE, System Diff Code: AAA, System Code: DA0, Sub System Code: 1, Sub Sub System Code: 0, Assy Code: 20, Disassy Code: 00, Disassy Code Variant: AA, Info Code: 215, Info Code Variant: A, Item Location Code: A.
		- **Step 4:** Do a check of the tire for damage.
			+ Question: Is there damage to the tire?
			+ Answer:
				1. Yes -> Go to step 5
				2. No -> Go to step 6
		- **Step 5:** Replace the tire (refer to DM Ref: Model Ident Code: S1000DBIKE, System Diff Code: AAA, System Code: DA0, Sub System Code: 1, Sub Sub System Code: 0, Assy Code: 20, Disassy Code: 00, Disassy Code Variant: AA, Info Code: 921, Info Code Variant: A, Item Location Code: A).
		- **Step 6:** Replace the inner-tube (refer to DM Ref: Model Ident Code: S1000DBIKE, System Diff Code: AAA, System Code: DA0, Sub System Code: 1, Sub Sub System Code: 0, Assy Code: 10, Disassy Code: 00, Disassy Code Variant: AA, Info Code: 921, Info Code Variant: A, Item Location Code: A).
	3. Close Rqmts:
		- No Conds.

Note: EA stands for "each" and represents a unit of measurement for the quantity required.