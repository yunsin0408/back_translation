# DMC-S1000DBIKE-AAA-D05-10-00-00AA-000A-A_011-00_EN-US
## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** D05
* **Sub System Code:** 1
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 000
* **Info Code Variant:** A
* **Item Location Code:** A
* **Language:**
	+ Country ISO Code: US
	+ Language ISO Code: en
* **Issue Info:**
	+ Issue Number: 011
	+ In Work: 00

#### DM Address Items
* **Issue Date:**
	+ Year: 2024
	+ Month: 06
	+ Day: 19
* **DM Title:**
	+ Tech Name: Bicycle
	+ Info Name: Time limits

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
			- Copyright Para: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
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
		- Data Conds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

* **Responsible Partner Company:**
	+ Enterprise Code: B6865
	+ Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
* **Originator:**
	+ Enterprise Code: B6865
	+ Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

* **Applic Cross Ref Table Ref:**
	+ DM Ref:
		- DM Ref Ident:
			- Model Ident Code: S1000DBIKE
			- System Diff Code: AAA
			- System Code: D00
			- Sub System Code: 0
			- Sub Sub System Code: 0
			- Assy Code: 00
			- Disassy Code: 00
			- Disassy Code Variant: AA
			- Info Code: 00W
			- Info Code Variant: A
			- Item Location Code: D

* **Applic:**
	+ Display Text: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
	+ Evaluate:
		- Assert:
			- Applic Property Ident: type
			- Applic Property Type: prodattr
			- Applic Property Values: Mountain bicycle
		- Evaluate:
			- Assert:
				- Applic Property Ident: model
				- Applic Property Type: prodattr
				- Applic Property Values: Mountain storm
			- Assert:
				- Applic Property Ident: version
				- Applic Property Type: prodattr
				- Applic Property Values: Mk1
			- Evaluate:
				- Assert:
					- Applic Property Ident: model
					- Applic Property Type: prodattr
					- Applic Property Values: Brook trekker
				- Assert:
					- Applic Property Ident: version
					- Applic Property Type: prodattr
					- Applic Property Values: Mk9

* **Tech Info:**
	+ Not available in this document.

## Content
### Maint Planning
#### Time Limit Info
1. **Time Limit Ident:** 001
	* **Applic Ref Id:** MK1MK9
	* **Equip Group:**
		- Equip:
			- Name: Bicycle
			- Ident Number:
				- Manufacturer Code: KZ555
				- Part And Serial Number:
					- Part Number: Bicycle-001
	* **Req Quantity:** 1 EA
	* **Time Limit:**
		- Limit Type: lt07
		- Threshold:
			- Threshold Unit Of Measure: th06
			- Threshold Value: 1
			- Tolerance:
				- Tolerance Type: plusorminus
				- Tolerance Value: 1
2. **Time Limit Ident:** 002
	* **Applic Ref Id:** MK1MK9
	* **Equip Group:**
		- Equip:
			- Name: Brake pads
			- Ident Number:
				- Manufacturer Code: KT444
				- Part And Serial Number:
					- Part Number: BR-PADS-001
	* **Req Quantity:** 4 EA
	* **Time Limit Category:** 1
	* **Time Limit:**
		- Limit Type: lt05
		- Threshold:
			- Threshold Unit Of Measure: th03
			- Threshold Value: 1
3. **Time Limit Ident:** 003
	* **Applic Ref Id:** MK1MK9
	* **Equip Group:**
		- Equip:
			- Name: Chain
			- Ident Number:
				- Manufacturer Code: KZ555
				- Part And Serial Number:
					- Part Number: Ch-001
	* **Time Limit:**
		- Limit Type: lt05
		- Threshold:
			- Threshold Unit Of Measure: th03
			- Threshold Value: 1
4. **Time Limit Ident:** 004
	* **Applic Ref Id:** MK1MK9
	* **Equip Group:**
		- Equip:
			- Name: Hub bearings
			- Ident Number:
				- Manufacturer Code: KZ555
				- Part And Serial Number:
					- Part Number: HB-001
	* **Req Quantity:** 2 EA
	* **Time Limit Category:** 1
	* **Time Limit:**
		- Limit Type: lt06
		- Threshold:
			- Threshold Unit Of Measure: th03
			- Threshold Value: 6
			- Tolerance:
				- Tolerance Type: plusorminus
				- Tolerance Value: 1

### Referenced Applic Group
* **Applic:** MK1MK9
	+ Display Text: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
	+ Evaluate:
		- Assert:
			- Applic Property Ident: type
			- Applic Property Type: prodattr
			- Applic Property Values: Mountain bicycle
		- Evaluate:
			- Assert:
				- Applic Property Ident: model
				- Applic Property Type: prodattr
				- Applic Property Values: Mountain storm
			- Assert:
				- Applic Property Ident: version
				- Applic Property Type: prodattr
				- Applic Property Values: Mk1
			- Evaluate:
				- Assert:
					- Applic Property Ident: model
					- Applic Property Type: prodattr
					- Applic Property Values: Brook trekker
				- Assert:
					- Applic Property Ident: version
					- Applic Property Type: prodattr
					- Applic Property Values: Mk9