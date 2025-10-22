# DMC-S1000D-H-04-10-0301-00A-022A-D_001-00_EN-US_1_1

## Content

### Data Module Rules

This document outlines the rules governing data modules, extracted from the provided `dmodule` XML.

Context Rules - Structure Object Rule Groups

The following rules are context-dependent and organized into rule groups.

#### Structure Object Rule Group

This group defines permissible values for various attributes within the data module structure.

##### Attribute Definitions & Permissible Values

*   **Attribute:** `updateReasonType
    *   Defines the reason for updating the data module.
    *   **Sublist:**
        *   **Value:** `urt01
            *   Editorial change (minor changes, technically insignificant).
        *   **Value:** `urt02
            *   Technical change (significant changes requiring review).
        *   **Value:** `urt03
            *   Markup change (changes related solely to XML markup).
        *   **Value:** `urt04
            *   Applicability change (only the applicability has changed).
        *   **Value:** `urt05
            *   Unique identifier of the referencing structure has changed.
        *   **Value:** `urt51-urt99
            *   Reserved for project/organization-specific values.

*   **Attribute:** `verbatimStyle
    *   Defines the style of verbatim text.
    *   **Sublist:**
        *   **Value:** `vs01
            *   Generic verbatim.
        *   **Value:** `vs02
            *   Filename.
        *   **Value:** `vs11
            *   XML/SGML markup.
        *   **Value:** `vs12
            *   XML/SGML element name.
        *   **Value:** `vs13
            *   XML/SGML attribute name.
        *   **Value:** `vs14
            *   XML/SGML attribute value.
        *   **Value:** `vs15
            *   XML/SGML entity name.
        *   **Value:** `vs16
            *   XML/SGML processing instruction.
        *   **Value:** `vs21
            *   Program prompt.
        *   **Value:** `vs22
            *   User input.
        *   **Value:** `vs23
            *   Computer output.
        *   **Value:** `vs24
            *   Program listing.
        *   **Value:** `vs25
            *   Program variable name.
        *   **Value:** `vs26
            *   Program variable value.
        *   **Value:** `vs27
            *   Constant.
        *   **Value:** `vs28
            *   Class name.
        *   **Value:** `vs29
            *   Parameter name.
        *   **Value:** `vs51-vs99
            *   Reserved for project/organization-specific values.

*   **Attribute:** `quantityUnitOfMeasure
    *   Defines the unit of measure for quantity data. Values within the range `um51-um99` can be allocated and defined by projects or organizations. (Refer to Table 2 in document section 3.9.6.2)

#### Non-Context Rules

These rules are not dependent on specific context within the data module.

##### Deletion of Data Modules

Deletion of data modules is treated as a special case of update. The data module itself is not physically deleted but is marked as deleted. (Refer to document section 3.9.5.1, Para 2.2)