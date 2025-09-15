DMC-S1000D LIGHTING AAA D00 00 00 00AA 00HA D_004 00 EN US
==============================================

## Ident and Status Section

### DM Address

#### DM Ident

The following attributes are defined for the `dmIdent` element:

* **modelIdentCode**: S1000DLIGHTING
* **systemDiffCode**: AAA
* **systemCode**: D00
* **subSystemCode**: 0
* **subSubSystemCode**: 0
* **assyCode**: 00
* **disassyCode**: 00
* **disassyCodeVariant**: AA
* **infoCode**: 00H
* **infoCodeVariant**: A
* **itemLocationCode**: D

The language for this document is defined as:
* **languageIsoCode**: en
* **countryIsoCode**: US

The issue information for this document is:
* **issueNumber**: 004
* **inWork**: 00

#### DM Address Items

The following attributes are defined for the `dmAddressItems` element:

##### Issue Date

* **year**: 2024
* **month**: 06
* **day**: 19

##### DM Title

The technical name and information name for this document are:
* **techName**: Lighting
* **infoName**: Zones common information repository

### DM Status

The issue type for this document is: **revised**

#### Security

The security classification and commercial classification for this document are:
* **securityClassification**: 01
* **commercialClassification**: cc51
* **caveat**: cv51

#### Data Restrictions

##### Restriction Instructions

The following data distribution, export control, data handling, data destruction, and data disclosure instructions apply:

* **dataDistribution**: To be made available to all S1000D users.
* **exportControl**:
	+ The export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted.
	+ Storage of this data module is to be at the discretion of the organization.
* **dataHandling**: There are no specific handling instructions for this data module.
* **dataDestruction**: Users may destroy this data module in accordance with their own local procedures.
* **dataDisclosure**: There are no dissemination limitations that apply to this data module.

##### Restriction Info

The following copyright, policy statement, and data conditions information applies:

* **copyright**:
	+ Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
	+ Publishers:
		- Aerospace, Security and Defence Industries Association of Europe
		- Aerospace Industries Association of America
		- ATA e-Business Program
	+ Limitations of liability:
		- This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
		- Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
		- Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
* **policyStatement**: S1000D-SC-2016-017-002-00 Steering Committee TOR
* **dataConds**: There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company

The responsible partner company is:
* **enterpriseName**: Not specified (only enterprise ID is required)
* **enterpriseID**: Not specified
* **enterpriseRole**: Not specified

However, in the actual XML document provided, only `enterpriseID` and `enterpriseRole` would be present if it followed the same structure as other elements.

#### Common Repository

The common repository contains a zone repository with various zones defined:

### Zone Repository

The following zones are defined:

* **Zone 100**: FRONT ZONE
	+ Description: FRONT ZONE BEGINS BY FRONT TIRE. IT STARTS FROM LENGTH "0 cm" TO LENGTH "50 cm"
	+ Contains:
		- Zone 110 (TIRE ZONE)
		- Zone 130 (HANDLE BAR ZONE)
* **Zone 110**: TIRE ZONE
	+ Description: TIRE ZONE INCLUDING THE FRONT TIRE, THE INNER TUBE AND THE SPOKES
	+ Belongs to: Zone 100
* **Zone 130**: HANDLE BAR ZONE
	+ Description: HANDLE BAR ZONE
	+ Contains:
		- Zone 131 (RIGHT HAND HANDLE BAR ZONE)
		- Zone 132 (LEFT HAND HANDLE BAR ZONE)
	+ Belongs to: Zone 100
* **Zone 131**: RIGHT HAND HANDLE BAR ZONE
	+ Description: RIGHT HAND HANDLE BAR ZONE
	+ Belongs to: Zone 130
* **Zone 132**: LEFT HAND HANDLE BAR ZONE
	+ Description: LEFT HAND HANDLE BAR ZONE
	+ Belongs to: Zone 130
* **Zone 200**: MIDDLE ZONE
	+ Description: MIDDLE ZONE. IT STARTS FROM LENGTH "50 cm" TO LENGTH "100 cm"
* **Zone 300**: BACK ZONE
	+ Description: BACK ZONE. IT STARTS FROM LENGTH "100 cm" TO LENGTH "150 cm"

## Applicability

The following applicability rules are defined:

### Applic Rules

* **App-0001**:
	+ Display text: Not specified in the XML (only `applicPropertyIdent` and `applicPropertyType` are present)
	+ Applies to model: Mountain storm
	+ Version: Mk1
	+ Versrank: 1~3
* **App-0002**:
	+ Display text: Brook trekker Mk9
	+ Applies to model: Brook trekker
	+ Version: Mk9
	+ Versrank: 1~2
* **App-0003**:
	+ Display text: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
	+ Applies to type: Mountain bicycle
	+ Model: 
		- Mountain storm
		- Brook trekker
	+ Version: 
		- Mk1 (for Mountain storm)
		- Mk9 (for Brook trekker)

However, please note that the actual display text for `app-0001` would depend on the context or external information not provided in the XML. In this markdown representation, it is assumed to be part of the applicability rules for demonstration purposes.

This document provides a structured overview of the zones and their relationships within the common repository, along with the applicable rules and restrictions associated with each zone.