# DMC-S1KDTOOLS-A-34-00-00-00A-040A-D_EN-CA
## Introduction
The `DMC-S1KDTOOLS-A-34-00-00-00A-040A-D_EN-CA` document is a data module that provides information about the `s1kd-sns` tool.

### Ident and Status Section
#### DM Address
The DM address section contains the following information:
* **DM Ident**: 
  + Model ident code: `S1KDTOOLS`
  + System diff code: `A`
  + System code: `34`
  + Sub system code: `0`
  + Sub sub system code: `0`
  + Assy code: `00`
  + Disassy code: `00`
  + Disassy code variant: `A`
  + Info code: `040`
  + Info code variant: `A`
  + Item location code: `D`
* **Language**: 
  + Language ISO code: `en`
  + Country ISO code: `CA`
* **Issue Info**: 
  + Issue number: `012`
  + In work: `00`
* **DM Address Items**:
  + **Issue Date**: 
    - Year: `2020`
    - Month: `09`
    - Day: `01`
  + **DM Title**:
    - Tech name: `s1kd-sns`
    - Info name: `Description`

#### DM Status
The DM status section contains the following information:
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
  + DM ref:
    - DM ref ident:
      - DM code:
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
### Description
The description section contains the following information:

#### General
The `s1kd-sns` tool can be used to automatically organize data modules in a CSDB into a directory hierarchy based on a specified SNS structure. It may also be used to simply print an indented text version of an SNS structure.

#### Usage
```bash
s1kd-sns [-D <dir>] [-d <dir>] [-cmnpsh?] [<BREX> ...]
```

#### Options
The following options are available:
* `-c, --copy`: Copy files into the SNS subfolders instead of linking them.
* `-D, --srcdir <dir>`: The flat directory containing the data modules to organize. By default, the current directory is used.
* `-d, --outdir <dir>`: The root directory of the new SNS structure. By default, the tool will use the name "SNS" in the current directory.
* `-h, -?, --help`: Show usage message.
* `-m, --move`: Move files into the SNS subfolders instead of linking them.
* `-n, --only-code`: Use only the SNS codes when naming directories. By default, each directory will be named in the form of "snsCode - snsTitle".
* `-p, --print`: Print the SNS structure only.
* `-s, --symlink`: Use symbolic links to organize the SNS instead of the default hard links.
* `--version`: Show version information.
* `<BREX>`: Read the SNS structure from the specified BREX data module. If none is specified, the tool will read from stdin.

Additional options for configuring the XML parser:
* `--dtdload`: Load the external DTD.
* `--huge`: Remove any internal arbitrary parser limits.
* `--net`: Allow network access to load external DTD and entities.
* `--noent`: Resolve entities.
* `--parser-errors`: Emit errors from parser.
* `--parser-warnings`: Emit warnings from parser.
* `--xinclude`: Do XInclude processing.
* `--xml-catalog <file>`: Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times.

#### Example
```bash
$ s1kd-sns DMC-S1000D-A-08-02-0100-00A-022A-D_EN-US.XML
$ tree SNS
SNS
|_ 00 - Product, General
   |_ 0 - Product, General
   |_ 1 - Product, General maintenance
   |_ 2 - Product, Safety
   |
...
|_ 04 - Worthiness (fit for purpose) limitations
   |_ 0 - General
   |_ 1 - Fatigue index calculations
   |_ 2 - Operating spectrums
|_ 05 - Scheduled/unscheduled maintenance
   |_ 0 - General
   |_ 1 - Time limits
   |_ 2 - Scheduled maintenance check lists
...
|_ 18 - Vibration and noise analysis and attenuation
```