```markdown
# Bike Lighting Circuit Breaker Documentation (DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00FA-D_001-00_EN-US_1_1_regenerated_2_regenerated_3_regenerated.XML)

## DMC Document

### Title

Bike Lighting Circuit Breaker Documentation

### Identification

*   **Document ID:** DModule
*   **Date:** (Not present in the document)
*   **Revision:** (Not present in the document)

### Content

#### Applicability Groups

##### Applicability Group: Mountain Storm Mk1

*   **Title:** Mountain Storm Mk1
*   **ID:** app-0001
*   **Description:** Mountain Storm Mk1
*   **Applicability Criteria:**
    *   **Type:** Model
    *   **Value:** Mountain storm
    *   **Version:** Mk1
    *   **Version Range:** 1-3

##### Applicability Group: Brook Trekker Mk9

*   **Title:** Brook Trekker Mk9
*   **ID:** app-0002
*   **Description:** Brook Trekker Mk9
*   **Applicability Criteria:**
    *   **Type:** Model
    *   **Value:** Brook trekker
    *   **Version:** Mk9
    *   **Version Range:** 1-2

##### Applicability Group: Mountain Bicycle (with Storm or Trekker)

*   **Title:** Mountain Bicycle (with Storm or Trekker)
*   **ID:** app-0003
*   **Description:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **Applicability Criteria:**
    *   **Type:** Type
    *   **Value:** Mountain bicycle
    *   **Condition:** Either:
    *   **Model:** Mountain storm
    *   **Version:** Mk1
    *   **Version Range:** 1-3
    *   **Model:** Brook trekker
    *   **Version:** Mk9
    *   **Version Range:** 1-2

#### Repository

##### Specification: CBLGT-1001-R (Right Side)

*   **Title:** CBLGT-1001-R (Right Side)
*   **ID:** SPEC-0010 / cb-CBLGT-1001-R
*   **Name:** Bike Lighting circuit breaker (right side)
*   **Functional Area:** DA2 / 2 / 0 / 00
*   **References:** SPEC-0008 (CBLGT-1001-E)

*   **Alternatives:**
    *   **ID:** cb-CBLGT-1001-R.001
    *   **Applicability:** app-0001 (Mountain Storm Mk1)
    *   **Name:** CBLGT-1001-R
    *   **Class:** cbt02
    *   **Location:** Zone 131

##### Specification: CBLGT-1001-L (Left Side)

*   **Title:** CBLGT-1001-L (Left Side)
*   **ID:** SPEC-0010 / cb-CBLGT-1001-L
*   **Name:** Bike Lighting circuit breaker (left side)
*   **Functional Area:** DA2 / 2 / 0 / 00
*   **References:** SPEC-0009 (CBLGT-1001-E)

*   **Alternatives:**
    *   **ID:** cb-CBLGT-1001-L.001
    *   **Applicability:** app-0002 (Brook Trekker Mk9)
    *   **Name:** CBLGT-1001-L
    *   **Class:** cbt02
    *   **Location:** Zone 132

##### Specification: CBLGT-1001-E (Empty)

*   **Title:** CBLGT-1001-E (Empty)
*   **ID:** SPEC-0010 / cb-CBLGT-1001-E
*   **Name:** Bike Lighting empty circuit breaker
*   **Functional Area:** DA2 / 2 / 0 / 00

*   **Alternatives:**
    *   **ID:** cb-CBLGT-1001-E.001
    *   **Applicability:** app-0003
    *   **Name:** CBLGT-1001-E
    *   **Class:** cbt02
    *   **Location:** Zone 133

##### Specification: CBLGT-1001-F (Sample)

*   **Title:** CBLGT-1001-F (Sample)
*   **ID:** SPEC-0011 / cb-CBLGT-1001-F
*   **Name:** Bike Lighting circuit breaker (Sample)
*   **Functional Area:** DA2 / 2 / 0 / 00

*   **Alternatives:**
    *   **ID:** cb-CBLGT-1001-F.001
    *   **Applicability:** app-0003
    *   **Name:** CBLGT-1001-F
    *   **Class:** cbt02
    *   **Location:** Zone 134
    *   **Flags:** Active
```