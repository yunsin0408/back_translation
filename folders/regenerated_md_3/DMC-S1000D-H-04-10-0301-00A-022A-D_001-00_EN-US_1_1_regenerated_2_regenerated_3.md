# DMC-S1000D-H-04-10-0301-00A-022A-D_001-00_EN-US_1_1

This document outlines the rules governing data modules, extracted from the provided `dmodule` XML.

## Context Rules - Structure Object Rule Groups

The following rules are context-dependent and organized into rule groups.

### Structure Object Rule Group

This group defines permissible values for various attributes within the data module structure.

#### Attribute Definitions & Permissible Values

*   **`updateReasonType`**
    *   Definition: Defines the reason for updating the data module.
    *   Sublist:
        *   `urt01`: Editorial change (minor changes, technically insignificant).
        *   `urt02`: Technical change (significant changes requiring review).
        *   `urt03`: Markup change (changes related solely to XML markup).
        *   `urt04`: Applicability change (only the applicability has changed).
        *   `urt05`: Unique identifier of the referencing structure has changed.
        *   `urt51-urt99`: Reserved for project/organization-specific values.

*   **`verbatimStyle`**
    *   Definition: Defines the style of verbatim text.
    *   Sublist:
        *   `vs01`: Generic verbatim.
        *   `vs02`: Filename.
        *   `vs11`: XML/SGML markup.
        *   `vs12`: XML/SGML element name.
        *   `vs13`: XML/SGML attribute name.
        *   `vs14`: XML/SGML attribute value.
        *   `vs15`: XML/SGML entity name.
        *   `vs16`: XML/SGML processing instruction.
        *   `vs21`: Program prompt.
        *   `vs22`: User input.
        *   `vs23`: Computer output.
        *   `vs24`: Program listing.
        *   `vs25`: Program variable name.
        *   `vs26`: Program variable value.
        *   `vs27`: Constant.
        *   `vs28`: Class name.
        *   `vs29`: Parameter name.
        *   `vs51-vs99`: Reserved for project/organization-specific values.

*   **`quantityUnitOfMeasure`**
    *   Definition: Defines the unit of measure for quantity data. Values within the range `um51-um99` can be allocated and defined by projects or organizations. (Refer to Table 2 in document section 3.9.6.2)

## Non-Context Rules

These rules are not dependent on specific context within the data module.

### Deletion of Data Modules

Deletion of data modules is treated as a special case of update. The data module itself is not physically deleted but is marked as deleted. (Refer to document section 3.9.5.1, Para 2.2)