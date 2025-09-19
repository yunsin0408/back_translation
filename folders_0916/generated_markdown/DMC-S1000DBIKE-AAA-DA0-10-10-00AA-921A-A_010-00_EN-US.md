# DMC-S1000DBIKE-AAA-DA0-10-10-00AA-921A-A_010-00_EN-US
## Ident and Status Section
### DM Address
The DM address section contains the following information:
* **DM Ident**
	+ Model ident code: `S1000DBIKE`
	+ System diff code: `AAA`
	+ System code: `DA0`
	+ Sub system code: `1`
	+ Sub sub system code: `0`
	+ Assy code: `10`
	+ Disassy code: `00`
	+ Disassy code variant: `AA`
	+ Info code: `921`
	+ Info code variant: `A`
	+ Item location code: `A`
* **Language**
	+ Country iso code: `US`
	+ Language iso code: `en`
* **Issue Info**
	+ Issue number: `010`
	+ In work: `00`

### DM Address Items
The DM address items section contains the following information:
* **Issue Date**
	+ Year: `2024`
	+ Month: `06`
	+ Day: `19`
* **DM Title**
	+ Tech name: `Inner tube`
	+ Info name: `Remove and install a new item`

### DM Status
The DM status section contains the following information:
* **Issue Type**: `changed`
* **Security**
	+ Security classification: `01`
	+ Commercial classification: `cc51`
	+ Caveat: `cv51`
* **Data Restrictions**
	+ Data distribution: `To be made available to all S1000D users.`
	+ Export control:
		- Export registration statement: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
	+ Data handling: `There are no specific handling instructions for this data module.`
	+ Data destruction: `Users may destroy this data module in accordance with their own local procedures.`
	+ Data disclosure: `There are no dissemination limitations that apply to this data module.`
* **Restriction Info**
	+ Copyright:
		- `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
		- Publishers:
			1. Aerospace, Security and Defence Industries Association of Europe
			2. Aerospace Industries Association of America
			3. ATA e-Business Program
		- Limitations of liability:
			1. This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
			2. Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
			3. Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
	+ Policy statement: `S1000D-SC-2016-017-002-00 Steering Committee TOR`
	+ Data conditions: `There are no known conditions that would change the data restrictions for, or security classification of, this data module.`
* **Responsible Partner Company**
	+ Enterprise code: `B6865`
	+ Enterprise name: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`
* **Originator**
	+ Enterprise code: `B6865`
	+ Enterprise name: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`
* **Applic Cross Ref Table Ref**
	+ DM ref:
		- Model ident code: `S1000DBIKE`
		- System diff code: `AAA`
		- System code: `D00`
		- Sub system code: `0`
		- Sub sub system code: `0`
		- Assy code: `00`
		- Disassy code: `00`
		- Disassy code variant: `AA`
		- Info code: `00W`
		- Info code variant: `A`
		- Item location code: `D`
* **Applic**
	+ Display text: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)`
	+ Evaluate:
		- And/or: `and`
		- Assert:
			1. Applic property ident: `type`
				- Applic property type: `prodattr`
				- Applic property values: `Mountain bicycle`
		- Evaluate:
			- And/or: `or`
			- Evaluate:
				- And/or: `and`
				- Assert:
					1. Applic property ident: `model`
						- Applic property type: `prodattr`
						- Applic property values: `Mountain storm`
					2. Applic property ident: `version`
						- Applic property type: `prodattr`
						- Applic property values: `Mk1`
			- Evaluate:
				- And/or: `and`
				- Assert:
					1. Applic property ident: `model`
						- Applic property type: `prodattr`
						- Applic property values: `Brook trekker`
					2. Applic property ident: `version`
						- Applic property type: `prodattr`
						- Applic property values: `Mk1`
* **Tech Info**
	+ Authority:
	+ Review date:

## Content
### Refs
The refs section contains the following information:
* **DM Ref**
	+ Model ident code: `S1000DBIKE`
	+ System diff code: `AAA`
	+ System code: `DA0`
	+ Sub system code: `1`
	+ Sub sub system code: `0`
	+ Assy code: `20`
	+ Disassy code: `00`
	+ Disassy code variant: `AA`
	+ Info code: `215`
	+ Info code variant: `A`
	+ Item location code: `A`

### Procedure
The procedure section contains the following information:
* **Preliminary Rqmts**
	+ Req cond group:
		- Req cond: `The tire is removed.`
		- DM ref:
			1. Model ident code: `S1000DBIKE`
				- System diff code: `AAA`
				- System code: `DA0`
				- Sub system code: `1`
				- Sub sub system code: `0`
				- Assy code: `20`
				- Disassy code: `00`
				- Disassy code variant: `AA`
				- Info code: `215`
				- Info code variant: `A`
				- Item location code: `A`
	+ Req persons:
		- Person man: `A`
			1. Person category person category code: `Basic user`
			2. Trade: `Operator`
			3. Estimated time unit of measure: `h`
			4. Estimated time value: `0,3`
	+ Req support equips:
		- No support equips
	+ Req supplies:
		- No supplies
	+ Req spares:
		- Spare descr group:
			1. Spare descr id: `spa-0001`
				- Name: `Inner tube`
				- Ident number:
					1. Manufacturer code: `KT222`
					2. Part and serial number:
						1. Part number: `IT-001`
				- Req quantity unit of measure: `EA`
				- Req quantity value: `1`
	+ Req safety:
		- Safety rqmts:
			1. Caution:
				- Warning and caution para: `Be careful with sharp or hard tools. They can cause damage to the inner tube.`
* **Main Procedure**
	+ Procedural step:
		- Para: `Remove the old inner-tube.`
		- Figure id: `fig-0001`
			1. Title: `Removing the inner tube`
			2. Graphic info entity ident: `ICN-C0419-S1000D0369-001-01`
	+ Procedural step:
		- Para: `Install the new <internalRef internalRefId="spa-0001" internalRefTargetType="irtt06"/>.`
* **Close Rqmts**
	+ Req cond group:
		- Req cond no ref:
			1. Req cond: `Replace the tire.`
		- Req cond dm:
			1. Req cond: `Inflate the tire with air.`
			2. DM ref:
				1. Model ident code: `S1000DBIKE`
					- System diff code: `AAA`
					- System code: `DA0`
					- Sub system code: `1`
					- Sub sub system code: `0`
					- Assy code: `20`
					- Disassy code: `00`
					- Disassy code variant: `AA`
					- Info code: `215`
					- Info code variant: `A`
					- Item location code: `A`