# DMC-S1000DLIGHTING - Zones Common Information Repository

This document represents the content of the XML file `DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-00HA-D_004-00_EN-US_1_1_regenerated_2_regenerated_3_regenerated_4_regenerated.XML`, adhering to the S1000D standard.

## DM Title

*   **Tech Name:** Lighting
*   **Info Name:** Zones common information repository

## Ident Status

### DM Address

*   **DM Ident:**
    *   **Model Ident Code:** S1000DLIGHTING
    *   **System Diff Code:** AAA
    *   **System Code:** D00
    *   **Sub-System Code:** 0
    *   **Sub-System Code:** 0
    *   **Assy Code:** 00
    *   **Disassy Code:** 00
    *   **Disassy Code Variant:** AA
    *   **Info Code:** 00H
    *   **Info Code Variant:** A
    *   **Item Location Code:** D
*   **Language:**
    *   **Language Iso Code:** en
    *   **Country Iso Code:** US
*   **Issue Info:**
    *   **Issue Number:** 004
    *   **In Work:** 00
*   **DM Address Items:**
    *   **Issue Date:**
        *   **Year:** 2024
        *   **Month:** 06
        *   **Day:** 19

### DM Status

*   **Issue Type:** revised
*   **Quality Assurance:**
    *   **First Verification:** tabtop
*   **Reason For Update:**
    *   **ID:** rfu_general
    *   **Update Reason Type:** urt03
    *   **Simple Para:** S1000D upissued
*   **Reason For Update:**
    *   **ID:** RFU-CPF_2020-040EPWG
    *   **Update Reason Type:** urt01
    *   **Simple Para:** CPF_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples

## Content

### Applic Group

#### Applic (app-0001)

*   **Display Text:**
    *   **Simple Para:** Mountain storm Mk1
*   **Evaluate:**
    *   **Assert:**
        *   **Applic Property Ident:** model
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** Mountain storm
    *   **Assert:**
        *   **Applic Property Ident:** version
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** Mk1
    *   **Assert:**
        *   **Applic Property Ident:** versrank
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** 1~3

#### Applic (app-0002)

*   **Display Text:**
    *   **Simple Para:** Brook trekker Mk9
*   **Evaluate:**
    *   **Assert:**
        *   **Applic Property Ident:** model
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** Brook trekker
    *   **Assert:**
        *   **Applic Property Ident:** version
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** Mk9
    *   **Assert:**
        *   **Applic Property Ident:** versrank
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** 1~2

#### Applic (app-0003)

*   **Display Text:**
    *   **Simple Para:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   **Evaluate:**
    *   **Assert:**
        *   **Applic Property Ident:** type
        *   **Applic Property Type:** prodattr
        *   **Applic Property Values:** Mountain bicycle
    *   **Evaluate:**
        *   **Assert:**
            *   **Applic Property Ident:** model
            *   **Applic Property Type:** prodattr
            *   **Applic Property Values:** Mountain storm
        *   **Assert:**
            *   **Applic Property Ident:** version
            *   **Applic Property Type:** prodattr
            *   **Applic Property Values:** Mk1
    *   **Evaluate:**
        *   **Assert:**
            *   **Applic Property Ident:** model
            *   **Applic Property Type:** prodattr
            *   **Applic Property Values:** Brook trekker
        *   **Assert:**
            *   **Applic Property Ident:** version
            *   **Applic Property Type:** prodattr
            *   **Applic Property Values:** Mk9

### Common Repository

#### Zone Repository

*   **Zone (100):**
    *   **Zone Type:** majorzone
    *   **Zone Ident:** 100
    *   **Zone Ref Group:** contains (110, 130)
    *   **Zone Alts:**
        *   **Zone (app-0002):**
            *   **Item Descr:** FRONT ZONE BEGINS BY FRONT TIRE. IT STARTS FROM LENGTH "0 cm" TO LENGTH "50 cm"
*   **Zone (110):**
    *   **Zone Type:** subzone
    *   **Zone Ident:** 110
    *   **Zone Ref Group:** belongsto (100)
    *   **Zone Alts:**
        *   **Zone (app-0002):**
            *   **Item Descr:** HANDLEBAR
*   **Zone (130):**
    *   **Zone Type:** majorzone
    *   **Zone Ident:** 130
    *   **Zone Ref Group:** contains (131, 132)
    *   **Zone Alts:**
        *   **Zone (app-0002):**
            *   **Item Descr:** REAR WHEEL
*   **Zone (131):**
    *   **Zone Type:** subzone
    *   **Zone Ident:** 131
    *   **Zone Ref Group:** belongsto (130)
    *   **Zone Alts:**
        *   **Zone (app-0002):**
            *   **Item Descr:**
*   **Zone (132):**
    *   **Zone Type:** subzone
    *   **Zone Ident:** 132
    *   **Zone Ref Group:** belongsto (130)
    *   **Zone Alts:**
        *   **Zone (app-0002):**
            *   **Item Descr:**
*   **Zone (100):**
    *   **Zone Type:** majorzone
    *   **Zone Ident:** 100
    *   **Zone Ref Group:**
    *   **Zone Alts:**
        *   **Zone (app-0002):**