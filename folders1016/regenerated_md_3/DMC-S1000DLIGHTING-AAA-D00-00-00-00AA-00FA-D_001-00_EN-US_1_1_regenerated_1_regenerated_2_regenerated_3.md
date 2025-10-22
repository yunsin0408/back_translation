# Bike Lighting Circuit Breaker Documentation

## 1. Identification and Status

*   **Key:** Document ID
    **Value:** DModule
*   **Key:** Date
    **Value:** (Not present in the document)
*   **Key:** Revision
    **Value:** (Not present in the document)

## 2. Content

### 2.1 Referenced Applic Groups

#### 2.1.1 Application: Mountain Storm Mk1

*   **ID:** app-0001
*   **Description:** Mountain Storm Mk1
*   **Applicability Criteria:**
    *   **Type:** Model
    *   **Value:** Mountain storm
    *   **Version:** Mk1
    *   **Version Range:** 1-3

#### 2.1.2 Application: Brook Trekker Mk9

*   **ID:** app-0002
*   **Description:** Brook Trekker Mk9
*   **Applicability Criteria:**
    *   **Type:** Model
    *   **Value:** Brook trekker
    *   **Version:** Mk9
    *   **Version Range:** 1-2

#### 2.1.3 Application: Mountain Bicycle (with Storm or Trekker)

*   **ID:** app-0003
*   **Description:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **Applicability Criteria:**
    *   **Type:** Type
    *   **Value:** Mountain bicycle
    *   **Condition:** Either:
    *   
        *   **Model:** Mountain storm
        *   **Version:** Mk1
        *   **Version Range:** 1-3
    *   
        *   **Model:** Brook trekker
        *   **Version:** Mk9
        *   **Version Range:** 1-2

### 2.2 Common Repository: Circuit Breaker Repository

#### 2.2.1 Circuit Breaker Specification: CBLGT-1001-R (Right Side)

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

#### 2.2.2 Circuit Breaker Specification: CBLGT-1001-L (Left Side)

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

#### 2.2.3 Circuit Breaker Specification: CBLGT-1001-E (Empty)

*   **ID:** SPEC-0010 / cb-CBLGT-1001-E
*   **Name:** Bike Lighting circuit breaker (empty)
*   **Functional Area:** DA2 / 2 / 0 / 00
*   **Alternatives:**
    *   **ID:** cb-CBLGT-1001-E.001
    *   **Applicability:** app-0003
    *   **Name:** CBLGT-1001-E
    *   **Class:** cbt02
    *   **Location:** Zone 133

#### 2.2.4 Circuit Breaker Specification: CBLGT-1001-F (Full)

*   **ID:** SPEC-0010 / cb-CBLGT-1001-F
*   **Name:** Bike Lighting circuit breaker (full)
*   **Functional Area:** DA2 / 2 / 0 / 00
*   **Alternatives:**
    *   **ID:** cb-CBLGT-1001-F.001
    *   **Applicability:** app-0003
    *   **Name:** CBLGT-1001-F
    *   **Class:** cbt02
    *   **Location:** Zone 134
    *   **Flags:** Active