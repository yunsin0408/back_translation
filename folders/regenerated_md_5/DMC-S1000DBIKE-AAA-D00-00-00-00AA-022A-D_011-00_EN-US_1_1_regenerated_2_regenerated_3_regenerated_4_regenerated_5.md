# DMC-S1000DBIKE-AAA-D00-00-00-00AA-022A-D_011-00_EN-US_1_1_regenerated_2_regenerated_3_regenerated_4_regenerated.XML

This document represents the converted markdown from the provided XML file, detailing Bike DModule context and non-context rules.

## Document Description

This document outlines the context and non-context rules defined within the provided DModule, detailing allowed values and project guidelines.

## Context Rules

### Structure Object Rule Groups

#### Rule Group: Limit Type (@limitUnitType)

*   **rule\_name**: limitType (@limitUnitType)
*   **allowed\_values**:
    *   Time between overhaul
    *   Hard time
    *   Since last maintenance
    *   Out time limit
    *   On condition
    *   Check maintenance
    *   Functional check

#### Rule Group: Threshold (@thresholdUnitOfMeasure)

*   **rule\_name**: threshold (@thresholdUnitOfMeasure)
*   **allowed\_values**:
    *   Months
    *   Weeks
    *   Years
    *   Days
    *   Shop visits
    *   Auxiliary power unit change
    *   Wheel change
    *   Kilometer (lexical)

#### Rule Group: Source Type (@sourceTypeCode)

*   **rule\_name**: sourceType (@sourceTypeCode)
*   **allowed\_values**:
    *   fec
    *   sample

#### Rule Group: Source Criticality (@sourceCriticality)

*   **rule\_name**: sourceType (@sourceCriticality)
*   **allowed\_values**:
    *   Evident, Safety
    *   Evident, operational
    *   Evident, Economic
    *   Hidden, Safety
    *   Hidden, Non-Safety

#### Rule Group: Verbatim Text (@verbatimStyle)

*   **rule\_name**: verbatimText (@verbatimStyle)
*   **allowed\_values**:
    *   Generic verbatim
    *   Filename
    *   XML/SGML markup and related elements (element name, attribute name/value, entity name, processing instruction)
    *   Program prompt, user input, output, listing, variable name/value, constant, class name, parameter name.

## Notation Rules

### Notation

*   **notation\_id**: //-//S1000D//NOTATION X-SHOCKWAVE-FLASH 3D Models Encoding//EN
*   **notation\_description**: Flash animation is *not* allowed in this project.

## Non-Context Rules

### Rule: BIKE-BR-00078

*   **rule\_id**: BIKE-BR-00078
*   **rule\_description**: Bike data modules *must* be reviewed and approved by the EPWG (Engineering Publication Working Group) before publication.

### Rule: BIKE-BR-00079

*   **rule\_id**: BIKE-BR-00079
*   **rule\_description**: The Bike data set *must* contain examples demonstrating the application of constructs and principles at various levels of conceptual sophistication.