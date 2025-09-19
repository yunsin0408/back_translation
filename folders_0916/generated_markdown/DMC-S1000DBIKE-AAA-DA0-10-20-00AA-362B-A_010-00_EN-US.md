# DMC-S1000DBIKE-AAA-DA0-10-20-00AA-362B-A_010-00_EN-US
## Ident and Status Section
### DM Address
The DM address contains the following information:
* **DM Ident**:
	+ Model Ident Code: `S1000DBIKE`
	+ System Diff Code: `AAA`
	+ System Code: `DA0`
	+ Sub System Code: `1`
	+ Sub Sub System Code: `0`
	+ Assy Code: `20`
	+ Disassy Code: `00`
	+ Disassy Code Variant: `AA`
	+ Info Code: `362`
	+ Info Code Variant: `B`
	+ Item Location Code: `A`
* **Language**:
	+ Country ISO Code: `US`
	+ Language ISO Code: `en`
* **Issue Info**:
	+ Issue Number: `010`
	+ In Work: `00`

### DM Address Items
The DM address items contain the following information:
* **Issue Date**: 
	+ Year: `2024`
	+ Month: `06`
	+ Day: `19`
* **DM Title**:
	+ Tech Name: `Tire`
	+ Info Name: `Check pressure`
	+ Info Name Variant: `Use pressure gauge`

### DM Status
The DM status contains the following information:
* **Issue Type**: `changed`
* **Security**:
	+ Security Classification: `01`
	+ Commercial Classification: `cc51`
	+ Caveat: `cv51`
* **Data Restrictions**:
	+ Restriction Instructions:
		- Data Distribution: `To be made available to all S1000D users.`
		- Export Control:
			- Export Registration Statement: 
				```markdown
Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
```
		- Data Handling: `There are no specific handling instructions for this data module.`
		- Data Destruction: `Users may destroy this data module in accordance with their own local procedures.`
		- Data Disclosure: `There are no dissemination limitations that apply to this data module.`
	+ Restriction Info:
		- Copyright:
			```markdown
Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
Publishers:
* Aerospace, Security and Defence Industries Association of Europe
* Aerospace Industries Association of America
* ATA e-Business Program
Limitations of liability:
* This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
* Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
* Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
```
			- Copyright Details: `The details for copyright can be found in the S1000D Specification.`
		- Policy Statement: `S1000D-SC-2016-017-002-00 Steering Committee TOR`
		- Data Conditions: `There are no known conditions that would change the data restrictions for, or security classification of, this data module.`

### Responsible Partner Company
* **Enterprise Code**: `B6865`
* **Enterprise Name**: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`

### Originator
* **Enterprise Code**: `B6865`
* **Enterprise Name**: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`

### Applic Cross Ref Table Ref
The applic cross ref table ref contains the following information:
* **DM Ref**:
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
The applic contains the following information:
* **Display Text**: 
	```markdown
Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
```
* **Evaluate**:
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
				- Applic Property Values: `Mk1`

### Tech Notes
* No tech notes available.

## Content
The content contains the following information:

### Refs
The refs contain the following information:
* **DM Ref**:
	+ DM Ref Ident:
		- Model Ident Code: `S1000DBIKE`
		- System Diff Code: `AAA`
		- System Code: `DA0`
		- Sub System Code: `1`
		- Sub Sub System Code: `0`
		- Assy Code: `20`
		- Disassy Code: `00`
		- Disassy Code Variant: `AA`
		- Info Code: `215`
		- Info Code Variant: `A`
		- Item Location Code: `A`

### Procedure
The procedure contains the following information:
* **Preliminary Rqmts**:
	+ Req Cond Group:
		- No Conds: 
	+ Req Persons:
		- Person Man: `A`
		- Person Category: 
			- Person Category Code: `Basic user`
		- Trade: `Operator`
		- Estimated Time:
			- Unit Of Measure: `h`
			- Value: `0.3`
	+ Req Support Equips:
		- Support Equip Descr Group:
			- Support Equip Descr Id: `seq-0003`
			- Name: `Tire pressure gauge`
			- Ident Number:
				- Manufacturer Code: `KZ666`
				- Part And Serial Number:
					- Part Number: `BSK-TLST-001-01`
			- Req Quantity:
				- Unit Of Measure: `EA`
				- Value: `1`

### Main Procedure
The main procedure contains the following information:
* **Procedural Step**:
	+ Para: 
		```markdown
Locate the valve stem of tire.
```
* **Procedural Step**:
	+ Para: 
		```markdown
Use the tire pressure gauge (<internalRef internalRefId="seq-0003" internalRefTargetType="irtt05"/>) to check the tire pressure.
```
* **Procedural Step**:
	+ Para: 
		```markdown
Tire pressure should between 2000 hPa to 2700 hPa.
```
	+ Procedural Step:
		- Para: 
			```markdown
If tire pressure is less than 2000 hPa inflate tire. Refer to <dmRef>
				<dmRefIdent>
					<dmCode modelIdentCode="S1000DBIKE" systemDiffCode="AAA" systemCode="DA0" subSystemCode="1" subSubSystemCode="0" assyCode="20" disassyCode="00" disassyCodeVariant="AA" infoCode="215" infoCodeVariant="A" itemLocationCode="A"/>
				</dmRefIdent>
			</dmRef>
```
	+ Procedural Step:
		- Para: 
			```markdown
If the tire cannot maintain pressure or the tire pressure is greater than 2700 hPa replace the inner tube. Refer to <dmRef>
				<dmRefIdent>
					<dmCode modelIdentCode="S1000DBIKE" systemDiffCode="AAA" systemCode="DA0" subSystemCode="1" subSubSystemCode="0" assyCode="10" disassyCode="00" disassyCodeVariant="AA" infoCode="921" infoCodeVariant="A" itemLocationCode="A"/>
				</dmRefIdent>
			</dmRef>
```

### Close Rqmts
The close rqmts contain the following information:
* **Req Cond Group**:
	+ No Conds: