# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00FA-D_001-00_EN-US
## Introduction
The DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00FA-D_001-00_EN-US document is a data module that provides information about the lighting system of a mountain bicycle.

## Ident and Status Section
### DM Address
The DM address section contains information about the data module's identification and status.
#### DM Ident
* **Model Ident Code:** S1000DLIGHTING
* **System Diff Code:** AAA
* **System Code:** D00
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 00F
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:** en-US
* **Issue Number:** 001
* **In Work:** 00

#### DM Address Items
* **Issue Date:** 2024-06-19
* **DM Title:**
	+ **Tech Name:** Lighting
	+ **Info Name:** Circuit Breaker common information repository

### DM Status
The DM status section contains information about the data module's status and restrictions.
* **Issue Type:** new
* **Security:**
	+ **Security Classification:** 01
	+ **Commercial Classification:** cc51
	+ **Caveat:** cv51
* **Data Restrictions:**
	+ **Restriction Instructions:**
		- **Data Distribution:** To be made available to all S1000D users.
		- **Export Control:**
			- **Export Registration Statement:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- **Data Handling:** There are no specific handling instructions for this data module.
		- **Data Destruction:** Users may destroy this data module in accordance with their own local procedures.
		- **Data Disclosure:** There are no dissemination limitations that apply to this data module.
	+ **Restriction Info:**
		- **Copyright:**
			- **Text:** 
			- **List:**
				1. The copyright notice is not provided in the given XML document.
		- **Responsible Organization:** Not specified

### Responsible Organization
The responsible organization for this data module is not specified.

## Content
The content section contains information about the lighting system of a mountain bicycle.
### Referenced Applic Group
The referenced applic group section contains a list of applications that are relevant to the lighting system.
* **Applic 1:**
	+ **Display Text:** Mountain storm Mk1
	+ **Evaluate:**
		- **And:**
			- **Assert:**
				- **Property Name:** type
				- **Property Value:** Mountain bicycle
			- **Or:**
				- **And:**
					- **Assert:**
						- **Property Name:** model
						- **Property Value:** Mountain storm
					- **Assert:**
						- **Property Name:** version
						- **Property Value:** Mk1
					- **Assert:**
						- **Property Name:** versrank
						- **Property Value:** 1~3
				- **And:**
					- **Assert:**
						- **Property Name:** model
						- **Property Value:** Brook trekker
					- **Assert:**
						- **Property Name:** version
						- **Property Value:** Mk9
					- **Assert:**
						- **Property Name:** versrank
						- **Property Value:** 1~2
* **Applic 2:**
	+ **Display Text:** Brook trekker Mk9
	+ **Evaluate:**
		- **And:**
			- **Assert:**
				- **Property Name:** type
				- **Property Value:** Mountain bicycle
			- **Or:**
				- **And:**
					- **Assert:**
						- **Property Name:** model
						- **Property Value:** Brook trekker
					- **Assert:**
						- **Property Name:** version
						- **Property Value:** Mk9
					- **Assert:**
						- **Property Name:** versrank
						- **Property Value:** 1~2
				- **And:**
					- **Assert:**
						- **Property Name:** model
						- **Property Value:** Mountain storm
					- **Assert:**
						- **Property Name:** version
						- **Property Value:** Mk1
					- **Assert:**
						- **Property Name:** versrank
						- **Property Value:** 1~3
* **Applic 3:**
	+ **Display Text:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
	+ **Evaluate:**
		- **And:**
			- **Assert:**
				- **Property Name:** type
				- **Property Value:** Mountain bicycle
			- **Or:**
				- **And:**
					- **Assert:**
						- **Property Name:** model
						- **Property Value:** Mountain storm
					- **Assert:**
						- **Property Name:** version
						- **Property Value:** Mk1
					- **Assert:**
						- **Property Name:** versrank
						- **Property Value:** 1~3
				- **And:**
					- **Assert:**
						- **Property Name:** model
						- **Property Value:** Brook trekker
					- **Assert:**
						- **Property Name:** version
						- **Property Value:** Mk9
					- **Assert:**
						- **Property Name:** versrank
						- **Property Value:** 1~2

### Common Repository
The common repository section contains information about the lighting system's circuit breakers.
* **Circuit Breaker Repository:**
	+ **Circuit Breaker Spec 1:**
		- **Circuit Breaker Ident:** CBLGT-1001-R
		- **Name:** Bike Lighting circuit breaker (right side)
		- **Functional Physical Area Ref:**
			- **System Diff Code:** AAA
			- **System Code:** DA2
			- **Sub System Code:** 2
			- **Sub Sub System Code:** 0
			- **Assy Code:** 00
		- **Circuit Breaker Ref Group:**
			- **Circuit Breaker Ref Type:** cbr02
			- **Id:** SPEC-0008
			- **Circuit Breaker Number:** CBLGT-1001-E
			- **Circuit Breaker Type:** cbt02
		- **Circuit Breaker Alts:**
			- **Circuit Breaker 1:**
				- **Id:** cb-CBLGT-1001-R.001
				- **Applic Ref Id:** app-0001
				- **Name:** CBLGT-1001-R
				- **Circuit Breaker Class:**
					- **Circuit Breaker Type:** cbt02
				- **Location:**
					- **Zone Ref:**
						- **Zone Number:** 131
	+ **Circuit Breaker Spec 2:**
		- **Circuit Breaker Ident:** CBLGT-1001-L
		- **Name:** Bike Lighting circuit breaker (left side)
		- **Functional Physical Area Ref:**
			- **System Diff Code:** AAA
			- **System Code:** DA2
			- **Sub System Code:** 2
			- **Sub Sub System Code:** 0
			- **Assy Code:** 00
		- **Circuit Breaker Ref Group:**
			- **Circuit Breaker Ref Type:** cbr02
			- **Id:** SPEC-0009
			- **Circuit Breaker Number:** CBLGT-1001-E
			- **Circuit Breaker Type:** cbt02
		- **Circuit Breaker Alts:**
			- **Circuit Breaker 1:**
				- **Id:** cb-CBLGT-1001-L.001
				- **Applic Ref Id:** app-0002
				- **Name:** CBLGT-1001-L
				- **Circuit Breaker Class:**
					- **Circuit Breaker Type:** cbt02
				- **Location:**
					- **Zone Ref:**
						- **Zone Number:** 132
	+ **Circuit Breaker Spec 3:**
		- **Circuit Breaker Ident:** CBLGT-1001-E
		- **Name:** Bike Lighting empty circuit breaker
		- **Functional Physical Area Ref:**
			- **System Diff Code:** AAA
			- **System Code:** DA2
			- **Sub System Code:** 2
			- **Sub Sub System Code:** 0
			- **Assy Code:** 00
		- **Circuit Breaker Alts:**
			- **Circuit Breaker 1:**
				- **Id:** cb-CBLGT-1001-E.001
				- **Applic Ref Id:** app-0003
				- **Name:** CBLGT-1001-E
				- **Circuit Breaker Class:**
					- **Circuit Breaker Type:** cbt02
				- **Location:**
					- **Zone Ref:**
						- **Zone Number:** 130

Note that the provided XML document contains additional information not included in this markdown representation, such as the `<circuitBreakerSpec id="SPEC-0001">` section. This information has been omitted for brevity and clarity.