# DMC-S1000DBIKE-AAA-D00-00-00-00AA-024A-D_003-00_EN-US_1_1_regenerated_2_regenerated_3_regenerated_4_regenerated.XML - Bike Business Rules Document

This document represents the converted markdown from the provided XML file, detailing business rules for the Bike project.

## Introduction

This document outlines the business rules defined for the Bike project, based on the provided XML data.

## Content

### Section: Content

#### Overview

This document details various business rules categorized by their nature. Many rules relate to configurable attributes, quality assurance, and content requirements.

#### Business Rules

##### 1. Data Validation & Configuration (Configurable Attributes)

The following rules define valid values for configurable attributes within the Bike data set. These attributes are often used for filtering, categorization, and reporting.

*   **Threshold Interval Unit**
    *   Valid units of measurement for threshold intervals include:
        *   Months
        *   Weeks
        *   Years
        *   Days
        *   Shop visits
        *   Auxiliary power unit change
        *   Wheel change
        *   kilometer

*   **Attribute Source Type Code**
    *   Valid source types include:
        *   fec
        *   sample

*   **Attribute Source Criticality**
    *   Valid criticality levels include:
        *   Evident, Safety
        *   Evident, operational
        *   Evident, Economic
        *   Hidden, Safety
        *   Hidden, Non-Safety

*   **Task Code**
    *   Valid task codes include:
        *   Detailed inspection (DET)
        *   Discard (DIS)
        *   Functional Check (FNC)
        *   General visual inspection (GVI)
        *   Lubrication (LUB)
        *   Operational check (OPC)
        *   Restoration (RST)
        *   Servicing (SVC)
        *   Visual check (VCK)

*   **Limit Type**
    *   Valid limit types include:
        *   Time between overhaul
        *   Hard time
        *   Since last maintenance
        *   Out time limit
        *   On condition
        *   Check maintenance
        *   Functional check

*   **Origin of Equipment/Harness/Wire**
    *   Valid origins include:
        *   Manufacturer
        *   Vendor
        *   Partner

##### 2. Quality Assurance & Process

Bike data modules *must* be reviewed and approved by the EPWG (Engineering Product Working Group) before publication.

##### 3. Content & Data Requirements

The Bike data set *must* contain examples demonstrating the application of constructs and principles representing various levels of conceptual sophistication.

### Notes

The categorization of some rules is based on interpretation of the provided data. It may be appropriate to re-categorize them based on further analysis or project needs. Rules pertaining to configurable attributes are considered data validation rules.