Options for s1kd-newdm
========================
### Overview

The `s1kd-newdm` command is used to create new S1000D data modules. The following options are available:

### Options

* `-#`: Specify the DM identifier (e.g., `S1KDTOOLS-A-00-07-00-00A-040A-D`)
* `-a`, `--author`: Specify the author name
* `-c`, `--country`: Specify the country ISO code
* `-d`, `--defaults`: Specify the path to a `.defaults` file
* `-D`, `--dm-types`: Specify the path to a `.dmtypes` file
* `-f`, `--file-name`: Specify the output file name
* `-h`, `--help`: Display help and usage information
* `-i`, `--info-code`: Specify the info code
* `-I`, `--issue`: Specify the S1000D issue (default: 5.0)
* `-l`, `--language`: Specify the language ISO code
* `-n`, `--no-validate`: Disable validation of DM metadata and content
* `-o`, `--originator`: Specify the originator name
* `-p`, `--path`: Specify the output directory path
* `-q`, `--quiet`: Suppress warnings and information messages
* `-r`, `--responsible-partner-company`: Specify the responsible partner company name
* `-s`, `--security-classification`: Specify the security classification (1-5)
* `-S`, `--schema`: Specify the schema identifier (e.g., `descript`)
* `-t`, `--template`: Specify a custom template directory path
* `-T`, `--type`: Specify the data module type (e.g., `dm`)
* `-v`, `--verbose`: Display detailed information and debug messages
* `-V`, `--version`: Display version information

### Defaults File

The `.defaults` file sets default values for each piece of metadata. The file should be named `.defaults` and located in the current directory or a parent directory.

Example:
```markdown
# General
countryIsoCode               CA
languageIsoCode              en
originator                   khzae.net
responsiblePartnerCompany    khzae.net
securityClassification       01
```
Alternatively, the `.defaults` file can be written in an XML format:
```xml
<?xml version="1.0"?>
<defaults>
    <!-- General -->
    <default ident="countryIsoCode" value="CA"/>
    <default ident="languageIsoCode" value="en"/>
    <default ident="originator" value="khzae.net"/>
    <default ident="responsiblePartnerCompany" value="khzae.net"/>
    <default ident="securityClassification" value="01"/>
</defaults>
```
### DM Types File

The `.dmtypes` file sets the default schema and info name for data modules based on their info code. The file should be named `.dmtypes` and located in the current directory or a parent directory.

Example:
```markdown
000    descript
022    brex        Business rules
040    descript    Description
520    proced      Remove procedure
```
Alternatively, the `.dmtypes` file can be written in an XML format:
```xml
<?xml version="1.0"?>
<dmtypes>
    <type infoCode="000" schema="descript"/>
    <type infoCode="022" schema="brex" infoName="Business rules"/>
    <type infoCode="040" schema="descript" infoName="Description"/>
    <type infoCode="520" schema="proced" infoName="Remove procedure"/>
</dmtypes>
```
### Custom XML Templates

Customized templates may be used with the `-%` option. This option takes a path to a directory where the custom templates are located.

Example:
```bash
$ s1kd-newdm -% /path/to/custom/templates
```
Each template should be named `<schema>.xml`, where `<schema>` is the name of the schema, matching one of the schema names in the `.dmtypes` file or the schema specified with the `-T` option.

### Example

```bash
$ s1kd-newdm -# S1KDTOOLS-A-00-07-00-00A-040A-D
```
This command creates a new data module with the specified DM identifier.