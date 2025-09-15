# s1kd-fmgen
The `s1kd-fmgen` command is used to generate the content for front matter data modules.

## Overview
The `s1kd-fmgen` command takes the output of the `s1kd-flatten` command and generates the content for front matter data modules. It supports various options to customize the generation process.

## Options
The following options are available:

* `-f`: Overwrite the output file if it already exists.
* `-D`: Dump the built-in XSLT for a type of front matter as a starting point for a custom script.
* `-F`: Specify a custom `.fmtypes` file.
* `-I`: Set the date to use when generating the front matter content.
* `-l`: Specify the language to use when generating the front matter content.
* `-x`: Specify an XSLT file to use instead of the built-in one.

## .fmtypes File
The `.fmtypes` file specifies a list of info codes to associate with a particular type of front matter. It can be in simple text format or XML format.

### Simple Text Format
Each line in the file consists of an info code and a type of front matter, separated by whitespace:
```
001    TP
005    LOA
006    LOT
007    LOS
009    TOC
00A    LOA
00S    LOEDM
00U    HIGH    fm/high.xsl
00V    LOASD
00Z    LOTBL
```

### XML Format
The XML format uses an `<fmtypes>` element to contain a list of `<fm>` elements:
```xml
<fmtypes>
  <fm infoCode="001" type="TP"/>
  <fm infoCode="005" type="LOA"/>
  <fm infoCode="006" type="LOT"/>
  <fm infoCode="007" type="LOS"/>
  <fm infoCode="009" type="TOC"/>
  <fm infoCode="00A" type="LOI"/>
  <fm infoCode="00S" type="LOEDM"/>
  <fm infoCode="00U" type="HIGH" xsl="fm/high.xsl"/>
  <fm infoCode="00V" type="LOASD"/>
  <fm infoCode="00Z" type="LOTBL"/>
</fmtypes>
```

## Optional Title Page Elements
When re-generating the front matter content for a title page data module, optional elements which cannot be derived from the publication module (such as the product illustration or bar code) will be copied from the source data module when updating it.

## Multi-Pass Transforms
The path specified for the `xsl` attribute in the `.fmtypes` file or the `-x` option may be an XProc file which contains a pipeline with multiple stylesheets. This allows for multi-pass transformations.

### Example XProc File
```xml
<p:pipeline
  xmlns:p="http://www.w3.org/ns/xproc"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  version="1.0">
  <p:xslt name="Pass 1">
    <p:input port="stylesheet">
      <p:document href="pass1.xsl"/>
    </p:input>
    <p:with-param name="update-instr" select="true()"/>
  </p:xslt>
  <p:xslt name="Pass 2">
    <p:input port="stylesheet">
      <p:inline>
        <xsl:transform version="1.0">
          ...
        </xsl:transform>
      </p:inline>
    </p:input>
  </p:xslt>
</p:pipeline>
```

## Exit Status
The following exit status codes are used:

* `0`: No errors.
* `1`: The date specified with `-I` is invalid.
* `2`: No front matter types were specified.
* `3`: An unknown front matter type was specified.
* `4`: The resulting front matter content could not be merged into a data module.
* `5`: The stylesheet specified for a type of front matter was invalid.

## Example Usage
Generate the content for a title page front matter data module and overwrite the file:
```bash
$ s1kd-flatten PMC-EX-12345-00001-00_001-00_EN-CA.XML |
  > s1kd-fmgen -f DMC-EX-A-00-00-00-00A-001A-D_001-00_EN-CA.XML
```