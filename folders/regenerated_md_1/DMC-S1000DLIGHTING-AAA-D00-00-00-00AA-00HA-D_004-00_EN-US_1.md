```markdown
# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00HA-D_004-00_EN-US

## Ident And Status Section

### DM Address

#### DM Ident

*   **modelIdentCode:** S1000DLIGHTING
*   **systemDiffCode:** AAA
*   **systemCode:** D00
*   **subSystemCode:** 0
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 00H
*   **infoCodeVariant:** A
*   **itemLocationCode:** D

*   **language:**
    *   **languageIsoCode:** en
    *   **countryIsoCode:** US

*   **issueInfo:**
    *   **issueNumber:** 004
    *   **inWork:** 00

#### DM Address Items

*   **issueDate:**
    *   **year:** 2024
    *   **month:** 06
    *   **day:** 19

*   **dmTitle:**
    *   **techName:** Lighting
    *   **infoName:** Zones common information repository

### DM Status

*   **issueType:** revised

#### Security

*   *(No specific security attributes provided in the XML)*

#### Quality Assurance

*   **firstVerification:** tabtop

#### Reason For Update

*   **id:** rfu_general
    *   **updateReasonType:** urt03
    *   **simplePara:** S1000D upissued

*   **id:** RFU-CPF_2020-040EPWG
    *   **updateReasonType:** urt01
    *   **simplePara:** CPF_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples

## Content

### Referenced Applic Group

#### Applic (app-0001)

*   **displayText:**
    *   **simplePara:** Mountain storm Mk1
*   **evaluate:**
    *   **assert:**
        *   **applicPropertyIdent:** model
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** Mountain storm
    *   **assert:**
        *   **applicPropertyIdent:** version
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** Mk1
    *   **assert:**
        *   **applicPropertyIdent:** versrank
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** 1~3

#### Applic (app-0002)

*   **displayText:**
    *   **simplePara:** Brook trekker Mk9
*   **evaluate:**
    *   **assert:**
        *   **applicPropertyIdent:** model
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** Brook trekker
    *   **assert:**
        *   **applicPropertyIdent:** version
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** Mk9
    *   **assert:**
        *   **applicPropertyIdent:** versrank
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** 1~2

#### Applic (app-0003)

*   **displayText:**
    *   **simplePara:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **evaluate:**
    *   **assert:**
        *   **applicPropertyIdent:** type
        *   **applicPropertyType:** prodattr
        *   **applicPropertyValues:** Mountain bicycle
    *   **evaluate:**
        *   **assert:**
            *   **applicPropertyIdent:** model
            *   **applicPropertyType:** prodattr
            *   **applicPropertyValues:** Mountain storm
        *   **assert:**
            *   **applicPropertyIdent:** version
            *   **applicPropertyType:** prodattr
            *   **applicPropertyValues:** Mk1
        *   **evaluate:**
            *   **assert:**
                *   **applicPropertyIdent:** model
                *   **applicPropertyType:** prodattr
                *   **applicPropertyValues:** Brook trekker
            *   **assert:**
                *   **applicPropertyIdent:** version
                *   **applicPropertyType:** prodattr
                *   **applicPropertyValues:** Mk9

### Common Repository

#### Zone Repository

*   **Zone (100):** FRONT
    *   **zoneType:** majorzone
    *   **zoneIdent:** 100
    *   **zoneRefGroup:** contains (110, 130)
    *   **zoneAlts:**
        *   **zone (app-0002):**
            *   **itemDescr:** FRONT ZONE BEGINS BY FRONT TIRE. IT STARTS FROM LENGTH "0 cm" TO LENGTH "50 cm"

*   **Zone (110):** TIRE
    *   **zoneType:** subzone
    *   **zoneIdent:** 110
    *   **zoneRefGroup:** belongsto (100)
    *   **zoneAlts:**
        *   **zone (app-0002):**
            *   **itemDescr:** TIRE ZONE INCLUDING THE FRONT TIRE, THE INNER TUBE AND THE SPOKES

*   **Zone (130):** HANDLE BAR
    *   **zoneType:** subzone
    *   **zoneIdent:** 130
    *   **zoneRefGroup:** belongsto (100)
    *   **zoneRefGroup:** contains (131, 132)
    *   **zoneAlts:**
        *   **zone (app-0003):**
            *   **itemDescr:** HANDLE BAR ZONE

*   **Zone (131):** RIGHT HAND HANDLE BAR
    *   **zoneType:** specifzone
    *   **zoneIdent:** 131
    *   **zoneRefGroup:** belongsto (130)
    *   **zoneAlts:**
        *   **zone (app-0003):**
            *   **itemDescr:** RIGHT HAND HANDLE BAR ZONE

*   **Zone (132):** LEFT HAND HANDLE BAR
    *   **zoneType:** specifzone
    *   **zoneIdent:** 132
    *   **zoneRefGroup:** belongsto (130)
    *   **zoneAlts:**
        *   **zone (app-0003):**
            *   **itemDescr:** LEFT HAND HANDLE BAR ZONE

*   **Zone (200):** MIDDLE
    *   **zoneType:** majorzone
    *   **zoneIdent:** 200
    *   **zoneAlts:**
        *   **zone (app-0002):**
            *   **itemDescr:** MIDDLE ZONE. IT STARTS FROM LENGTH "50 cm" TO LENGTH "100 cm"

*   **Zone (300):** BACK
    *   **zoneType:** majorzone
    *   **zoneIdent:** 300
    *   **zoneAlts:**
        *   **zone (app-0001):**
            *   **itemDescr:** BACK ZONE. IT STARTS FROM LENGTH "100 cm" TO LENGTH "150 cm"
```