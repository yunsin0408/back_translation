# s1kd-refs Documentation
## Overview
The `s1kd-refs` tool is used to list references in CSDB objects. It can read from stdin or take one or more CSDB object(s) as input.

## Options
The following options are available:

### General Options

* `-h`, `--help`: Show help message and exit.
* `--version`: Show version information and exit.
* `<object>...`: CSDB object(s) to list references in. If none are specified, the tool will read from stdin.

### Reference Matching Options

* `-H`: Enable hotspot matching.
* `-j <xpath>`: Specify a custom XPath expression for hotspot matching.
* `-K`: Enable CSN reference matching.
* `-b <sns>`: Specify the SNS for non-chapterized IPDs.
* `-k <pattern>`: Specify the pattern for the disassembly code variant of IPDs.

### Output Options

* `-l`, `--list`: Read input from stdin as a list of files.
* `-n`, `--no-color`: Disable color output.
* `-q`, `--quiet`: Suppress warning messages.
* `-v`, `--verbose`: Increase verbosity of output.

### XML Parser Options

* `--dtdload`: Load the external DTD.
* `--huge`: Remove any internal arbitrary parser limits.
* `--net`: Allow network access to load external DTD and entities.
* `--noent`: Resolve entities.
* `--parser-errors`: Emit errors from parser.
* `--parser-warnings`: Emit warnings from parser.
* `--xinclude`: Do XInclude processing.
* `--xml-catalog <file>`: Use an XML catalog when resolving entities.

### Exit Status

The following exit status codes are used:

* `0`: No errors, all references were matched.
* `1`: Some references were unmatched.
* `2`: The number of objects found in a recursive check exceeded the available memory.
* `3`: stdin did not contain valid XML and not in list mode.
* `4`: The non-chapterized SNS specified is not valid.

## Examples
### General Example

```bash
$ s1kd-refs DMC-EX-A-00-00-00-00A-040A-D_000-01_EN-CA.XML \
             DMC-EX-A-00-00-00-00A-022A-D_001-00_EN-CA.XML \
             DMC-EX-A-01-00-00-00A-040A-D_000-01_EN-CA.XML \
             ICN-12345-00001-001-01.JPG
```

### CSN Reference Example

The following examples are based on the CSN reference:
```xml
<catalogSeqNumberRef figureNumber="01" item="004"/>
```
in the data module:
```bash
DM=DMC-EX-A-00-00-00-00AA-100A-D_001-00_EN-CA.XML
```

Because the CSN reference is not chapterized, it cannot be matched to an IPD DM without more information:
```bash
$ s1kd-refs -K $DM
Unmatched reference: Fig 01 Item 004
```
The SNS for non-chapterized IPDs can be specified with `-b`. In this case, the project uses the SNS "ZD-00-35" for their IPDs:
```bash
$ s1kd-refs -K -b ZD-00-35 $DM
Unmatched reference: DMC-EX-A-ZD-00-35-010-941A-D Item 004
```
This project uses a 2-character disassembly code variant, so the figure number variant is not sufficient to resolve the DMC of the referenced IPD data module. The `-k` option can be used in this case to specify the pattern for the disassembly code variant of IPDs. Since the second character of the disassembly code variant of all IPD DMs in this project is A, the pattern "%A" can be used:
```bash
$ s1kd-refs -K -b ZD-00-35 -k %A $DM
DMC-EX-A-ZD-00-35-010A-941A-D_001-00_EN-CA.XML Item 004
```

## .externalpubs File
The `.externalpubs` file contains definitions of external publication references. This can be used to update external publication references in CSDB objects with `-U`.

Example of a `.externalpubs` file:
```xml
<externalPubs>
  <externalPubRef>
    <externalPubRefIdent>
      <externalPubCode>ABC</externalPubCode>
      <externalPubTitle>ABC Manual</externalPubTitle>
    </externalPubRefIdent>
  </externalPubRef>
</externalPubs>
```
External publication references will be updated whether they are matched to a file or not.

## Hotspot Matching
Hotspots can be matched in XML-based ICN formats, such as SVG or X3D. By default, matching is based on the APS ID of the hotspot and the following attributes:

* `SVG`: `@id`
* `X3D`: `@DEF`

If hotspots are identified in a different way in a project's ICNs, a custom XPath expression can be specified with the `-j` option. In this XPath expression, the variable `$id` represents the hotspot APS ID:
```bash
$ s1kd-refs -H -j "//*[@attr = $id]" <DM>
```