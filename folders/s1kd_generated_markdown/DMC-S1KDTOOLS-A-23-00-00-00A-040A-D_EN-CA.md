# DMC-S1KDTOOLS-A-23-00-00-00A-040A-D_EN-CA
## Ident and Status Section
### DM Address
The `dmAddress` section contains the following information:
* **DM Ident**: 
  + modelIdentCode: S1KDTOOLS
  + systemDiffCode: A
  + systemCode: 23
  + subSystemCode: 0
  + subSubSystemCode: 0
  + assyCode: 00
  + disassyCode: 00
  + disassyCodeVariant: A
  + infoCode: 040
  + infoCodeVariant: A
  + itemLocationCode: D
* **Language**:
  + languageIsoCode: en
  + countryIsoCode: CA
* **Issue Info**:
  + issueNumber: 025
  + inWork: 00

### DM Address Items
The `dmAddressItems` section contains the following information:
* **Issue Date**: 
  + year: 2020
  + month: 09
  + day: 01
* **DM Title**:
  + techName: s1kd-flatten
  + infoName: Description

## DM Status
The `dmStatus` section contains the following information:
* **Issue Type**: changed
* **Security Classification**: 01
* **Responsible Partner Company**: khzae.net
* **Originator**: khzae.net
* **Applic**:
  + displayText: All
* **BrexDmRef**:
  + dmRefIdent:
    - modelIdentCode: S1KDTOOLS
    - systemDiffCode: A
    - systemCode: 00
    - subSystemCode: 0
    - subSubSystemCode: 0
    - assyCode: 00
    - disassyCode: 00
    - disassyCodeVariant: A
    - infoCode: 022
    - infoCodeVariant: A
    - itemLocationCode: D
* **Quality Assurance**: unverified
* **Reason for Update**:
  + id: rfu-xml-catalog
  + updateHighlight: 1
  + updateReasonType: urt02
  + simplePara: Add --xml-catalog parser option.

## Content
### Description
The `description` section contains the following information:

#### General
The `s1kd-flatten` tool combines a publication module and the data modules it references into a single file for use with a publishing system.
Data modules are by default searched for in the current directory using the data module code, language and/or issue info provided in each reference.

#### Usage
```bash
s1kd-flatten [-d <dir>] [-I <path>] [-cDfimNPpqRruvx] <PM> [<DM>...]
```

#### Options
The following options are available:
| Option | Description |
| --- | --- |
| -c, --containers | Flatten referenced container data modules by copying the references inside the container directly into the publication module. The copied references will also be flattened, unless the -m option is specified. |
| -D, --remove | Remove unresolved references. |
| -d, --dir <dir> | Directory to start search in. By default, the current directory is used. |
| -f, --overwrite | Overwrite input publication module instead of writing to stdout. |
| -h, -?, --help | Show help/usage message. |
| -I, --include <path> | Add <path> to the list of directories that the tool will search when resolving references. |
| -i, --ignore-issue | Always match the latest issue of an object found, regardless of the issue specified in the reference. |
| -m, --modify | Modify the references in the publication module without flattening them. |
| -N, --omit-issue | Assume that the files representing the referenced data modules do not include the issue info in their filenames, i.e. they were created using the -N option of the s1kd-new* tools. |
| -P, --only-pm-refs | Only flatten PM references, leaving DM references alone. |
| -p, --simple | Instead of the hierarchical PM-based format, use a simpler "flat" format. |
| -q, --quiet | Quiet mode. Errors are not printed. |
| -R, --recursively | Recursively flatten referenced publication modules, copying their content into the "master" publication module. |
| -r, --recursive | Search directories recursively. |
| -u, --unique | Remove duplicate references within the PM content. |
| -v, --verbose | Verbose output. Specify multiple times to increase the verbosity. |
| -x, --use-xinclude | Use XInclude rather than copying each data module's contents directly inside the publication module. DTD entities in data modules will only be carried over to the final publication when using this option, otherwise they do not carry over when copying the data module. |
| --version | Show version information. |
| <DM>... | When using the -p option, the filenames to include can be specified manually as additional arguments instead of searching for them in the current directory. When not using the -p option, additional arguments are ignored. |
| <PM> | The publication module to flatten. |

In addition, the following options allow configuration of the XML parser:
| Option | Description |
| --- | --- |
| --dtdload | Load the external DTD. |
| --huge | Remove any internal arbitrary parser limits. |
| --net | Allow network access to load external DTD and entities. |
| --noent | Resolve entities. |
| --parser-errors | Emit errors from parser. |
| --parser-warnings | Emit warnings from parser. |
| --xinclude | Do XInclude processing. |
| --xml-catalog <file> | Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times. |

#### Exit Status
The following exit statuses are available:
| Code | Description |
| --- | --- |
| 0 | No errors. |
| 1 | The publication module specified is malformed. |
| 2 | An encoding error occurred. |

#### Example
```bash
$ s1kd-flatten -x PMC-EX-12345-00001-00_001-00_EN-CA.XML > Book.xml
```