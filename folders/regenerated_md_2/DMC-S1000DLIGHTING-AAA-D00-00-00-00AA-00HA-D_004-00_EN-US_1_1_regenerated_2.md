# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00HA-D_004-00_EN-US

This document represents the content of the XML file `DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00HA-D_004-00_EN-US`. It adheres to the S1000D standard.

## 1. Ident and Status Section

### 1.1 DM Address

#### 1.1.1 DM Ident

*   `modelIdentCode`: `S1000DLIGHTING`
*   `systemDiffCode`: `AAA`
*   `systemCode`: `D00`
*   `subSystemCode`: `0`
*   `subSubSystemCode`: `0`
*   `assyCode`: `00`
*   `disassyCode`: `00`
*   `disassyCodeVariant`: `AA`
*   `infoCode`: `00H`
*   `infoCodeVariant`: `A`
*   `itemLocationCode`: `D`

#### 1.1.2 Language

*   `languageIsoCode`: `en`
*   `countryIsoCode`: `US`

#### 1.1.3 Issue Info

*   `issueNumber`: `004`
*   `inWork`: `00`

#### 1.1.4 DM Address Items

*   `issueDate`:
    *   `year`: `2024`
    *   `month`: `06`
    *   `day`: `19`
*   `dmTitle`:
    *   `techName`: `Lighting`
    *   `infoName`: `Zones common information repository`

### 1.2 DM Status

*   `issueType`: `revised`
*   `security`: (empty)
*   `qualityAssurance`:
    *   `firstVerification`: `tabtop`
*   `reasonForUpdate`:
    *   `id`: `rfu_general`
    *   `updateReasonType`: `urt03`
    *   `simplePara`: `S1000D upissued`
*   `reasonForUpdate`:
    *   `id`: `RFU-CPF_2020-040EPWG`
    *   `updateReasonType`: `urt01`
    *   `simplePara`: `CPF_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples`

## 2. Content

### 2.1 Referenced Applic Group

#### 2.1.1 Applic (id: app-0001)

*   `displayText`:
    *   `simplePara`: `Mountain storm Mk1`
*   `evaluate`:
    *   `assert`:
        *   `applicPropertyIdent`: `model`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Mountain storm`
    *   `assert`:
        *   `applicPropertyIdent`: `version`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Mk1`
    *   `assert`:
        *   `applicPropertyIdent`: `versrank`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `1~3`

#### 2.1.2 Applic (id: app-0002)

*   `displayText`:
    *   `simplePara`: `Brook trekker Mk9`
*   `evaluate`:
    *   `assert`:
        *   `applicPropertyIdent`: `model`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Brook trekker`
    *   `assert`:
        *   `applicPropertyIdent`: `version`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Mk9`
    *   `assert`:
        *   `applicPropertyIdent`: `versrank`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `1~2`

#### 2.1.3 Applic (id: app-0003)

*   `displayText`:
    *   `simplePara`: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)`
*   `evaluate`:
    *   `assert`:
        *   `applicPropertyIdent`: `type`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Mountain bicycle`
    *   `evaluate`:
        *   `assert`:
            *   `applicPropertyIdent`: `model`
            *   `applicPropertyType`: `prodattr`
            *   `applicPropertyValues`: `Mountain storm`
        *   `assert`:
            *   `applicPropertyIdent`: `version`
            *   `applicPropertyType`: `prodattr`
            *   `applicPropertyValues`: `Mk1`
        *   `evaluate`:
            *   `assert`:
                *   `applicPropertyIdent`: `model`
                *   `applicPropertyType`: `prodattr`
                *   `applicPropertyValues`: `Brook trekker`
            *   `assert`:
                *   `applicPropertyIdent`: `version`
                *   `applicPropertyType`: `prodattr`
                *   `applicPropertyValues`: `Mk9`

### 2.2 Common Repository

#### 2.2.1 Zone Repository

*   **Zone (id: 100)**
    *   `zoneType`: `majorzone`
    *   `zoneIdent`: `100`
    *   `zoneRefGroup`: `contains (110, 130)`
    *   `zoneAlts`:
        *   **Zone (id: app-0002)**
            *   `itemDescr`: `FRONT ZONE BEGINS BY FRONT TIRE. IT STARTS FROM LENGTH "0 cm" TO LENGTH "50 cm"`
*   **Zone (id: 110)**
    *   `zoneType`: `subzone`
    *   `zoneIdent`: `110`
    *   `zoneRefGroup`: `belongsto (100)`
    *   `zoneAlts`:
        *   **Zone (id: app-0002)**
            *   `itemDescr`: `HANDLE BAR ZONE`
*   **Zone (id: 130)**
    *   `zoneType`: `specifzone`
    *   `zoneIdent`: `130`
    *   `zoneRefGroup`: `belongsto (100)`
    *   `zoneRefGroup`: `contains (131, 132)`
    *   `zoneAlts`:
        *   **Zone (id: app-0003)**
            *   `itemDescr`: `HANDLE BAR ZONE`
*   **Zone (id: 131)**
    *   `zoneType`: `specifzone`
    *   `zoneIdent`: `131`
    *   `zoneRefGroup`: `belongsto (130)`
    *   `zoneAlts`:
        *   **Zone (id: app-0003)**
            *   `itemDescr`: (empty)
*   **Zone (id: 132)**
    *   `zoneType`: `specifzone`
    *   `zoneIdent`: `132`
    *   `zoneRefGroup`: `belongsto (130)`
    *   `zoneAlts`:
        *   **Zone (id: app-0003)**
            *   `itemDescr`: (empty)
*   **Zone (id: 100)**
    *   `zoneType`: `majorzone`
    *   `zoneIdent`: `100`
    *   `zoneRefGroup`: (empty)
    *   `zoneAlts`:
        *   **Zone (id: app-0002)**
            *   `itemDescr`: (empty)
*   **Zone (id: 100)**
    *   `zoneType`: `majorzone`
    *   `zoneIdent`: `100`
    *   `zoneRefGroup`: (empty)
    *   `zoneAlts`:
        *   **Zone (id: app-0002)**
            *   `itemDescr`: (empty)