# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00JA-D_001-00_EN-US
## Introduction
The XML file `DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00JA-D_001-00_EN-US.XML` is a S1000D document that contains information about lighting systems. This markdown document provides a clean and well-structured representation of the XML content.

## Ident and Status Section
### DM Address
The `dmAddress` section contains information about the document's identification and status.
* **DM Ident**
	+ Model Ident Code: S1000DLIGHTING
	+ System Diff Code: AAA
	+ System Code: D00
	+ Sub System Code: 0
	+ Sub Sub System Code: 0
	+ Assy Code: 00
	+ Disassy Code: 00
	+ Disassy Code Variant: AA
	+ Info Code: 00J
	+ Info Code Variant: A
	+ Item Location Code: D
* **Language**
	+ Country ISO Code: US
	+ Language ISO Code: en
* **Issue Info**
	+ Issue Number: 001
	+ In Work: 00

### DM Address Items
The `dmAddressItems` section contains additional information about the document.
* **Issue Date**
	+ Year: 2024
	+ Month: 06
	+ Day: 19
* **DM Title**
	+ Tech Name: Lighting
	+ Info Name: Access panels and doors common information repository

### DM Status
The `dmStatus` section contains information about the document's status.
* **Issue Type**: new
* **Security**
	+ Caveat: cv51
	+ Commercial Classification: cc51
	+ Security Classification: 01
* **Data Restrictions**
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
				+ Aerospace, Security and Defence Industries Association of Europe
				+ Aerospace Industries Association of America
				+ ATA e-Business Program
			- Limitations of liability:
				+ This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
				+ Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
				+ Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
		- Policy Statement: S1000D-SC-2016-017-002-00 Steering Committee TOR
		- Data Conds: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Responsible Partner Company
The `responsiblePartnerCompany` section contains information about the responsible partner company.
* **Enterprise Code**: B6865
* **Enterprise Name**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Originator
The `originator` section contains information about the originator.
* **Enterprise Code**: B6865
* **Enterprise Name**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Applic Cross Ref Table Ref
The `applicCrossRefTableRef` section contains a reference to an application cross-reference table.
* **DM Ref**
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

### Applic
The `applic` section contains information about the application.
* **Display Text**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Evaluate**
	+ And Or: and
	+ Assert:
		- Applic Property Ident: type
		- Applic Property Type: prodattr
		- Applic Property Values: Mountain bicycle
	+ Evaluate:
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

### Tech Standard
The `techStandard` section contains information about the technical standard.
* **Authority Info And Tp**
	+ Authority Info: 20010131
	+ Tech Pub Base: Bike book
* **Authority Exceptions**: None
* **Authority Notes**: None

### Brex DM Ref
The `brexDmRef` section contains a reference to a BREX data module.
* **DM Ref**
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

### Quality Assurance
The `qualityAssurance` section contains information about the quality assurance.
* **First Verification**
	+ Verification Type: tabtop

### Remarks
The `remarks` section contains additional remarks.
* **Simple Para**: CPF_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples
* **Simple Para**: accessPointRepository, accessPointSpec, accessPointIdent, accessPointAlts, accessPoint, accessPointType, accessTo, otherItems

## Content
The `content` section contains the main content of the document.
### Common Repository
The `commonRepository` section contains information about the common repository.
* **Access Point Repository**
	+ Id: SPEC-0001
	+ Access Point Spec:
		- Id: acc-0001
		- Access Point Ident:
			- Access Point Number: any-access
			- Id: SPEC-0002
		- Access Point Alts:
			- Id: SPEC-0003
			- Access Point:
				- Id: SPEC-0004
				- Access Point Type:
					- Access Point Type Value: accpnl03
					- Id: SPEC-0005
				- Zone Ref:
					- Name: N/A
				- Access To:
					- Id: SPEC-0006
					- Other Items:
						- Id: SPEC-0007
						- Value: This dummy access point gives access to all electrical parts of the bike.