# DMC-S1000DBIKE-AAA-DA0-20-00-00AA-412A-A_010-00_EN-US

## Ident And Status Section

### DM Address

#### DM Ident

*   **modelIdentCode:** S1000DBIKE
*   **systemDiffCode:** AAA
*   **systemCode:** DA0
*   **subSystemCode:** 2
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 00
*   **disassyCodeVariant:** AA
*   **infoCode:** 412
*   **infoCodeVariant:** A
*   **itemLocationCode:** A

*   **language:**
    *   **countryIsoCode:** US
    *   **languageIsoCode:** en

*   **issueInfo:**
    *   **issueNumber:** 010
    *   **inWork:** 00

#### DM Address Items

*   **issueDate:**
    *   **year:** 2024
    *   **month:** 06
    *   **day:** 19

*   **DM Title**
    *   **techName:** Rear wheel
    *   **infoName:** Detected fault

### DM Status

*   **issueType:** changed

*   **Security**
    *   **securityClassification:** 01
    *   **commercialClassification:** cc51
    *   **caveat:** cv51

*   **Data Restrictions**

    *   **Restriction Instructions**
        *   **Data Distribution:** To be made available to all S1000D users.
        *   **Export Control**
            *   **Export Registration Statement:**
                *   Simple Paragraph: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   **Data Handling:** There are no specific handling instructions for this data module.
        *   **Data Destruction:** Users may destroy this data module in accordance with their own local procedures.
        *   **Data Disclosure:** There are no dissemination limitations that apply to this data module.

    *   **Restriction Info**
        *   **Copyright**
            *   Paragraph: *Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   Paragraph: *Publishers:*
            *   Random List:
                *   Aerospace, Security and Defence Industries Association of Europe
                *   Aerospace Industries Association of America
                *   ATA e-Business Program
            *   Paragraph: *Limitations of liability:*
            *   Random List:
                *   Paragraph: This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                *   Paragraph: Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
                *   Paragraph: Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
            *   Paragraph: The details for copyright can be found in the S1000D Specification.
        *   **Policy Statement:** S1000D-SC-2016-017-002-00 Steering Committee TOR
        *   **Data Conditions:** There are no known conditions that would change the data restrictions for, or security classification of, this data module.

*   **Responsible Partner Company**
    *   **enterpriseCode:** B6865
    *   **enterpriseName:** AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

*   **Originator**
    *   **enterpriseCode:** B6865
    *   **enterpriseName:** AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE

*   **Applic Cross Ref Table Ref**
    *   **DM Ref**
        *   **DM Ref Ident**
            *   **DM Code**
                *   **modelIdentCode:** S1000DBIKE
                *   **systemDiffCode:** AAA
                *   **systemCode:** D00
                *   **subSystemCode:** 0
                *   **subSubSystemCode:** 0
                *   **assyCode:** 00
                *   **disassyCode:** 00
                *   **disassyCodeVariant:** AA
                *   **infoCode:** 00W
                *   **infoCodeVariant:** A
                *   **itemLocationCode:** D

*   **Applic**
    *   **Display Text:**
        *   Simple Paragraph: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
    *   **Evaluate:**
        *   **Assert:**
            *   **applicPropertyIdent:** type
            *   **applicPropertyType:** prodattr
            *   **applicPropertyValues:** Mountain bicycle
        *   **Evaluate:**
            *   **Evaluate:**
                *   **Assert:**
                    *   **applicPropertyIdent:** model
                    *   **applicPropertyType:** prodattr
                    *   **applicPropertyValues:** Mountain storm
                *   **Assert:**
                    *   **applicPropertyIdent:** version
                    *   **applicPropertyType:** prodattr
                    *   **applicPropertyValues:** Mk1
            *   **Evaluate:**
                *   **Assert:**
                    *   **applicPropertyIdent:** model
                    *   **applicPropertyType:** prodattr
                    *   **applicPropertyValues:** Brook trekker
                *   **Assert:**
                    *   **applicPropertyIdent:** version
                    *   **applicPropertyType:** prodattr
                    *   **applicPropertyValues:** Mk9

*   **Tech Standard**
    *   **Authority Info And Tp:**
        *   **authorityInfo:** 20010131
        *   **techPubBase:** Bike book
    *   **Authority Exceptions:**
    *   **Authority Notes:**

*   **Brex Dm Ref**
    *   **DM Ref**
        *   **DM Ref Ident**
            *   **DM Code**
                *   **modelIdentCode:** S1000DBIKE
                *   **systemDiffCode:** AAA
                *   **systemCode:** D00
                *   **subSystemCode:** 0
                *   **subSubSystemCode:** 0
                *   **assyCode:** 00
                *   **disassyCode:** 00
                *   **disassyCodeVariant:** AA
                *   **infoCode:** 022
                *   **infoCodeVariant:** A

*   **Quality Assurance**
    *   **firstVerification:** tabtop

*   **System Breakdown Code:** BY12

*   **Skill Level:** sk01

*   **Reason For Update:**
    *   **id:** rfu_general
    *   **updateReasonType:** urt03
    *   **Simple Paragraph:** S1000D upissued

## Content

### Fault Reporting

*   **Detected Fault**
    *   **id:** flt-0002
    *   **faultCode:** NYCJD00
    *   **Fault Descr:**
        *   Descr: The rear wheel does not operate correctly
    *   **Detection Info:**
        *   **detectionType:** Major
        *   **detectedLruItem:**
            *   **lru:**
                *   **name:** Tire
                *   **identNumber:**
                    *   **manufacturerCode:** KT666
                    *   **partAndSerialNumber:**
                        *   **partNumber:** TIRES-010101
    *   **Isolate Detected Fault:**
        *   **lruItem:**
            *   **lru:**
                *   **name:** Rear wheel
                *   **identNumber:**
                    *   **manufacturerCode:** KZ333
                    *   **partAndSerialNumber:**
                        *   **partNumber:** WH-001
    *   **Remarks:**
        *   Simple Paragraph: Prepare the rear wheel for the removal of the tire