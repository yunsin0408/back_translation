# DMC-S1000DLIGHTING - Zones common information repository

## dmTitle

*   **techName**: Lighting
*   **infoName**: Zones common information repository

## identStatus

### dmAddress

#### dmIdent

*   **modelIdentCode**: S1000DLIGHTING
*   **systemDiffCode**: AAA
*   **systemCode**: D00
*   **subSystemCode**: 0
*   **subSubSystemCode**: 0
*   **assyCode**: 00
*   **disassyCode**: 00
*   **disassyCodeVariant**: AA
*   **infoCode**: 00H
*   **infoCodeVariant**: A
*   **itemLocationCode**: D

#### language

*   **languageIsoCode**: en
*   **countryIsoCode**: US

#### issueInfo

*   **issueNumber**: 004
*   **inWork**: 00

#### dmAddressItems

*   **issueDate**:
    *   **year**: 2024
    *   **month**: 06
    *   **day**: 19

### dmStatus

*   **issueType**: revised
*   **qualityAssurance**:
    *   **firstVerification**: tabtop
*   **reasonForUpdate**:
    *   **id**: rfu_general
    *   **updateReasonType**: urt03
    *   **simplePara**: S1000D upissued
*   **reasonForUpdate**:
    *   **id**: RFU-CPF_2020-040EPWG
    *   **updateReasonType**: urt01
    *   **simplePara**: CPF_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples

## content

### applicGroup

#### applic (id: app-0001)

*   **displayText**:
    *   **simplePara**: Mountain storm Mk1
*   **evaluate**:
    *   **assert**:
        *   **applicPropertyIdent**: model
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: Mountain storm
    *   **assert**:
        *   **applicPropertyIdent**: version
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: Mk1
    *   **assert**:
        *   **applicPropertyIdent**: versrank
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: 1~3

#### applic (id: app-0002)

*   **displayText**:
    *   **simplePara**: Brook trekker Mk9
*   **evaluate**:
    *   **assert**:
        *   **applicPropertyIdent**: model
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: Brook trekker
    *   **assert**:
        *   **applicPropertyIdent**: version
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: Mk9
    *   **assert**:
        *   **applicPropertyIdent**: versrank
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: 1~2

#### applic (id: app-0003)

*   **displayText**:
    *   **simplePara**: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **evaluate**:
    *   **assert**:
        *   **applicPropertyIdent**: type
        *   **applicPropertyType**: prodattr
        *   **applicPropertyValues**: Mountain bicycle
    *   **evaluate**:
        *   **assert**:
            *   **applicPropertyIdent**: model
            *   **applicPropertyType**: prodattr
            *   **applicPropertyValues**: Mountain storm
        *   **assert**:
            *   **applicPropertyIdent**: version
            *   **applicPropertyType**: prodattr
            *   **applicPropertyValues**: Mk1
    *   **evaluate**:
        *   **assert**:
            *   **applicPropertyIdent**: model
            *   **applicPropertyType**: prodattr
            *   **applicPropertyValues**: Brook trekker
        *   **assert**:
            *   **applicPropertyIdent**: version
            *   **applicPropertyType**: prodattr
            *   **applicPropertyValues**: Mk9

### commonRepository

#### zoneRepository

*   **zone (id: 100)**
    *   **zoneType**: majorzone
    *   **zoneIdent**: 100
    *   **zoneRefGroup**: contains (110, 130)
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: FRONT ZONE BEGINS BY FRONT TIRE. IT STARTS FROM LENGTH "0 cm" TO LENGTH "50 cm"
*   **zone (id: 110)**
    *   **zoneType**: subzone
    *   **zoneIdent**: 110
    *   **zoneRefGroup**: belongsto (100)
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: HANDLEBAR
*   **zone (id: 130)**
    *   **zoneType**: majorzone
    *   **zoneIdent**: 130
    *   **zoneRefGroup**: contains (131, 132)
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: REAR WHEEL
*   **zone (id: 131)**
    *   **zoneType**: subzone
    *   **zoneIdent**: 131
    *   **zoneRefGroup**: belongsto (130)
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: 
*   **zone (id: 132)**
    *   **zoneType**: subzone
    *   **zoneIdent**: 132
    *   **zoneRefGroup**: belongsto (130)
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: 
*   **zone (id: 100)**
    *   **zoneType**: majorzone
    *   **zoneIdent**: 100
    *   **zoneRefGroup**: 
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: 
*   **zone (id: 100)**
    *   **zoneType**: majorzone
    *   **zoneIdent**: 100
    *   **zoneRefGroup**: 
    *   **zoneAlts**:
        *   **zone (id: app-0002)**
            *   **itemDescr**: