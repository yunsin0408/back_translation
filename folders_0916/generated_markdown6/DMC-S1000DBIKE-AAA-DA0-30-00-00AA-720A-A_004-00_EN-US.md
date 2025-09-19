# DMC-S1000DBIKE-AAA-DA0-30-00-00AA-720A-A_004-00_EN-US
## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code**: S1000DBIKE
* **System Diff Code**: AAA
* **System Code**: DA0
* **Sub System Code**: 3
* **Sub Sub System Code**: 0
* **Assy Code**: 00
* **Disassy Code**: 00
* **Disassy Code Variant**: AA
* **Info Code**: 720
* **Info Code Variant**: A
* **Item Location Code**: A
* **Language**:
	+ Country ISO Code: US
	+ Language ISO Code: en
* **Issue Info**:
	+ Issue Number: 004
	+ In Work: 00

#### DM Address Items
* **Issue Date**:
	+ Year: 2024
	+ Month: 06
	+ Day: 19
* **DM Title**:
	+ Tech Name: Front wheel
	+ Info Name: Install procedures

### DM Status
#### Issue Type
* **Status**

#### Security
* **Security Classification**: 01
* **Commercial Classification**: cc51
* **Caveat**: cv51

#### Data Restrictions
##### Restriction Instructions
* **Data Distribution**: To be made available to all S1000D users.
* **Export Control**:
	+ Export Registration Statement: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
* **Data Handling**: There are no specific handling instructions for this data module.
* **Data Destruction**: Users may destroy this data module in accordance with their own local procedures.
* **Data Disclosure**: There are no dissemination limitations that apply to this data module.

##### Restriction Info
* **Copyright**:
	+ Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
	+ Publishers:
		- Aerospace, Security and Defence Industries Association of Europe
		- Aerospace Industries Association of America
		- ATA e-Business Program
	+ Limitations of Liability:
		- This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
		- Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
		- Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* **Policy Statement**: S1000D-SC-2016-017-002-00 Steering Committee TOR
* **Data Conds**: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company
* **Enterprise Code**: B6865
* **Enterprise Name**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Originator
* **Enterprise Code**: B6865
* **Enterprise Name**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

#### Applic Cross Ref Table Ref
* **DM Ref**:
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

#### Applic
* **Display Text**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Evaluate**:
	+ And/Or: and
	+ Assert:
		- Applic Property Ident: type
		- Applic Property Type: prodattr
		- Applic Property Values: Mountain bicycle
	+ Evaluate:
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

#### Tech Note
* No technical notes available.

## Content
### Referenced Applic Group
* **Applic**:
	+ ID: app-0002
	+ Display Text: Mountain bicycle and Mountain storm Mk1
	+ Evaluate:
		- And/Or: and
		- Assert:
			- Applic Property Ident: type
			- Applic Property Type: prodattr
			- Applic Property Values: Mountain bicycle
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
* **Applic**:
	+ ID: app-0003
	+ Display Text: Mountain bicycle and Brook trekker Mk9
	+ Evaluate:
		- And/Or: and
		- Assert:
			- Applic Property Ident: type
			- Applic Property Type: prodattr
			- Applic Property Values: Mountain bicycle
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

### Procedure
#### Preliminary Requirements
* **Required Conditions Group**: No conditions.
* **Required Persons**: No personnel required.
* **Required Support Equipment**:
	+ Support Equip Descr Group:
		- Support Equip Descr:
			- ID: seq-0001
			- Name: Specialist toolset
			- Ident Number:
				- Manufacturer Code: KZ666
				- Part and Serial Number:
					- Part Number: BSK-TLST-001
			- Required Quantity: 1 EA
* **Required Supplies**: No supplies required.
* **Required Spares**: No spares required.
* **Required Safety**: No safety requirements.

#### Main Procedure
* **Procedural Step**:
	+ Note: It is necessary to install the fork and the brakes before installing the wheel.
* **Procedural Step**:
	+ Para: Hold the front of the bicycle.
* **Procedural Step**:
	+ Para: Install the wheel with (Specialist toolset) and be careful to not damage the chainring.
* **Procedural Step**:
	+ Para: Close the light circuit breaker located on the handlebar
	+ Circuit Breaker Descr Group:
		- ID: SPEC-0009
		- Circuit Breaker Descr Sub Group:
			- Applic Ref ID: app-0002
			- Circuit Breaker Action: close
			- ID: SPEC-0001
			- Circuit Breaker Descr:
				- ID: SPEC-0007
				- Circuit Breaker Ref: CBLGT-1001-R
				- Name: Bike Lighting circuit breaker (right side)
				- Access Point Ref:
					- Access Point Number: any-access
					- ID: SPEC-0005
				- Circuit Breaker Location:
					- ID: SPEC-0003
					- Zone: 131
		- Circuit Breaker Descr Sub Group:
			- Applic Ref ID: app-0003
			- Circuit Breaker Action: close
			- ID: SPEC-0002
			- Circuit Breaker Descr:
				- ID: SPEC-0008
				- Circuit Breaker Ref: CBLGT-1001-L
				- Name: Bike Lighting circuit breaker (left side)
				- Access Point Ref:
					- Access Point Number: any-access
					- ID: SPEC-0006
				- Circuit Breaker Location:
					- ID: SPEC-0004
					- Zone: 132
* **Procedural Step**:
	+ Para: Put the bike on the floor.

#### Close Requirements
* **Required Conditions Group**: No conditions.