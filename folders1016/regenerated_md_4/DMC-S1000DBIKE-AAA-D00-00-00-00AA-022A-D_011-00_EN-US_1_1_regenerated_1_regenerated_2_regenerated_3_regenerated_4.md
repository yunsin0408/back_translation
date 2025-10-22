# DMC-S1000DBIKE-AAA-D00-00-00-00AA-022A-D_011-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated_3_regenerated

## dmModule

### dmTitle
Bike DModule - Context and Non-Context Rules

### dmDescription
This document outlines the context and non-context rules defined within the provided DModule, detailing allowed values and project guidelines.

## contextRules

### structureObjectRuleGroups

#### ruleGroup
* ruleName: limitType/@limitUnitType
* allowedValues:
  * Value: Time between overhaul
  * Value: Hard time
  * Value: Since last maintenance
  * Value: Out time limit
  * Value: On condition
  * Value: Check maintenance
  * Value: Functional check

#### ruleGroup
* ruleName: threshold/@thresholdUnitOfMeasure
* allowedValues:
  * Value: Months
  * Value: Weeks
  * Value: Years
  * Value: Days
  * Value: Shop visits
  * Value: Auxiliary power unit change
  * Value: Wheel change
  * Value: Kilometer (lexical)

#### ruleGroup
* ruleName: sourceType/@sourceTypeCode
* allowedValues:
  * Value: fec
  * Value: sample

#### ruleGroup
* ruleName: sourceType/@sourceCriticality
* allowedValues:
  * Value: Evident, Safety
  * Value: Evident, operational
  * Value: Evident, Economic
  * Value: Hidden, Safety
  * Value: Hidden, Non-Safety

#### ruleGroup
* ruleName: verbatimText/@verbatimStyle
* allowedValues:
  * Value: Generic verbatim
  * Value: Filename
  * Value: XML/SGML markup and related elements (element name, attribute name/value, entity name, processing instruction)
  * Value: Program prompt, user input, output, listing, variable name/value, constant, class name, parameter name.

### notationRules

#### notation
* notationId: //-//S1000D//NOTATION X-SHOCKWAVE-FLASH 3D Models Encoding//EN
* notationDescription: Flash animation is *not* allowed in this project.

## nonContextRules

### rule
* ruleId: BIKE-BR-00078
* ruleDescription: Bike data modules *must* be reviewed and approved by the EPWG (Engineering Publication Working Group) before publication.

### rule
* ruleId: BIKE-BR-00079
* ruleDescription: The Bike data set *must* contain examples demonstrating the application of constructs and principles at various levels of conceptual sophistication.