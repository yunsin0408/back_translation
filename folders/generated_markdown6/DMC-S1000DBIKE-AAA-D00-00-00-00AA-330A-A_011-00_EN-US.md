# DMC-S1000DBIKE-AAA-D00-00-00-00AA-330A-A_011-00_EN-US
## Introduction
The following document is based on the XML file `DMC-S1000DBIKE-AAA-D00-00-00-00AA-330A-A_011-00_EN-US.XML`.

## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code**: S1000DBIKE
* **System Diff Code**: AAA
* **System Code**: D00
* **Sub System Code**: 0
* **Sub Sub System Code**: 0
* **Assy Code**: 00
* **Disassy Code**: 00
* **Disassy Code Variant**: AA
* **Info Code**: 330
* **Info Code Variant**: A
* **Item Location Code**: A
* **Language**:
	+ Country ISO Code: US
	+ Language ISO Code: en
* **Issue Info**:
	+ Issue Number: 011
	+ In Work: 00

#### DM Address Items
* **Issue Date**: 2024-06-19
* **DM Title**:
	+ Tech Name: Bicycle
	+ Info Name: Place on test stand

### DM Status
* **Issue Type**: changed
* **Security**:
	+ Security Classification: 01
	+ Commercial Classification: cc51
* **Data Restrictions**:
	+ **Restriction Instructions**:
		- Data Distribution: To be made available to all S1000D users.
		- Export Control:
			- Export Registration Statement: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- Data Handling: There are no specific handling instructions for this data module.
		- Data Destruction: Users may destroy this data module in accordance with their own local procedures.
		- Data Disclosure: There are no dissemination limitations that apply to this data module.
	+ **Restriction Info**:
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
		- Policy Statement: S1000D-SC-2016-017-002-00 Steering Committee TOR
		- Data Conds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

* **Responsible Partner Company**:
	+ Enterprise Code: B6865
	+ Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
* **Originator**:
	+ Enterprise Code: B6865
	+ Enterprise Name: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
* **Applic Cross Ref Table Ref**:
	+ DM Ref Ident:
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
* **Applic**:
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
					- Applic Property Values: Mk9

* **Tech Standard**:
	+ Authority Info And Tp:
		- Authority Info: 20010131
		- Tech Pub Base: Bike book
	+ Authority Exceptions: None
	+ Authority Notes: None
* **BrexDm Ref**:
	+ DM Ref Ident:
		- Model Ident Code: S1000DBIKE
		- System Diff Code: AAA
		- System Code: D00
		- Sub System Code: 0
		- Sub Sub System Code: 0
		- Assy Code: 00
		- Disassy Code: 00
		- Disassy Code Variant: AA
		- Info Code: 022
		- Info Code Variant: A
		- Item Location Code: D

* **Quality Assurance**:
	+ First Verification:
		- Verification Type: tabtop
* **System Breakdown Code**: BY112
* **Skill Level**:
	+ Skill Level Code: sk01
* **Reason For Update**:
	+ Id: rfu_general
	+ Update Reason Type: urt03
	+ Simple Para: S1000D upissued

## Content
### Procedure
#### Preliminary Rqmts
* **Req Cond Group**: No conditions
* **Req Persons**:
	+ Person:
		- Man: A
		- Person Category:
			- Person Category Code: Basic user
		- Trade: Operator
		- Estimated Time:
			- Unit Of Measure: h
			- Value: 0.3
* **Req Support Equips**:
	+ Support Equip Descr Group:
		- Support Equip Descr:
			- Id: seq-0001
			- Name: Test stand
			- Ident Number:
				- Manufacturer Code: KZ666
				- Part And Serial Number:
					- Part Number: BSK-TLST-999-01
			- Req Quantity:
				- Unit Of Measure: EA
				- Value: 1

* **Req Supplies**: No supplies
* **Req Spares**: No spares
* **Req Safety**: No safety requirements

#### Main Procedure
1. Ensure the test stand is level.
2. Place the bicycle on the test stand.
3. Tighten clamps until the bicycle is securely attached to the test stand.

#### Close Rqmts
* **Req Cond Group**: No conditions

Note: This markdown document is based on the provided XML file and maintains the same structure and content. However, some formatting and indentation may have been adjusted for better readability.