# DMC-S1KDTOOLS-A-28-00-00-00A-040A-D_EN-CA
## Ident and Status Section
The ident and status section contains information about the document identification and status.

### DM Address
#### DM Ident
* **Model Ident Code:** S1KDTOOLS
* **System Diff Code:** A
* **System Code:** 28
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
	+ **Issue Number:** 018
	+ **In Work:** 00

#### DM Address Items
* **Issue Date:**
	+ **Year:** 2020
	+ **Month:** 09
	+ **Day:** 01
* **DM Title:**
	+ **Tech Name:** s1kd-index
	+ **Info Name:** Description

### DM Status
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
			- **DM Code:**
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
	+ **Unverified:**
* **Reason For Update:**
	+ **Id:** rfu-xml-catalog
	+ **Update Highlight:** 1
	+ **Update Reason Type:** urt02
	+ **Simple Para:** Add --xml-catalog parser option.

## Content
### Description
The s1kd-index tool adds index flags to a data module based on a user-defined set of keywords.

#### General
The s1kd-index tool is used to add index flags to a data module.

#### Usage
```bash
s1kd-index -h?
s1kd-index [-I <index>] [-filqv] [<module>...]
s1kd-index -D [-filqv] [<module>...]
```

#### Options
The following options are available:
* `-D, --delete`: Remove the current index flags from a data module.
* `-f, --overwrite`: Overwrite input module(s).
* `-h, -?, --help`: Show help/usage message.
* `-I, --indexflags <index>`: Flag the terms in the specified `<index>` XML file instead of the default `.indexflags` file.
* `-i, --ignore-case`: Ignore case when flagging terms.
* `-l, --list`: Treat input (stdin or arguments) as lists of filenames of data modules to add index flags to, rather than data modules themselves.
* `-q, --quiet`: Quiet mode. Errors are not printed.
* `-v, --verbose`: Verbose output.
* `--version`: Show version information.

Additional options for XML parser configuration:
* `--dtdload`: Load the external DTD.
* `--huge`: Remove any internal arbitrary parser limits.
* `--net`: Allow network access to load external DTD and entities.
* `--noent`: Resolve entities.
* `--parser-errors`: Emit errors from parser.
* `--parser-warnings`: Emit warnings from parser.
* `--xinclude`: Do XInclude processing.
* `--xml-catalog <file>`: Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times.

#### .indexflags file
The `.indexflags` file specifies the list of indexable keywords for the project and their level. By default, the program will search for a file named `.indexflags` in the current directory or parent directories, but any file can be specified using the `-I` option.
```xml
<indexFlags>
  <indexFlag indexLevelOne="bicycle"/>
  <indexFlag indexLevelOne="bicycle" indexLevelTwo="brake system"/>
</indexFlags>
```

#### Example
Given the following in a data module:
```xml
<levelledPara>
  <title>General</title>
  <para>
    The s1kd-tools are a set of small tools for manipulating S1000D XML
    data.
  </para>
</levelledPara>
```
And the following `.indexflags` file:
```xml
<indexFlags>
  <indexFlag indexLevelOne="S1000D"/>
  <indexFlag indexLevelTwo="S10000D" indexLevelTwo="s1kd-tools"/>
  <indexFlag indexLevelOne="data"/>
  <indexFlag indexLevelOne="data" indexLevelTwo="XML"/>
</indexFlags>
```
Then the s1kd-index command:
```bash
$ s1kd-index <DM>.XML
```
Would result in the following:
```xml
<levelledPara>
  <title>General</title>
  <para>
    The s1kd-tools<indexFlag indexLevelOne="S1000D"
      indexLevelTwo="s1kd-tools"/> are a set of small tools for
    manipulating S1000D<indexFlag indexLevelOne="S1000D"/>
    XML<indexFlag indexLevelOne="data" indexLevelTwo="XML"/>
    data<indexFlag indexLevelOne="data"/>.
  </para>
</levelledPara>
```