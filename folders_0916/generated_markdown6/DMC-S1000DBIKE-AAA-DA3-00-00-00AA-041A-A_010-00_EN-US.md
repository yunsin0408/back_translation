# DMC-S1000DBIKE-AAA-DA3-00-00-00AA-041A-A_010-00_EN-US
## Introduction
The provided XML file `DMC-S1000DBIKE-AAA-DA3-00-00-00AA-041A-A_010-00_EN-US.XML` contains a S1000D data module for a bicycle frame. The following sections provide an overview of the contents.

## Ident and Status Section
### DM Address
The DM address section provides identification information about the data module.
* **DM Ident**
	+ Model Ident Code: `S1000DBIKE`
	+ System Diff Code: `AAA`
	+ System Code: `DA3`
	+ Sub System Code: `0`
	+ Sub Sub System Code: `0`
	+ Assy Code: `00`
	+ Disassy Code: `00`
	+ Disassy Code Variant: `AA`
	+ Info Code: `041`
	+ Info Code Variant: `A`
	+ Item Location Code: `A`
* **Language**
	+ Country Iso Code: `US`
	+ Language Iso Code: `en`
* **Issue Info**
	+ Issue Number: `010`
	+ In Work: `00`
### DM Address Items
The DM address items section provides additional information about the data module.
* **Issue Date**: 2024-06-19
* **DM Title**
	+ Tech Name: Frame
	+ Info Name: Description of how it is made

## DM Status
### Issue Type
The issue type for this data module is `changed`.
### Security
The security classification for this data module is:
* **Security Classification**: `01`
* **Commercial Classification**: `cc51`
* **Caveat**: `cv51`

### Data Restrictions
The data restrictions section provides information about the distribution and use of the data module.
#### Restriction Instructions
* **Data Distribution**: To be made available to all S1000D users.
* **Export Control**
	+ Export Registration Stmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
* **Data Handling**: There are no specific handling instructions for this data module.
* **Data Destruction**: Users may destroy this data module in accordance with their own local procedures.
* **Data Disclosure**: There are no dissemination limitations that apply to this data module.

#### Restriction Info
The restriction info section provides additional information about the data restrictions.
* **Copyright**
	+ Copyright Para: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
	+ Publishers:
		- Aerospace, Security and Defence Industries Association of Europe
		- Aerospace Industries Association of America
		- ATA e-Business Program
	+ Limitations of Liability:
		1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
		2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
		3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* **Policy Statement**: S1000D-SC-2016-017-002-00 Steering Committee TOR
* **Data Conds**: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

### Responsible Partner Company
The responsible partner company is:
* **Enterprise Code**: `B6865`
* **Enterprise Name**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Originator
The originator of the data module is:
* **Enterprise Code**: `B6865`
* **Enterprise Name**: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

### Applic Cross Ref Table Ref
The applic cross ref table ref section provides a reference to another data module.
* **DM Ref**
	+ DM Ref Ident:
		- Model Ident Code: `S1000DBIKE`
		- System Diff Code: `AAA`
		- System Code: `D00`
		- Sub System Code: `0`
		- Sub Sub System Code: `0`
		- Assy Code: `00`
		- Disassy Code: `00`
		- Disassy Code Variant: `AA`
		- Info Code: `00W`
		- Info Code Variant: `A`
		- Item Location Code: `D`

### Applic
The applic section provides information about the application of the data module.
* **Display Text**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Evaluate**
	+ And Or: `and`
	+ Assert:
		- Applic Property Ident: `type`
		- Applic Property Type: `prodattr`
		- Applic Property Values: `Mountain bicycle`
	+ Evaluate:
		- And Or: `or`
		- Evaluate:
			- And Or: `and`
			- Assert:
				- Applic Property Ident: `model`
				- Applic Property Type: `prodattr`
				- Applic Property Values: `Mountain storm`
			- Assert:
				- Applic Property Ident: `version`
				- Applic Property Type: `prodattr`
				- Applic Property Values: `Mk1`
		- Evaluate:
			- And Or: `and`
			- Assert:
				- Applic Property Ident: `model`
				- Applic Property Type: `prodattr`
				- Applic Property Values: `Brook trekker`
			- Assert:
				- Applic Property Ident: `version`
				- Applic Property Type: `prodattr`
				- Applic Property Values: `Mk9`

### Tech Standard
The tech standard section provides information about the technical standards used in the data module.
* **Authority Info And Tp**
	+ Authority Info: 20010131
	+ Tech Pub Base: Bike book

### BrexDm Ref
The brexdm ref section provides a reference to another data module.
* **DM Ref**
	+ DM Ref Ident:
		- Model Ident Code: `S1000DBIKE`
		- System Diff Code: `AAA`
		- System Code: `D00`
		- Sub System Code: `0`
		- Sub Sub System Code: `0`
		- Assy Code: `00`
		- Disassy Code: `00`
		- Disassy Code Variant: `AA`
		- Info Code: `041`
		- Info Code Variant: `A`
		- Item Location Code: `A`

### Quality Assurance
The quality assurance section provides information about the quality of the data module.
* **Verification**: The data module has been verified to ensure that it meets the requirements.

## Content
The content section provides the main body of the data module.
### Description
The description section provides a detailed description of the bicycle frame.
* **Levelled Para**
	+ The initial frames (refer to [fig-0001](#fig-0001)) were tubes of aluminum or steel welded together.
	+ Subsequent frames (refer to [fig-0002](#fig-0002)) can be made out of a wide variety of materials, including aluminium, titanium, or chrome moly.
	+ Other Frames are different and can also be of different materials (for example, titanium or chrome moly). Some bicycle frames are of carbon fiber. To get this material, it is necessary to put sheets of carbon fiber cloth on foam forms and epoxy them in position. This procedure gives a very light, strong structure that can have different shapes.
	+ The frame includes the parts that follow:
		1. the top tube (the higher bar of the bicycle frame)
		2. the down tube (the section of the frame that extends from the stem to the bottom bracket)
		3. the head tube (the part of the frame that the fork steerer tube goes through)
		4. the seat tube (the vertical part of the frame that is the rear of the front triangle and that is between the bottom bracket and the top tube)
		5. the seat stay (the tube that includes the distance between the seat tube and the rear dropouts)
		6. the chain stay (the tube that is the bottom part of the rear triangle)

#### Figures
##### fig-0001
* **Title**: Welded frame joints
* **Graphic**: ICN-C0419-S1000D0394-001-01

##### fig-0002
* **Title**: Frame
* **Graphic**: ICN-C0419-S1000D0393-001-01