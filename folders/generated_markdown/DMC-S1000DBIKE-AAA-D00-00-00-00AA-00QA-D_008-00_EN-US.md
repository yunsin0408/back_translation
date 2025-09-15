# DMC-S1000DBIKE-AAA-D00-00-00-00AA-00QA-D_008-00_EN-US
## Introduction
The following is a conversion of the provided XML file to a markdown format.

### Ident and Status Section
#### DM Address
##### DM Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** D00
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 00Q
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:**
	+ Country ISO Code: US
	+ Language ISO Code: en
* **Issue Info:**
	+ Issue Number: 008
	+ In Work: 00

##### DM Address Items
* **Issue Date:**
	+ Year: 2024
	+ Month: 06
	+ Day: 19
* **DM Title:**
	+ Tech Name: Mountain bicycle
	+ Info Name: Conditions cross-reference table

#### DM Status
* **Issue Type:** changed
* **Security:**
	+ Security Classification: 01
* **Data Restrictions:**
	+ Restriction Instructions:
		- Data Distribution: To be made available to all S1000D users.
		- Export Control:
			- Export Registration Statement: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- Data Handling: There are no specific handling instructions for this data module.
		- Data Destruction: Users may destroy this data module in accordance with their own local procedures.
		- Data Disclosure: There are no dissemination limitations that apply to this data module.
	+ Restriction Info:
		- Copyright:
			- Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
			- Publishers:
				1. Aerospace, Security and Defence Industries Association of Europe
				2. Aerospace Industries Association of America
				3. ATA e-Business Program
			- Limitations of liability:
				1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
				2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
				3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
			- Copyright details can be found in the S1000D Specification.
		- Policy Statement: S1000D-SC-2016-017-002-00 Steering Committee TOR
		- Data Conds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Content
#### Referenced Applic Group
* **Applic ID:** A-1
	+ Display Text: SB 1
	+ Assert:
		- Applic Property Type: condition
		- Applic Property Ident: SB-S001
		- Applic Property Values: POST-001~POST-999
* **Applic ID:** A-2
	+ Display Text: POST SB 1 AND PRE SB 9
	+ Evaluate:
		- And/Or: and
		- Assert:
			- Applic Property Type: condition
			- Applic Property Ident: SB-S001
			- Applic Property Values: POST-001~POST-999
		- Assert:
			- Applic Property Type: condition
			- Applic Property Ident: SB-S009
			- Applic Property Values: PRE

#### Cond Cross Ref Table
##### Cond Type List
* **Cond Type ID:** SB
	+ Value Data Type: string
	+ Name: Service bulletin
	+ Descr: Generic service bulletin type
	+ Enumeration:
		- Applic Property Values: PRE
		- Applic Property Values: POST-001~POST-999
* **Cond Type ID:** Boolean
	+ Value Data Type: string
	+ Name: generic Boolean condition
	+ Descr: Boolean condition
	+ Enumeration:
		- Applic Property Values: True|False

##### Cond List
* **Cond ID:** SB-S001
	+ Name: Service bulletin S001 - Chain guard
	+ Descr: Service bulletin S001 for the installation of the chain guard
	+ Refs:
		- DM Ref:
			- DM Ref Ident:
				- Model Ident Code: S1000DBIKE
				- System Diff Code: AAA
				- System Code: DA0
				- Sub System Code: 2
				- Sub Sub System Code: 0
				- Assy Code: 00
				- Disassy Code: 00
				- Disassy Code Variant: AA
				- Info Code: 520
				- Info Code Variant: A
				- Item Location Code: A
	+ Dependency:
		- For Cond Values: POST-001
		- Dependency Test: A-1
* **Cond ID:** SB-S009
	+ Name: Service bulletin 9 - Chain guard (2)
	+ Descr: Service bulletin 9 for the installation of the chain guard (2)
	+ Refs:
		- DM Ref:
			- DM Ref Ident:
				- Model Ident Code: S1000DBIKE
				- System Diff Code: AAA
				- System Code: DA0
				- Sub System Code: 2
				- Sub Sub System Code: 0
				- Assy Code: 01
				- Disassy Code: 00
				- Disassy Code Variant: AA
				- Info Code: 520
				- Info Code Variant: A
				- Item Location Code: A
* **Cond ID:** tourFinished
	+ Name: tour finished
	+ Descr: finished tour

##### Incorporation
* **Cond Ref ID:** SB-S001
	+ Cond Issue Number: 00
	+ Document Incorporation:
		- Refs:
			- DM Ref:
				- DM Ref Ident:
					- Model Ident Code: S1000DBIKE
					- System Diff Code: AAA
					- System Code: DA0
					- Sub System Code: 2
					- Sub Sub System Code: 0
					- Assy Code: 00
					- Disassy Code: 00
					- Disassy Code Variant: AA
					- Info Code: 520
					- Info Code Variant: A
					- Item Location Code: A
		- Incorporation Status:
			- Incorporation Status: incorporated
			- Year: 2007
			- Month: 07
			- Day: 31
* **Cond Ref ID:** SB-S001
	+ Cond Issue Number: 01
	+ Document Incorporation:
		- Refs:
			- DM Ref:
				- DM Ref Ident:
					- Model Ident Code: S1000DBIKE
					- System Diff Code: AAA
					- System Code: DA0
					- Sub System Code: 2
					- Sub Sub System Code: 0
					- Assy Code: 00
					- Disassy Code: 00
					- Disassy Code Variant: AA
					- Info Code: 520
					- Info Code Variant: A
					- Item Location Code: A
		- Incorporation Status:
			- Incorporation Status: noeffect