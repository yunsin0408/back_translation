# Introduction to s1kd-brexcheck
The `s1kd-brexcheck` tool is used for checking S1000D CSDB objects against BREX (Business Rules eXchange) data modules.

## Command-Line Options
The following options are available:

* `-b`: Specify a BREX file to validate against.
* `-c`: Enable checking of object values specified in the BREX module.
* `-q` or `--quiet`: Disable printing of errors to stderr.
* `-r` or `--recursive`: Recursively check all CSDB objects found under the given directory path.
* `-v` or `--verbose`: Increase verbosity of output.
* `-x` or `--xpath`: Specify an XPath expression for use with the `-c` option.

## Exit Status
The exit status of the tool is as follows:

1. **0**: Check completed successfully, and no CSDB objects had BREX errors.
2. **1**: Check completed successfully, but some CSDB objects had BREX errors.
3. **2**: One or more CSDB objects specified could not be read.
4. **3**: A referenced BREX data module could not be found.
5. **5**: The number of paths or CSDB objects specified exceeded the available memory.

## Example Usage
```bash
$ DMOD=DMC-EX-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
$ BREX=DMC-S1000D-G-04-10-0301-00A-022A-D_001-00_EN-US.XML
$ s1kd-brexcheck -b $BREX $DMOD
```

## XML Report Format
The tool can generate an XML report of the BREX errors found. The format is as follows:
```xml
<?xml version="1.0"?>
<brexCheck>
  <document path="DMC-EX-A-00-00-00-00A-040A-D_000-01_EN-CA.XML">
    <brex path="DMC-S1000D-G-04-10-0301-00A-022A-D_001-00_EN-US.XML">
      <error fail="yes">
        <brDecisionRef brDecisionIdentNumber="BREX-S1-00052"/>
        <objectPath allowedObjectFlag="0">...</objectPath>
        <objectUse>Only when the reference target is a step can the value of attribute internalRefTargetType be irtt08 (Chap 3.9.5.2.1.2, Para 2.1).</objectUse>
        <object line="52" xpath="/dmodule[1]/content[1]/description[1]/para[2]/internalRef[1]">
          <internalRef internalRefId="stp-0001" internalRefTargetType="irtt08"/>
        </object>
      </error>
    </brex>
  </document>
</brexCheck>
```

## Supported XPath Syntax
The supported XPath syntax depends on the XPath engine used:

* **libxml2 (default)**: XPath 1.0, partial support for EXSLT functions.
* **Saxon (experimental)**: XPath 1.0, XPath 2.0, XPath 3.0.

Information on which XPath engine is in use can be obtained from the `--version` option.

## Object Value Checking
The tool supports checking of object values specified in the BREX module using the `-c` option. The `valueForm` attribute can be used to specify what kind of notation the `valueAllowed` attribute will contain:

* **single**: A single, exact value.
* **range**: Values given in the S1000D range/set notation (e.g., "a~c" or "a|b|c").
* **pattern**: A regular expression.

If the `valueForm` attribute is omitted, it will assume the value is in the **single** notation.