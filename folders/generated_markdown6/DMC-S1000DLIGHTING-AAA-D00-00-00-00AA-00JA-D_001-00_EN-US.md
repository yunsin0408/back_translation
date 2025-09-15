DMC-S1000D LIGHTING AAA D00 00 00 00AA 00JA D_001 00 EN-US
============================================================

### Ident and Status Section
#### DM Address
##### DM Ident
* **Model Ident Code:** S1000DLIGHTING
* **System Diff Code:** AAA
* **System Code:** D00
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 00J
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:**
	+ Country Iso Code: US
	+ Language Iso Code: en
* **Issue Info:**
	+ Issue Number: 001
	+ In Work: 00

##### DM Address Items
* **Issue Date:** 2024-06-19
* **DM Title:**
	+ Tech Name: Lighting
	+ Info Name: Access panels and doors common information repository

#### DM Status
* **Issue Type:** new
* **Security:**
	+ Caveat: cv51
	+ Commercial Classification: cc51
	+ Security Classification: 01
* **Data Restrictions:**
	+ **Restriction Instructions:**
		- Data Distribution: To be made available to all S1000D users.
		- Export Control:
			- Export Registration Stmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- Data Handling: There are no specific handling instructions for this data module.
		- Data Destruction: Users may destroy this data module in accordance with their own local procedures.
		- Data Disclosure: There are no dissemination limitations that apply to this data module.
	+ **Restriction Info:**
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
			- DM Code:
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
	+ Display Text:
		- Simple Para: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
	+ Evaluate:
		- And Or: and
		- Assert:
			- Applic Property Ident: type
			- Applic Property Type: prodattr
			- Applic Property Values: Mountain bicycle
		- Evaluate:
			- And Or: or
			- Evaluate:
				- And Or: and
				- Assert:
					- Applic Property Ident: model
					- Applic Property Type: prodattr
					- Applic Property Values: Mountain storm
				- Assert:
					- Applic Property Ident: version
					- Applic Property Type: prodattr
					- Applic Property Values: Mk1
				- Assert:
					- Applic Property Ident: versrank
					- Applic Property Type: prodattr
					- Applic Property Values: 1~3
			- Evaluate:
				- And Or: and
				- Assert:
					- Applic Property Ident: model
					- Applic Property Type: prodattr
					- Applic Property Values: Brook trekker
				- Assert:
					- Applic Property Ident: version
					- Applic Property Type: prodattr
					- Applic Property Values: Mk9
				- Assert:
					- Applic Property Ident: versrank
					- Applic Property Type: prodattr
					- Applic Property Values: 1~2

* **Tech Standard:**
	+ Authority Info And Tp:
		- Authority Info: 20010131
		- Tech Pub Base: Bike book
	+ Authority Exceptions: None
	+ Authority Notes: None
* **BrexDm Ref:**
	+ DM Ref:
		- DM Ref Ident:
			- DM Code:
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
* **Quality Assurance:**
	+ First Verification:
		- Verification Type: tabtop
* **Remarks:**
	+ Simple Para: CPF_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples
	+ Simple Para: accessPointRepository, accessPointSpec, accessPointIdent, accessPointAlts, accessPoint, accessPointType, accessTo, otherItems

### Content
#### Common Repository
##### Access Point Repository
* **ID:** SPEC-0001
* **Access Point Spec:**
	+ **ID:** acc-0001
	+ **Access Point Ident:**
		- Access Point Number: any-access
		- ID: SPEC-0002
	+ **Access Point Alts:**
		- ID: SPEC-0003
		- Access Point:
			- ID: SPEC-0004
			- Access Point Type:
				- Access Point Type Value: accpnl03
				- ID: SPEC-0005
			- Zone Ref:
				- Name: N/A
			- Access To:
				- ID: SPEC-0006
				- Other Items:
					- ID: SPEC-0007
					- Text: This dummy access point gives access to all electrical parts of the bike.