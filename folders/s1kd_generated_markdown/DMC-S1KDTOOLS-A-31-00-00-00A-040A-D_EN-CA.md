# DMC-S1KDTOOLS-A-31-00-00-00A-040A-D_EN-CA
## Introduction
The following document is based on the XML file `DMC-S1KDTOOLS-A-31-00-00-00A-040A-D_EN-CA.XML`.

### Ident and Status Section
#### DM Address
##### DM Ident
* **Model Ident Code:** S1KDTOOLS
* **System Diff Code:** A
* **System Code:** 31
* **Sub System Code:** 0
* **Sub Sub System Code:** 0
* **Assy Code:** 00
* **Disassy Code:** 00
* **Disassy Code Variant:** A
* **Info Code:** 040
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:**
	+ **Language Iso Code:** en
	+ **Country Iso Code:** CA
* **Issue Info:**
	+ **Issue Number:** 019
	+ **In Work:** 00

##### DM Address Items
* **Issue Date:**
	+ **Year:** 2020
	+ **Month:** 09
	+ **Day:** 01
* **DM Title:**
	+ **Tech Name:** s1kd-newupf
	+ **Info Name:** Description

#### DM Status
* **Issue Type:** changed
* **Security:**
	+ **Security Classification:** 01
* **Responsible Partner Company:**
	+ **Enterprise Name:** khzae.net
* **Originator:**
	+ **Enterprise Name:** khzae.net
* **Applic:**
	+ **Display Text:**
		- All
* **BrexDm Ref:**
	+ **DM Ref:**
		- **DM Ref Ident:**
			- **Model Ident Code:** S1KDTOOLS
			- **System Diff Code:** A
			- **System Code:** 00
			- **Sub System Code:** 0
			- **Sub Sub System Code:** 0
			- **Assy Code:** 00
			- **Disassy Code:** 00
			- **Disassy Code Variant:** A
			- **Info Code:** 022
			- **Info Code Variant:** A
			- **Item Location Code:** D
* **Quality Assurance:**
	+ Unverified
* **Reason for Update:**
	+ **Id:** rfu-xml-catalog
	+ **Update Highlight:** 1
	+ **Update Reason Type:** urt02
	+ **Simple Para:** Add --xml-catalog parser option.

## Content
### Refs
#### DM Ref
* **DM Ref Ident:**
	+ **Model Ident Code:** S1KDTOOLS
	+ **System Diff Code:** A
	+ **System Code:** 07
	+ **Sub System Code:** 0
	+ **Sub Sub System Code:** 0
	+ **Assy Code:** 00
	+ **Disassy Code:** 00
	+ **Disassy Code Variant:** A
	+ **Info Code:** 040
	+ **Info Code Variant:** A
	+ **Item Location Code:** D
* **DM Ref Address Items:**
	+ **DM Title:**
		- **Tech Name:** s1kd-newdm
		- **Info Name:** Description

### Description
#### General
The `s1kd-newupf` tool creates a new S1000D data update file for two specified issues of a CIR data module. Changes to items between the source and target issues of the CIR are recorded in the resulting UPF, along with update instructions.

#### Usage
```bash
s1kd-newupf [options] <SOURCE> <TARGET>
```

#### Options
The following options are available:
* **-$, --issue &lt;issue&gt;:** Specify which issue of S1000D to use. Currently supported issues are:
	+ 5.0 (default)
	+ 4.2
	+ 4.1
* **-@, --out &lt;path&gt;:** Save the new update file to &lt;path&gt;. If &lt;path&gt; is an existing directory, the update file will be created in it instead of the current directory. Otherwise, the update file will be saved as the filename &lt;path&gt; instead of being automatically named.
* **-%, --templates &lt;dir&gt;:** Use XML template in the specified directory instead of the built-in template. The template must be named `update.xml` in the directory &lt;dir&gt;, and must conform to the default S1000D issue of this tool (5.0).
* **-~, --dump-templates &lt;dir&gt;:** Dump the built-in XML template to the specified directory.
* **-d, --defaults &lt;file&gt;:** Specify the `.defaults` file name.
* **-f, --overwrite:** Overwrite existing file.
* **-h, -?, --help:** Show help/usage message.
* **-q, --quiet:** Do not report an error when the file already exists.
* **-v, --verbose:** Print the file name of the newly created data update file.
* **--version:** Show version information.
* **&lt;SOURCE&gt;:** The source (original) issue of the CIR data module.
* **&lt;TARGET&gt;:** The target (updated) issue of the CIR data module.

Additional options for configuring the XML parser:
* **--dtdload:** Load the external DTD.
* **--huge:** Remove any internal arbitrary parser limits.
* **--net:** Allow network access to load external DTD and entities.
* **--noent:** Resolve entities.
* **--parser-errors:** Emit errors from parser.
* **--parser-warnings:** Emit warnings from parser.
* **--xinclude:** Do XInclude processing.
* **--xml-catalog &lt;file&gt;:** Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times.

#### .defaults file
Refer to [s1kd-newdm](#) for information on the `.defaults` file which is used by all the s1kd-new* commands.

#### Example
```bash
$ s1kd-newupf \
    DMC-EX-A-00-00-00-00A-00GA-D_001-00_EN-CA.XML \
    DMC-EX-A-00-00-00-00A-00GA-D_002-00_EN-CA.XML
```