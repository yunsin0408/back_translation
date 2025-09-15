# DMC-S1000DBIKE-AAA-DA0-10-10-00AA-921A-A_010-00_EN-US
## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** DA0
* **Sub System Code:** 1
* **Sub Sub System Code:** 0
* **Assy Code:** 10
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 921
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
	+ Tech Name: Inner tube
	+ Info Name: Remove and install a new item

### DM Status
* **Issue Type:** changed
* **Security:**
	+ Security Classification: 01
	+ Commercial Classification: cc51
	+ Caveat: cv51
* **Data Restrictions:**
	+ **Restriction Instructions:**
		- Data Distribution: To be made available to all S1000D users.
		- Export Control:
			- Export Registration Statement: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- Data Handling: There are no specific handling instructions for this data module.
		- Data Destruction: Users may destroy this data module in accordance with their own local procedures.
		- Data Disclosure: There are no dissemination limitations that apply to this data module.
	+ **Restriction Info:**
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
			- Details for copyright can be found in the S1000D Specification.
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
		- And/Or: and
		- Assert:
			- Applic Property Ident: type
			- Applic Property Type: prodattr
			- Applic Property Values: Mountain bicycle
		- Evaluate:
			- And/Or: or
			- Evaluate:
				- And/Or: and
				- Assert:
					- Applic Property Ident: model
					- Applic Property Type: prodattr
					- Applic Property Values: Mountain storm
				- Assert:
					- Applic Property Ident: version
					- Applic Property Type: prodattr
					- Applic Property Values: Mk1
			- Evaluate:
				- And/Or: and
				- Assert:
					- Applic Property Ident: model
					- Applic Property Type: prodattr
					- Applic Property Values: Brook trekker
				- Assert:
					- Applic Property Ident: version
					- Applic Property Type: prodattr
					- Applic Property Values: Mk1
* **Tech Note:** Not applicable

## Content
### References
* DM Ref:
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
* DM Ref:
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

### Procedure
#### Preliminary Requirements
* **Req Cond Group:**
	+ Req Cond Dm:
		- Req Cond: The tire is removed.
		- DM Ref:
			- Model Ident Code: S1000DBIKE
			- System Diff Code: AAA
			- System Code: DA0
			- Sub System Code: 1
			- Sub Sub System Code: 0
			- Assy Code: 20
			- Disassy Code: 00
			- Disassy Code Variant: AA
			- Info Code: 215
			- Info Code Variant: A
			- Item Location Code: A
* **Req Persons:**
	+ Person:
		- Man: A
		- Person Category: Basic user
		- Trade: Operator
		- Estimated Time: 0.3 hours
* **Req Support Equips:** No support equips required
* **Req Supplies:** No supplies required
* **Req Spares:**
	+ Spare Descr Group:
		- Spare Descr:
			- ID: spa-0001
			- Name: Inner tube
			- Ident Number:
				- Manufacturer Code: KT222
				- Part and Serial Number:
					- Part Number: IT-001
			- Req Quantity: 1 EA
* **Req Safety:**
	+ Safety Rqmts:
		- Caution: Be careful with sharp or hard tools. They can cause damage to the inner tube.

#### Main Procedure
1. Remove the old inner-tube.
2. Install the new [inner tube](#req-spares).
	* Figure: Removing the inner tube
		+ Title: Removing the inner tube
		+ Graphic: ICN-C0419-S1000D0369-001-01

#### Close Requirements
* **Req Cond Group:**
	+ Req Cond No Ref:
		- Req Cond: Replace the tire.
	+ Req Cond Dm:
		- Req Cond: Inflate the tire with air.
		- DM Ref:
			- Model Ident Code: S1000DBIKE
			- System Diff Code: AAA
			- System Code: DA0
			- Sub System Code: 1
			- Sub Sub System Code: 0
			- Assy Code: 20
			- Disassy Code: 00
			- Disassy Code Variant: AA
			- Info Code: 215
			- Info Code Variant: A
			- Item Location Code: A