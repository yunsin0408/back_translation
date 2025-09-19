# Introduction to S1KD Repcheck
The `s1kd-repcheck` tool is used for validating CIR (Common Information Repository) references in data modules.

## Usage
To use the `s1kd-repcheck` tool, simply run it from the command line and provide the necessary options and input files. The basic syntax is as follows:
```bash
$ s1kd-repcheck [options] <object>...
```
### Options

The following options are available:

* `-R`, `--repository`: Specify a repository to use for validation.
* `-X`, `--xsl`: Specify a custom XSLT script for extracting CIR references.
* `-D`, `--dump-xsl`: Dump the built-in XSLT script for extracting CIR references.
* `--version`: Show version information.

### Custom XSLT Script
A custom XSLT script can be used to configure which elements are extracted as CIR references and how they are validated. The script should add the following attributes to elements that will be validated:

* `type`: A name for the type of CIR reference.
* `name`: A descriptive name for the CIR reference.
* `test`: An XPath expression used to match the corresponding CIR identification element.

The namespace for these attributes must be `urn:s1kd-tools:s1kd-repcheck`.

### Exit Status
The following exit statuses are possible:

* **0**: The check completed successfully, and all CIR references were resolved.
* **1**: The check completed successfully, but some CIR references could not be resolved.
* **2**: The number of CSDB objects specified exceeded the available memory.

## Example Usage

### Part Repository
```xml
<partRepository>
  <partSpec>
    <partIdent manufacturerCodeValue="12345" partNumberValue="ABC"/>
    <itemIdentData>
      <descrForPart>ABC part</descrForPart>
    </itemIdentData>
  </partSpec>
</partRepository>
```
### Part References in a Procedure
```xml
<spareDescrGroup>
  <spareDescr>
    <partRef manufacturerCodeValue="12345" partNumberValue="ABC"/>
    <reqQuantity>1</reqQuantity>
  </spareDescr>
  <spareDescr>
    <partRef manufacturerCodeValue="12345" partNumberValue="DEF"/>
    <reqQuantity>1</reqQuantity>
  </spareDescr>
</spareDescrGroup>
```
### Command and Results
```bash
$ s1kd-repcheck -R <CIR> ... <DM>
s1kd-repcheck: ERROR: <DM> (<line>): Part 12345/DEF not found.
```
## Configuration of XML Parser

In addition to the main options, the following options allow configuration of the XML parser:

* `--dtdload`: Load the external DTD.
* `--huge`: Remove any internal arbitrary parser limits.
* `--net`: Allow network access to load external DTD and entities.
* `--noent`: Resolve entities.
* `--parser-errors`: Emit errors from parser.
* `--parser-warnings`: Emit warnings from parser.
* `--xinclude`: Do XInclude processing.
* `--xml-catalog <file>`: Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times.

### Custom XSLT Example
```xml
<xsl:template match="functionalItemRef">
  <xsl:variable name="fin" select="@functionalItemNumber"/>
  <xsl:copy>
    <xsl:apply-templates select="@*"/>
    <xsl:attribute name="s1kd-repcheck:type">fin</xsl:attribute>
    <xsl:attribute name="s1kd-repcheck:name">
      <xsl:text>Functional item </xsl:text>
      <xsl:value-of select="$fin"/>
    </xsl:attribute>
    <xsl:attribute name="s1kd-repcheck:test">
      <xsl:text>//functionalItemIdent[@functionalItemNumber='</xsl:text>
      <xsl:value-of select="$fin"/>
      <xsl:text>']</xsl:text>
    </xsl:attribute>
    <xsl:apply-templates select="node()"/>
  </xsl:copy>
</xsl:template>
```