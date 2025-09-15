# DMC-S1KDTOOLS-A-14-00-00-00A-040A-D_EN-CA
## Ident and Status Section
The following section provides identification and status information for the data module.

### DM Address
The DM address contains the following information:
* **DM Ident**: 
  + Model ident code: `S1KDTOOLS`
  + System diff code: `A`
  + System code: `14`
  + Sub system code: `0`
  + Sub sub system code: `0`
  + Assy code: `00`
  + Disassy code: `00`
  + Disassy code variant: `A`
  + Info code: `040`
  + Info code variant: `A`
  + Item location code: `D`
* **Language**: 
  + Language iso code: `en`
  + Country iso code: `CA`
* **Issue Info**:
  + Issue number: `024`
  + In work: `00`

### DM Address Items
The following items are included in the DM address:
* **Issue Date**: 
  + Year: `2020`
  + Month: `09`
  + Day: `01`
* **DM Title**:
  + Tech name: `s1kd-neutralize`
  + Info name: `Description`

### DM Status
The current status of the data module is:
* **Issue Type**: `changed`
* **Security**: 
  + Security classification: `01`
* **Responsible Partner Company**:
  + Enterprise name: `khzae.net`
* **Originator**:
  + Enterprise name: `khzae.net`
* **Applic**:
  + Display text: `All`
* **BrexDmRef**:
  + DM ref ident:
    - Model ident code: `S1KDTOOLS`
    - System diff code: `A`
    - System code: `00`
    - Sub system code: `0`
    - Sub sub system code: `0`
    - Assy code: `00`
    - Disassy code: `00`
    - Disassy code variant: `A`
    - Info code: `022`
    - Info code variant: `A`
    - Item location code: `D`
* **Quality Assurance**:
  + Unverified
* **Reason for Update**:
  + ID: `rfu-xml-catalog`
  + Update highlight: `1`
  + Update reason type: `urt02`
  + Simple para: `Add --xml-catalog parser option.`

## Content
The following section provides the content of the data module.

### Description
The description includes the following information:
#### General
Generates neutral metadata for the specified CSDB objects. This includes:
* XLink attributes for references, using the S1000D URN scheme.
* RDF and Dublin Core metadata.

#### Usage
```bash
s1kd-neutralize [-o <file>] [-Dflnqvh?] [<object>...]
```

#### Options
The following options are available:
| Option | Description |
| --- | --- |
| -D, --delete | Remove neutral metadata from the CSDB object. |
| -f, --overwrite | Overwrite specified CSDB object(s) automatically. |
| -h, -?, --help | Show usage message. |
| -l, --list | Treat input (stdin or arguments) as lists of CSDB objects to neutralize, rather than CSDB objects themselves. |
| -n, --namespace | Include the IETP namespaces for data module and publication module elements. |
| -o, --out <file> | Output neutralized CSDB object XML to <file> instead of stdout. |
| -q, --quiet | Quiet mode. Errors are not printed. |
| -v, --verbose | Verbose output. |
| --version | Show version information. |

Additional options for configuring the XML parser:
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

#### Example
```bash
$ DMOD=DMC-XLINKTEST-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
$ xmllint --xpath "//description/dmRef" $DMOD
<dmRef>
  <dmRefIdent>
    <dmCode modelIdentCode="XLINKTEST" systemDiffCode="A"
           systemCode="00" subSystemCode="0" subSubSystemCode="0" assyCode="01"
           disassyCode="00" disassyCodeVariant="A" infoCode="040"
           infoCodeVariant="A" itemLocationCode="D"/>
  </dmRefIdent>
  <dmRefAddressItems>
    <dmTitle>
      <techName>XLink test</techName>
      <infoName>Referenced data module</infoName>
    </dmTitle>
  </dmRefAddressItems>
</dmRef>

$ s1kd-neutralize $DMOD | xmllint --xpath "//description/dmRef" -
<dmRef xlink:type="simple"
       xlink:href="URN:S1000D:DMC-XLINKTEST-A-00-00-01-00A-040A-D"
       xlink:title="XLink test - Referenced data module">
[...]
</dmRef>
```