# DMC-S1000DBIKE-AAA-D00-00-00-00AA-00KA-D_001-00_EN-US

## Ident and Status Section

### DM Address

#### DM Ident

```
modelIdentCode: S1000DBIKE
systemDiffCode: AAA
systemCode: D00
subSystemCode: 0
subSubSystemCode: 0
assyCode: 00
disassyCode: 00
disassyCodeVariant: AA
infoCode: 00K
infoCodeVariant: A
itemLocationCode: D
```

#### Language

```
countryIsoCode: US
languageIsoCode: en
```

#### Issue Info

```
issueNumber: 001
inWork: 00
```

#### DM Address Items

##### Issue Date

```
year: 2024
month: 06
day: 19
```

##### DM Title

*   **Tech Name:** Mountain bicycle
*   **Info Name:** Organizations common information repository

### DM Status

*   **Issue Type:** new

#### Security

```
caveat: cv51
commercialClassification: cc51
securityClassification: 01
```

#### Data Restrictions

##### Restriction Instructions

*   **Data Distribution:** To be made available to all S1000D users.

*   **Export Control:**

    ```
    simplePara: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
    ```

*   **Data Handling:** There are no specific handling instructions for this data module.
*   **Data Destruction:** Users may destroy this data module in accordance with their own local procedures.
*   **Data Disclosure:** There are no dissemination limitations that apply to this data module.

##### Restriction Info

*   **Copyright:**

    ```
    emphasis: Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
    ```

    ```
    emphasis: Publishers:
    ```

    *   Aerospace, Security and Defence Industries Association of Europe
    *   Aerospace Industries Association of America
    *   ATA e-Business Program

    ```
    emphasis: Limitations of liability:
    ```

    *   This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
    *   Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
    *   Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.

    The details for copyright can be found in the S1000D Specification.

*   **Policy Statement:** S1000D-SC-2016-017-002-00 Steering Committee TOR
*   **Data Conditions:** There are no known conditions that would change the data restrictions for, or security classification of, this data module.

#### Responsible Partner Company

```
enterpriseCode: B6865
enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
```

#### Originator

```
enterpriseCode: B6865
enterpriseName: AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
```

#### Applic Cross-Reference Table Ref

```
modelIdentCode: S1000DBIKE
systemDiffCode: AAA
systemCode: D00
subSystemCode: 0
subSubSystemCode: 0
assyCode: 00
disassyCode: 00
disassyCodeVariant: AA
infoCode: 00W
infoCodeVariant: A
itemLocationCode: D
```

#### Applic

*   **Display Text:** Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)

*   **Evaluate:** and

    *   **Assert:** `applicPropertyIdent = type`, `applicPropertyType = prodattr`, `applicPropertyValues = Mountain bicycle`

    *   **Evaluate:** or

        *   **Evaluate:** and

            *   **Assert:** `applicPropertyIdent = model`, `applicPropertyType = prodattr`, `applicPropertyValues = Mountain storm`
            *   **Assert:** `applicPropertyIdent = version`, `applicPropertyType = prodattr`, `applicPropertyValues = Mk1`
            *   **Assert:** `applicPropertyIdent = versrank`, `applicPropertyType = prodattr`, `applicPropertyValues = 1~3`

        *   **Evaluate:** and

            *   **Assert:** `applicPropertyIdent = model`, `applicPropertyType = prodattr`, `applicPropertyValues = Brook trekker`
            *   **Assert:** `applicPropertyIdent = version`, `applicPropertyType = prodattr`, `applicPropertyValues = Mk9`
            *   **Assert:** `applicPropertyIdent = versrank`, `applicPropertyType = prodattr`, `applicPropertyValues = 1~2`

#### Tech Standard

```
authorityInfo: 20010131
techPubBase: Bike book
```

#### Brex DM Ref

```
modelIdentCode: S1000DBIKE
systemDiffCode: AAA
systemCode: D00
subSystemCode: 0
subSubSystemCode: 0
assyCode: 00
disassyCode: 00
disassyCodeVariant: AA
infoCode: 022
infoCodeVariant: A
itemLocationCode: D
```

#### Quality Assurance

*   **Verification Type:** tabtop

#### Remarks

*   CPF\_2020-040EPWG Bike Enhancement with elements and attributes missing in the samples
*   EPWG add enterpriseRepository, enterpriseSpec, enterpriseIdent, enterpriseIdentAlt

## Content

### Common Repository

#### Enterprise Repository (id: SPEC-0001)

##### Enterprise Spec (id: C001)

*   **Enterprise Ident (id: SPEC-0003, manufacturerCodeValue: KZ444)**
*   **Enterprise Name:** UTOPIA plc

    *   **Business Unit:**

        *   **Business Unit Name:** Customers Services Business Line
        *   **Business Unit Address:**
            *   **Street:** Heaven street
            *   **Postal Zip Code:** 99999
            *   **City:** Saint Vitus
            *   **Country:** UTOPIA
            *   **Phone Number:** 111 222 333 444
            *   **Fax Number:** 111 222 333 445
            *   **Email:** customers\_services@utopia.com
            *   **Email:** info@utopia.com
            *   **Internet:** www.utopia.customers.services.online.com
            *   **Internet:** www.utopia.online.com

##### Enterprise Spec (id: SPEC-0002)

*   **Enterprise Ident (id: SPEC-0004, manufacturerCodeValue: 00000)**
*   **Enterprise Ident Alt (altCode: 1235, altCodeType: DUNS)**
*   **Enterprise Name:** Greasy Bikes Co. Plc

    *   **Business Unit:**

        *   **Business Unit Name:** Heavy bikes
        *   **Business Unit Address:**
            *   **Street:** Off Road 66
            *   **Postal Zip Code:** 12587
            *   **City:** Noway
            *   **Country:** Atlantis