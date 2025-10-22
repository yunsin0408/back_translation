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

*   **id:** app-0001
*   **description:** Mountain Storm Mk1
*   **applicability_criteria:**
    *   **type:** Model
    *   **value:** Mountain storm
    *   **version:** Mk1
    *   **version_range:** 1-3

#### 2.1.2 Application: Brook Trekker Mk9

*   **id:** app-0002
*   **description:** Brook Trekker Mk9
*   **applicability_criteria:**
    *   **type:** Model
    *   **value:** Brook trekker
    *   **version:** Mk9
    *   **version_range:** 1-2

#### 2.1.3 Application: Mountain Bicycle (with Storm or Trekker)

*   **id:** app-0003
*   **description:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **applicability_criteria:**
    *   **type:** Type
    *   **value:** Mountain bicycle
    *   **condition:** Either:
        *   **item:**
            *   **model:** Mountain storm
            *   **version:** Mk1
            *   **version_range:** 1-3
        *   **item:**
            *   **model:** Brook trekker
            *   **version:** Mk9
            *   **version_range:** 1-2

### 2.2 Common Repository: Circuit Breaker Repository

#### 2.2.1 Circuit Breaker Specification: CBLGT-1001-R (Right Side)

*   **id:** SPEC-0010 / cb-CBLGT-1001-R
*   **name:** Bike Lighting circuit breaker (right side)
*   **functional_area:** DA2 / 2 / 0 / 00
*   **references:** SPEC-0008 (CBLGT-1001-E)
*   **alternatives:**
    *   **id:** cb-CBLGT-1001-R.001
    *   **applicability:** app-0001 (Mountain Storm Mk1)
    *   **name:** CBLGT-1001-R
    *   **class:** cbt02
    *   **location:** Zone 131

#### 2.2.2 Circuit Breaker Specification: CBLGT-1001-L (Left Side)

*   **id:** SPEC-0010 / cb-CBLGT-1001-L
*   **name:** Bike Lighting circuit breaker (left side)
*   **functional_area:** DA2 / 2 / 0 / 00
*   **references:** SPEC-0009 (CBLGT-1001-E)
*   **alternatives:**
    *   **id:** cb-CBLGT-1001-L.001
    *   **applicability:** app-0002 (Brook Trekker Mk9)
    *   **name:** CBLGT-1001-L
    *   **class:** cbt02
    *   **location:** Zone 132

#### 2.2.3 Circuit Breaker Specification: CBLGT-1001-E (Empty)

*   **id:** SPEC-0010 / cb-CBLGT-1001-E
*   **name:** Bike Lighting circuit breaker (empty)
*   **functional_area:** DA2 / 2 / 0 / 00
*   **alternatives:**
    *   **id:** cb-CBLGT-1001-E.001
    *   **applicability:** app-0003
    *   **name:** CBLGT-1001-E
    *   **class:** cbt02
    *   **location:** Zone 133

#### 2.2.4 Circuit Breaker Specification: CBLGT-1001-F (Full)

*   **id:** SPEC-0010 / cb-CBLGT-1001-F
*   **name:** Bike Lighting circuit breaker (full)
*   **functional_area:** DA2 / 2 / 0 / 00
*   **alternatives:**
    *   **id:** cb-CBLGT-1001-F.001
    *   **applicability:** app-0003
    *   **name:** CBLGT-1001-F
    *   **class:** cbt02
    *   **location:** Zone 134
    *   **flags:** Active