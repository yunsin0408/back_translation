# Introduction to S1000D Instance Filtering
The `s1kd-instance` tool is used for filtering S1000D data modules based on specified applicability and creating customized instances.

## Basic Usage
The basic usage of the `s1kd-instance` tool involves specifying the input file, the desired output location, and any applicable filtering options. The general syntax is as follows:
```bash
$ s1kd-instance [options] <input_file>
```
### Options

* `-a`: Remove applicability annotations that are fully resolved.
* `-e <code>`: Specify an extended code to use in the identification of output files.
* `-f <file>`: Read input from a file instead of stdin.
* `-I <date>`: Limit search for CIR data modules by issue date.
* `-k <levels>`: Filter on skill levels.
* `-O <directory>`: Write output to a directory with automatic naming.
* `-p <product_instance>`: Filter on a specified product instance.
* `-P <pct_file>`: Read product information from a PCT file.
* `-s <applicability_definition>`: Filter on specified applicability.

## Advanced Usage
### Filtering on Applicability
To filter a data module based on specified applicability, use the `-s` option followed by the applicability definition. For example:
```bash
$ s1kd-instance -s version:prodattr=A <DM>
```
This command filters the input data module (`<DM>`) to only include content applicable to `version A`.

### Filtering on Product Instance
To filter a data module based on a specified product instance, use the `-P` option followed by the PCT file and the `-p` option with the product instance. For example:
```bash
$ s1kd-instance -P <PCT> -p versionA <DM>
```
This command filters the input data module (`<DM>`) to only include content applicable to `version A` as defined in the PCT file.

### Filtering on Skill Levels
To filter a data module based on specified skill levels, use the `-k` option followed by the skill levels. For example:
```bash
$ s1kd-instance -k sk01/sk02 <DMs>
```
This command filters the input data modules (`<DMs>`) to only include content applicable to `sk01` and `sk02`.

### Output Options
To write output to a directory with automatic naming, use the `-O` option followed by the directory path. For example:
```bash
$ s1kd-instance -SO <dir>
```
This command writes the filtered data module(s) to the specified directory (`<dir>`) with automatically generated file names.

### Extended Identification
To specify an extended code for output files, use the `-e` option followed by the extended code. For example:
```bash
$ s1kd-instance -s version:prodattr=A -e 12345-54321 -O . <DMs>
```
This command filters the input data modules (`<DMs>`) based on `version A`, generates output files with the extended identification code `12345-54321`, and writes them to the current directory.

## Exit Status
The exit status of the `s1kd-instance` tool is as follows:

* 0: No errors.
* 1: Missing or incomplete argument.
* 2: Specified file does not exist.
* 3: Source object for an instance could not be found.
* 4: Malformed applicability definition.
* 6: XML was invalid or does not conform to S1000D.
* 7: Value given for an argument was malformed.
* 8: Issue date specified with `-I` is invalid.
* 9: The number of CIR data modules found when searching exceeded the available memory.

## Examples
The following examples demonstrate how to use the `s1kd-instance` tool:

* Filter a data module on specified applicability and write to stdout:
```bash
$ s1kd-instance -s version:prodattr=A <DM>
```
* Filter a data module on a specified product instance and write to stdout:
```bash
$ s1kd-instance -P <PCT> -p versionA <DM>
```
* Filter data modules for a particular customer and output with extended identification:
```bash
$ s1kd-instance -s version:prodattr=A -e 12345-54321 -O . <DMs>
```
* Write out a data module from stdin to a directory with automatic naming:
```bash
$ xml-transform -s <xsl> <DM> | s1kd-instance -SO <dir>
```