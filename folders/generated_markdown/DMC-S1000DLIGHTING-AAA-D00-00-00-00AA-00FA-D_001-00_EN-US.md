# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00FA-D_001-00_EN-US
## Ident and Status Section
### DM Address
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
* **Language:**
	+ **Language Iso Code:** en
	+ **Country Iso Code:** US
* **Issue Info:**
	+ **Issue Number:** 001
	+ **In Work:** 00

#### DM Address Items
* **Issue Date:**
	+ **Year:** 2024
	+ **Month:** 06
	+ **Day:** 19
* **DM Title:**
	+ **Tech Name:** Lighting
	+ **Info Name:** Circuit Breaker common information repository

### DM Status
* **Issue Type:** new
* **Security:**
	+ **Security Classification:** 01
	+ **Commercial Classification:** cc51
	+ **Caveat:** cv51
* **Data Restrictions:**
	+ **Restriction Instructions:**
		- **Data Distribution:** To be made available to all S1000D users.
		- **Export Control:**
			- **Export Registration Stmt:** Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
		- **Data Handling:** There are no specific handling instructions for this data module.
		- **Data Destruction:** Users may destroy this data module in accordance with their own local procedures.
		- **Data Disclosure:** There are no dissemination limitations that apply to this data module.
	+ **Restriction Info:**
		- **Copyright:**
			- **Copyright Para:** Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
			- **Publishers:**
				1. AeroSpace, Security and Defence Industries Association of Europe - ASD
			- **Random List of Publishers:**
				* AeroSpace, Security and Defence Industries Association of Europe - ASD
				* Other Publisher 1
				* Other Publisher 2
		- **Other Restriction Info:** No other restriction info available

## Content
### Referenced Applic Group
* **Applic 1:**
	+ **Id:** app-0001
	+ **Display Text:** Mountain storm Mk1
	+ **Evaluate:**
		- **And:**
			- **Assert:**
				- **Applic Property Ident:** model
				- **Applic Property Type:** prodattr
				- **Applic Property Values:** Mountain storm
* **Applic 2:**
	+ **Id:** app-0002
	+ **Display Text:** Brook trekker Mk9
	+ **Evaluate:**
		- **And:**
			- **Assert:**
				- **Applic Property Ident:** model
				- **Applic Property Type:** prodattr
				- **Applic Property Values:** Brook trekker
* **Applic 3:**
	+ **Id:** app-0003
	+ **Display Text:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
	+ **Evaluate:**
		- **And:**
			- **Assert:**
				- **Applic Property Ident:** type
				- **Applic Property Type:** prodattr
				- **Applic Property Values:** Mountain bicycle
			- **Or:**
				- **And:**
					- **Assert:**
						- **Applic Property Ident:** model
						- **Applic Property Type:** prodattr
						- **Applic Property Values:** Mountain storm
				- **And:**
					- **Assert:**
						- **Applic Property Ident:** model
						- **Applic Property Type:** prodattr
						- **Applic Property Values:** Brook trekker

### Common Repository
* **Circuit Breaker Repository:**
	+ **Id:** SPEC-0010
	+ **Circuit Breaker Spec 1:**
		- **Id:** cb-CBLGT-1001-R
		- **Circuit Breaker Ident:**
			- **Circuit Breaker Number:** CBLGT-1001-R
		- **Name:** Bike Lighting circuit breaker (right side)
		- **Functional Physical Area Ref:**
			- **System Diff Code:** AAA
			- **System Code:** DA2
			- **Sub System Code:** 2
			- **Sub Sub System Code:** 0
			- **Assy Code:** 00
		- **Circuit Breaker Ref Group:**
			- **Id:** SPEC-0008
			- **Circuit Breaker Ref Type:** cbr02
			- **Circuit Breaker Ref:**
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
		- **Id:** cb-CBLGT-1001-L
		- **Circuit Breaker Ident:**
			- **Circuit Breaker Number:** CBLGT-1001-L
		- **Name:** Bike Lighting circuit breaker (left side)
		- **Functional Physical Area Ref:**
			- **System Diff Code:** AAA
			- **System Code:** DA2
			- **Sub System Code:** 2
			- **Sub Sub System Code:** 0
			- **Assy Code:** 00
		- **Circuit Breaker Ref Group:**
			- **Id:** SPEC-0009
			- **Circuit Breaker Ref Type:** cbr02
			- **Circuit Breaker Ref:**
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
		- **Id:** cb-CBLGT-1001-E
		- **Circuit Breaker Ident:**
			- **Circuit Breaker Number:** CBLGT-1001-E
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

Note that the provided XML data has been converted into a markdown format, with each section and subsection representing the corresponding elements in the original XML. The attribute values have been preserved and presented in a readable format.