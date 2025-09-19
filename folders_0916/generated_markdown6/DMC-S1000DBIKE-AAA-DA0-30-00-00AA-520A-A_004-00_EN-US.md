# DMC-S1000DBIKE-AAA-DA0-30-00-00AA-520A-A_004-00_EN-US
## Introduction
The following document is a conversion of the XML file `DMC-S1000DBIKE-AAA-DA0-30-00-00AA-520A-A_004-00_EN-US.XML` to a well-structured markdown format.

## Ident and Status Section
### DM Address
#### DM Ident
* **Model Ident Code:** S1000DBIKE
* **System Diff Code:** AAA
* **System Code:** DA0
* **Sub System Code:** 3
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** AA
* **Info Code:** 520
* **Info Code Variant:** A
* **Item Location Code:** A
#### Language
* **Country Iso Code:** US
* **Language Iso Code:** en
#### Issue Info
* **Issue Number:** 004
* **In Work:** 00

### DM Address Items
#### Issue Date
* **Year:** 2024
* **Month:** 06
* **Day:** 19
#### DM Title
##### Tech Name
Front wheel
##### Info Name
Remove procedures

## Content
### Referenced Applic Group
#### Applic 1
* **Display Text:** Mountain bicycle and Mountain storm Mk1
* **Evaluate:**
	+ **And/Or:** and
	+ **Assert:**
		- **Applic Property Ident:** type
		- **Applic Property Type:** prodattr
		- **Applic Property Values:** Mountain bicycle
	+ **Evaluate:**
		- **And/Or:** and
		- **Assert:**
			- **Applic Property Ident:** model
			- **Applic Property Type:** prodattr
			- **Applic Property Values:** Mountain storm
			- **Assert:**
				- **Applic Property Ident:** version
				- **Applic Property Type:** prodattr
				- **Applic Property Values:** Mk1

#### Applic 2
* **Display Text:** Mountain bicycle and Brook trekker Mk9
* **Evaluate:**
	+ **And/Or:** and
	+ **Assert:**
		- **Applic Property Ident:** type
		- **Applic Property Type:** prodattr
		- **Applic Property Values:** Mountain bicycle
	+ **Evaluate:**
		- **And/Or:** and
		- **Assert:**
			- **Applic Property Ident:** model
			- **Applic Property Type:** prodattr
			- **Applic Property Values:** Brook trekker
			- **Assert:**
				- **Applic Property Ident:** version
				- **Applic Property Type:** prodattr
				- **Applic Property Values:** Mk9

### Warnings and Cautions
#### Caution 1
* **Warning and Caution Para:** Be sure to operate on a white surface in order to prevent lost of part that could fall on the floor.

### Procedure
#### Preliminary Requirements
##### Required Conditions
No conditions required.
##### Required Persons
No persons required.
##### Required Support Equipment
| Name | Ident Number | Required Quantity |
| --- | --- | --- |
| Specialist toolset | KZ666 BSK-TLST-001 | 1 EA |
##### Required Supplies
| Supply Ref | Supply Number | Supply Number Type | Required Quantity |
| --- | --- | --- | --- |
| SPEC-0012 | BKO200 | sp01 | As Required |
| SPEC-0013 | EU-OIL3212 |  | As Required |
##### Required Spares
No spares required.
##### Required Safety
No safety requirements.

#### Main Procedure
1. **Open the light circuit breaker located on the handlebar**
	* Circuit Breaker Descr Group:
		+ Applic Ref Id: app-0002
		+ Circuit Breaker Action: open
		+ Circuit Breaker Descr:
			- Circuit Breaker Ref: CBLGT-1001-R
			- Name: Bike Lighting circuit breaker (right side)
			- Access Point Ref: any-access
			- Circuit Breaker Location: Zone 131
		+ Applic Ref Id: app-0003
		+ Circuit Breaker Action: open
		+ Circuit Breaker Descr:
			- Circuit Breaker Ref: CBLGT-1001-L
			- Name: Bike Lighting circuit breaker (left side)
			- Access Point Ref: any-access
			- Circuit Breaker Location: Zone 132
2. **Hold the front of the bicycle**
3. **Use the Specialist toolset to disengage the fork from the chainring by pushing the wheel forwards and down**
	* Caution Refs: C0001
	* Figure:
		+ Title:
		+ Graphic: ICN-C0419-S1000D0372-001-01
		+ Reason for Amendment: Addition of the wheel illustration
	* Internal Refs:
		+ Internal Ref Id: seq-0001
		+ Internal Ref Target Type: irtt05
4. **Use specific oil if the fork do not desengage easily**
	* Internal Refs:
		+ Internal Ref Id: sup-0001
		+ Internal Ref Target Type: irtt04
5. **If not available, use any oil compliant with requirements**
	* Internal Refs:
		+ Internal Ref Id: sup-0002
		+ Internal Ref Target Type: irtt04
6. **Lift the wheel away from the frame**
7. **Put the frame on the floor**

#### Close Requirements
No conditions required.

## DM Status Section
### Data Module Status
The data module status is not explicitly stated in the provided XML file. However, based on the content and structure of the file, it appears to be a maintenance or repair procedure for a bicycle.

### References
* **ICN-C0419-S1000D0372-001-01:** The illustration of the wheel.
* **SPEC-0001:** The circuit breaker description for the right side.
* **SPEC-0002:** The circuit breaker description for the left side.
* **SPEC-0003:** The circuit breaker location for the right side (Zone 131).
* **SPEC-0004:** The circuit breaker location for the left side (Zone 132).
* **SPEC-0005:** The access point reference for the right side.
* **SPEC-0006:** The access point reference for the left side.
* **SPEC-0007:** The circuit breaker description for the right side.
* **SPEC-0008:** The circuit breaker description for the left side.
* **SPEC-0009:** The circuit breaker description group.
* **SPEC-0010:** The graphic illustration of the wheel.
* **SPEC-0011:** The warning and caution section.
* **SPEC-0012:** The supply reference for the specific oil (BKO200).
* **SPEC-0013:** The supply requirement reference for any oil compliant with requirements (EU-OIL3212).