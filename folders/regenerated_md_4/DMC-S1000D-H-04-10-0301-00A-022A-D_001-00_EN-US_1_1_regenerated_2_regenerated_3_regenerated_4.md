# DMC-S1000D-H-04-10-0301-00A-022A-D_001-00_EN-US_1_1

This document outlines the rules governing data modules, extracted from the provided `dmodule` XML.

## Context Rules - Structure Object Rule Groups

The following rules are context-dependent and organized into rule groups.

### Structure Object Rule Group

This group defines permissible values for various attributes within the data module structure.

#### Attribute Definitions & Permissible Values

*   **updateReasonType**
    *   **Definition:** Defines the reason for updating the data module.
    *   **Permissible Values:**
        *   `urt01`
        *   `urt02`
        *   `urt03`
        *   `urt04`
        *   `urt05`
        *   `urt51-urt99`

*   **verbatimStyle**
    *   **Definition:** Defines the style of verbatim text.
    *   **Permissible Values:**
        *   `vs01`
        *   `vs02`
        *   `vs11`
        *   `vs12`
        *   `vs13`
        *   `vs14`
        *   `vs15`
        *   `vs16`
        *   `vs21`
        *   `vs22`
        *   `vs23`
        *   `vs24`
        *   `vs25`
        *   `vs26`
        *   `vs27`
        *   `vs28`
        *   `vs29`
        *   `vs51-vs99`

*   **quantityUnitOfMeasure**
    *   **Definition:** Defines the unit of measure for quantity data. Values within the range `um51-um99` can be allocated and defined by projects or organizations. (Refer to Table 2 in document section 3.9.6.2)

## Non-Context Rules

These rules are not dependent on specific context within the data module.

### Deletion of Data Modules

Deletion of data modules is treated as a special case of update. The data module itself is not physically deleted but is marked as deleted. (Refer to document section 3.9.5.1, Para 2.2)