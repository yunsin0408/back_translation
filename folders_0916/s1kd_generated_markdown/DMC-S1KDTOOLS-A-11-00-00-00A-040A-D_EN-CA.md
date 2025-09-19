# Introduction to s1kd-appcheck
The `s1kd-appcheck` tool is used to check the applicability of S1000D data modules. This document provides an overview of the tool's options and usage.

## Options
The following options are available for use with `s1kd-appcheck`:

* `-a`: Perform a full check, reading values from the ACT and CCT referenced by the data module.
* `-n`: Report when the applicability of an element is incompatible with the applicability of any parent elements or the whole object.
* `-R`: Report when the applicability of a nested element is redundant.
* `-D`: Report when an applicability annotation is a duplicate of another annotation.
* `-t`: Specify the type of check to perform (e.g., `standalone`, `full`).
* `-v`: Increase verbosity, providing more detailed output.
* `-h`: Display help and usage information.

## Examples
### Standalone Check
The following example performs a standalone check on a data module:
```bash
s1kd-appcheck -v <DM>
```
This will report any errors or warnings found in the data module.

### Full Check
To perform a full check, use the `-a` option:
```bash
s1kd-appcheck -a <DM>
```
This will read values from the ACT and CCT referenced by the data module and report any errors or warnings.

### Reporting Redundant Applicability Annotations
The following example reports when the applicability of a nested element is redundant:
```bash
s1kd-appcheck -R <DM>
```
This will identify any redundant annotations in the data module.

### Reporting Duplicate Applicability Annotations
To report duplicate applicability annotations, use the `-D` option:
```bash
s1kd-appcheck -D <DM>
```
This will identify any duplicate annotations in the data module.

## Use Cases
The `s1kd-appcheck` tool can be used in a variety of scenarios, including:

* **Validating data modules**: Before publishing or sharing data modules, use `s1kd-appcheck` to ensure they are valid and free from errors.
* **Identifying redundant annotations**: Use the `-R` option to identify and remove redundant annotations, simplifying the data module and improving maintainability.
* **Detecting duplicate annotations**: Use the `-D` option to identify and remove duplicate annotations, reducing the risk of errors and inconsistencies.

## Best Practices
When using `s1kd-appcheck`, keep the following best practices in mind:

* Always perform a standalone check before publishing or sharing data modules.
* Use the `-a` option to perform a full check when necessary.
* Regularly review and remove redundant annotations to simplify data modules and improve maintainability.
* Use the `-D` option to identify and remove duplicate annotations.