# Introduction to s1kd-upissue
The `s1kd-upissue` command is used to update the issue and inwork numbers of S1000D data modules. This document provides an overview of the command, its options, and examples of how to use it.

## Options
The following options are available when using the `s1kd-upissue` command:

### General Options

* `-i`: Make the new issue official.
* `-N`: Do not add issue/inwork numbers to the filename if they are not already present.
* `-v`, `--verbose`: Verbose output.
* `-w`, `--lock`: Make the old issue file read-only after upissuing. Official issues will also be made read-only when they are created.

### Issue Type Options

* `-z`, `--issue-type <type>`: Set the issue type of the new issue.
* If not specified, the issue type will default to "status" for official issues or be the same as the previous issue for inwork issues.

### Date and Time Options

* `-s`, `--keep-date`: Keep the date of the previous inwork or official issue. In `-m` mode, this option has the opposite effect.
* `-t`, `--type <urt>`: Set the updateReasonType of the last specified reason for update.

### XML Parser Options

* `--dtdload`: Load the external DTD.
* `--huge`: Remove any internal arbitrary parser limits.
* `--net`: Allow network access to load external DTD and entities.
* `--noent`: Resolve entities.
* `--parser-errors`: Emit errors from parser.
* `--parser-warnings`: Emit warnings from parser.
* `--xinclude`: Do XInclude processing.
* `--xml-catalog <file>`: Use an XML catalog when resolving entities. Multiple catalogs may be loaded by specifying this option multiple times.

### Other Options

* `-c`, `--clean-rfus`: Remove RFUs which are not associated with any change markup.
* `-^`, `--remove-deleted`: Remove elements with change type of "delete".
* `-r`, `--keep-changes`: Keep the current RFUs and change marks. In `-m` mode, this option has the opposite effect.

## Examples

### Data Module with Issue/Inwork in Filename
```bash
$ ls
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-01_EN-CA.XML

$ s1kd-upissue DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
$ ls
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-02_EN-CA.XML

$ s1kd-upissue -i DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-02_EN-CA.XML
$ ls
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-01_EN-CA.XML
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_000-02_EN-CA.XML
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_001-00_EN-CA.XML
```

### Data Module without Issue/Inwork in Filename
```bash
$ ls
DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_EN-US.XML

$ s1kd-metadata DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_EN-CA.XML -n issueInfo
000-01
$ s1kd-upissue -N DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_EN-CA.XML
$ s1kd-metadata DMC-S1KDTOOLS-A-00-00-00-00A-040A-D_EN-CA.XML -n issueInfo
000-02
```

### Non-XML File with Issue/Inwork in Filename
```bash
$ ls
TXT-S1KDTOOLS-KHZAE-FOOBAR_000-01_EN-CA.TXT

$ s1kd-upissue TXT-S1KDTOOLS-KHZAE-00001_000-01_EN-CA.TXT
$ ls
TXT-S1KDTOOLS-KHZAE-FOOBAR_000-01_EN-CA.TXT
TXT-S1KDTOOLS-KHZAE-FOOBAR_000-02_EN-CA.TXT
```