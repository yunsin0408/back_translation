# DMC-S1000DBIKE-AAA-D00-00-00-00AA-022A-D_011-00_EN-US_1_1_regenerated_2_regenerated.XML

This document represents the converted markdown from the provided XML file, detailing Bike DModule context and non-context rules.

## dmTitle

Bike DModule - Context and Non-Context Rules

## dmDescription

This document outlines the context and non-context rules defined within the provided DModule, detailing allowed values and project guidelines.

## contextRules

### structureObjectRuleGroups

#### ruleGroup (limitType="@limitUnitType")

*   **ruleName:** limitType/@limitUnitType
*   **allowedValues:**
    *   Time between overhaul
    *   Hard time
    *   Since last maintenance
    *   Out time limit
    *   On condition
    *   Check maintenance
    *   Functional check

#### ruleGroup (threshold="@thresholdUnitOfMeasure")

*   **ruleName:** threshold/@thresholdUnitOfMeasure
*   **allowedValues:**
    *   Months
    *   Weeks
    *   Years
    *   Days
    *   Shop visits
    *   Auxiliary power unit change
    *   Wheel change
    *   Kilometer (lexical)

#### ruleGroup (sourceType="@sourceTypeCode")

*   **ruleName:** sourceType/@sourceTypeCode
*   **allowedValues:**
    *   fec
    *   sample

#### ruleGroup (sourceType="@sourceCriticality")

*   **ruleName:** sourceType/@sourceCriticality
*   **allowedValues:**
    *   Evident, Safety
    *   Evident, operational
    *   Evident, Economic
    *   Hidden, Safety
    *   Hidden, Non-Safety

#### ruleGroup (verbatimText="@verbatimStyle")

*   **ruleName:** verbatimText/@verbatimStyle
*   **allowedValues:**
    *   Generic verbatim
    *   Filename
    *   XML/SGML markup and related elements (element name, attribute name/value, entity name, processing instruction)
    *   Program prompt, user input, output, listing, variable name/value, constant, class name, parameter name.

### notationRules

#### notation

*   **notationId:** //-//S1000D//NOTATION X-SHOCKWAVE-FLASH 3D Models Encoding//EN
*   **notationDescription:** Flash animation is *not* allowed in this project.

## nonContextRules

### rule (BIKE-BR-00078)

*   **ruleId:** BIKE-BR-00078
*   **ruleDescription:** Bike data modules *must* be reviewed and approved by the EPWG (Engineering Publication Working Group) before publication.

### rule (BIKE-BR-00079)

*   **ruleId:** BIKE-BR-00079
*   **ruleDescription:** The Bike data set *must* contain examples demonstrating the application of constructs and principles at various levels of conceptual sophistication.