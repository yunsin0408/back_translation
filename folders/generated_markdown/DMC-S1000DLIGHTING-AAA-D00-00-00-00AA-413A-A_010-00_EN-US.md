# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-413A-A_010-00_EN-US
## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code:** S1000DLIGHTING
* **System Diff Code:** AAA
* **System Code:** D00
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 413
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
	+ Tech Name: Lights
	+ Info Name: Observed fault

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
			- Limitations of Liability:
				1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
				2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
				3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
			- Copyright Details: The details for copyright can be found in the S1000D Specification.
		- Policy Statement: S1000D-SC-2016-017-002-00 Steering Committee TOR
		- Data Conditions: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

## Content
### References
* **DM Refs:**
	1. Model Ident Code: S1000DLIGHTING
		System Diff Code: AAA
		System Code: D00
		Sub System Code: 0
		Sub Sub System Code: 0
		Assy Code: 00
		Disassy Code: 02
		Disassy Code Variant: AA
		Info Code: 0A5
		Info Code Variant: A
		Item Location Code: A
	2. Model Ident Code: S1000DLIGHTING
		System Diff Code: AAA
		System Code: D00
		Sub System Code: 0
		Sub Sub System Code: 0
		Assy Code: 00
		Disassy Code: 01
		Disassy Code Variant: AA
		Info Code: 0A4
		Info Code Variant: A
		Item Location Code: A

### Warnings and Cautions Ref
* **Warning Refs:**
	1. Warning Ident Number: warning-001
		Model Ident Code: S1000DLIGHTING
		System Diff Code: AAA
		System Code: D00
		Sub System Code: 0
		Sub Sub System Code: 0
		Assy Code: 00
		Disassy Code: 01
		Disassy Code Variant: AA
		Info Code: 0A4
		Info Code Variant: A
		Item Location Code: A
	2. Warning Ident Number: warning-002
		Model Ident Code: S1000DLIGHTING
		System Diff Code: AAA
		System Code: D00
		Sub System Code: 0
		Sub Sub System Code: 0
		Assy Code: 00
		Disassy Code: 01
		Disassy Code Variant: AA
		Info Code: 0A4
		Info Code Variant: A
		Item Location Code: A
* **Caution Refs:**
	1. Caution Ident Number: caution-001
		Model Ident Code: S1000DLIGHTING
		System Diff Code: AAA
		System Code: D00
		Sub System Code: 0
		Sub Sub System Code: 0
		Assy Code: 00
		Disassy Code: 02
		Disassy Code Variant: AA
		Info Code: 0A5
		Info Code Variant: A
		Item Location Code: A

### Fault Reporting
#### Preliminary Requirements
* **No Conditions**
* **No Support Equipment**
* **No Supplies**
* **No Spares**
* **Safety Requirements:**
	+ Caution Refs: c001
	+ Warning Refs: w001, w002

#### Observed Fault
* **Fault Code:** NYCJD02
* **Fault Description:** The lights are set to the dim position.
* **Context and Isolation Info:**
	+ Fault Context: During use or maintenance
	+ Isolation Info:
		- LRU Item:
			- Name: Bulb
			- Ident Number:
				1. Manufacturer Code: KZ111
				2. Part and Serial Number:
					- Part Number: LiRUs-L1-11
			- Fault Isolation Test:
				+ Test Type: Operation
				+ Test Code: O-001
				+ Test Description:
					- Test Name: Test the bulbs
				+ Test Parameters:
					- From: 1
					- To: 1
					- Unit of Measure: Days
				+ Test Procedure:
					1. DM Ref:
						- Model Ident Code: S1000DLIGHTING
						System Diff Code: AAA
						System Code: D00
						Sub System Code: 0
						Sub Sub System Code: 0
						Assy Code: 00
						Disassy Code: 00
						Disassy Code Variant: AA
						Info Code: 341
						Info Code Variant: A
						Item Location Code: A
			- Repair:
				1. DM Ref:
					- Model Ident Code: S1000DLIGHTING
					System Diff Code: AAA
					System Code: D00
					Sub System Code: 0
					Sub Sub System Code: 0
					Assy Code: 00
					Disassy Code: 00
					Disassy Code Variant: AA
					Info Code: 921
					Info Code Variant: A
					Item Location Code: A

* **Remarks:** This is the data module you would visit when you notice that the lights do not operate correctly.