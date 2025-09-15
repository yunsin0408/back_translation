DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00HA-D_004-00_EN-US
==============================================

## Ident and Status Section
The ident and status section contains information about the data module's identification and status.

### DM Address
The DM address section contains information about the data module's address.

#### DM Ident
The DM ident section contains information about the data module's identification.
* **Model Ident Code**: S1000DLIGHTING
* **System Diff Code**: AAA
* **System Code**: D00
* **Sub System Code**: 0
* **Sub Sub System Code**: 0
* **Assy Code**: 00
* **Disassy Code**: 00
* **Disassy Code Variant**: AA
* **Info Code**: 00H
* **Info Code Variant**: A
* **Item Location Code**: D

#### Language
The language section contains information about the data module's language.
* **Language Iso Code**: en
* **Country Iso Code**: US

#### Issue Info
The issue info section contains information about the data module's issue.
* **Issue Number**: 004
* **In Work**: 00

### DM Address Items
The DM address items section contains additional information about the data module's address.

#### Issue Date
The issue date section contains information about the data module's issue date.
* **Year**: 2024
* **Month**: 06
* **Day**: 19

#### DM Title
The DM title section contains information about the data module's title.
* **Tech Name**: Lighting
* **Info Name**: Zones common information repository

### DM Status
The DM status section contains information about the data module's status.

#### Issue Type
The issue type is: revised

#### Security
The security section contains information about the data module's security classification.
* **Security Classification**: 01
* **Commercial Classification**: cc51
* **Caveat**: cv51

#### Data Restrictions
The data restrictions section contains information about the data module's restrictions.

##### Restriction Instructions
The restriction instructions section contains information about the data module's restriction instructions.
* **Data Distribution**: To be made available to all S1000D users.
* **Export Control**:
	+ **Export Registration Statement**: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
* **Data Handling**: There are no specific handling instructions for this data module.
* **Data Destruction**: Users may destroy this data module in accordance with their own local procedures.
* **Data Disclosure**: There are no dissemination limitations that apply to this data module.

##### Restriction Info
The restriction info section contains additional information about the data module's restrictions.
* **Copyright**:
	+ **Copyright Paragraph**: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
	+ **Publishers**:
		- Aerospace, Security and Defence Industries Association of Europe
		- Aerospace Industries Association of America
		- ATA e-Business Program
	+ **Limitations of Liability**:
		- This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
		- Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
		- Revisions may occur and therefore users should check the document's currency before relying on it.
* **Policy Info**: There are no policy information available.

#### Responsible Organization
The responsible organization section contains information about the data module's responsible organization.
* **Enterprise Id**: Not specified

### Applicability
The applicability section contains information about the data module's applicability.

## Content
The content section contains the main body of the data module.

### Referenced Applic Group
The referenced applic group section contains a list of referenced applications.

#### Applic 1
* **Applic Id**: app-0001
* **Display Text**: Mountain storm Mk1
* **Assert**:
	+ **Applic Property Ident**: model
	+ **Applic Property Type**: prodattr
	+ **Applic Property Values**: Mountain storm
	+ **Applic Property Ident**: version
	+ **Applic Property Type**: prodattr
	+ **Applic Property Values**: Mk1

#### Applic 2
* **Applic Id**: app-0002
* **Display Text**: Brook trekker Mk9
* **Assert**:
	+ **Applic Property Ident**: model
	+ **Applic Property Type**: prodattr
	+ **Applic Property Values**: Brook trekker
	+ **Applic Property Ident**: version
	+ **Applic Property Type**: prodattr
	+ **Applic Property Values**: Mk9

#### Applic 3
* **Applic Id**: app-0003
* **Display Text**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
* **Assert**:
	+ **Applic Property Ident**: type
	+ **Applic Property Type**: prodattr
	+ **Applic Property Values**: Mountain bicycle
	+ **Assert**:
		- **Applic Property Ident**: model
		- **Applic Property Type**: prodattr
		- **Applic Property Values**: Mountain storm
		- **Applic Property Ident**: version
		- **Applic Property Type**: prodattr
		- **Applic Property Values**: Mk1
	+ **Assert**:
		- **Applic Property Ident**: model
		- **Applic Property Type**: prodattr
		- **Applic Property Values**: Brook trekker
		- **Applic Property Ident**: version
		- **Applic Property Type**: prodattr
		- **Applic Property Values**: Mk9

### Common Repository
The common repository section contains a list of zones.

#### Zone Repository
The zone repository section contains a list of zones.

##### Zone 1: FRONT
* **Zone Number**: 100
* **Zone Type**: majorzone
* **Zone Ref Group**:
	+ **Zone Ref Type**: contains
	+ **Zone Ref Number**: 110
	+ **Zone Ref Number**: 130
* **Zone Alts**:
	+ **Applic Ref Id**: app-0002
	+ **Item Descr**: FRONT ZONE BEGINS BY FRONT TIRE. IT STARTS FROM LENGTH "0 cm" TO LENGTH "50 cm"

##### Zone 2: TIRE ZONE
* **Zone Number**: 110
* **Zone Type**: subzone
* **Zone Ref Group**:
	+ **Zone Ref Type**: belongsto
	+ **Zone Ref Number**: 100
* **Zone Alts**:
	+ **Applic Ref Id**: app-0002
	+ **Item Descr**: TIRE ZONE INCLUDING THE FRONT TIRE, THE INNER TUBE AND THE SPOKES

##### Zone 3: HANDLE BAR ZONE
* **Zone Number**: 130
* **Zone Type**: subzone
* **Zone Ref Group**:
	+ **Zone Ref Type**: belongsto
	+ **Zone Ref Number**: 100
	+ **Zone Ref Type**: contains
	+ **Zone Ref Number**: 131
	+ **Zone Ref Number**: 132
* **Zone Alts**:
	+ **Applic Ref Id**: app-0003
	+ **Item Descr**: HANDLE BAR ZONE

##### Zone 4: RIGHT HAND HANDLE BAR ZONE
* **Zone Number**: 131
* **Zone Type**: specifzone
* **Zone Ref Group**:
	+ **Zone Ref Type**: belongsto
	+ **Zone Ref Number**: 130
* **Zone Alts**:
	+ **Applic Ref Id**: app-0003
	+ **Item Descr**: RIGHT HAND HANDLE BAR ZONE

##### Zone 5: LEFT HAND HANDLE BAR ZONE
* **Zone Number**: 132
* **Zone Type**: specifzone
* **Zone Ref Group**:
	+ **Zone Ref Type**: belongsto
	+ **Zone Ref Number**: 130
* **Zone Alts**:
	+ **Applic Ref Id**: app-0003
	+ **Item Descr**: LEFT HAND HANDLE BAR ZONE

##### Zone 6: MIDDLE
* **Zone Number**: 200
* **Zone Type**: majorzone
* **Zone Alts**:
	+ **Applic Ref Id**: app-0002
	+ **Item Descr**: MIDDLE ZONE. IT STARTS FROM LENGTH "50 cm" TO LENGTH "100 cm"

##### Zone 7: BACK
* **Zone Number**: 300
* **Zone Type**: majorzone
* **Zone Alts**:
	+ **Applic Ref Id**: app-0001
	+ **Item Descr**: BACK ZONE. IT STARTS FROM LENGTH "100 cm" TO LENGTH "150 cm"