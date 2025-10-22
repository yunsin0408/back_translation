# DMC-S1000DBIKE-AAA-D05-10-00-00AA-000A-A_011-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated_3_regenerated_4_regenerated

## dmIdent

### dmAddress

#### dmIdent

*   modelIdentCode: S1000DBIKE
*   systemDiffCode: AAA
*   systemCode: D05
*   subSystemCode: 1
*   subSubSystemCode: 0
*   assyCode: 00
*   disassyCode: 00
*   disassyCodeVariant: AA
*   infoCode: 000
*   infoCodeVariant: A
*   itemLocationCode: A

#### language

*   countryIsoCode: US
*   languageIsoCode: en

#### issueInfo

*   issueNumber: 011
*   inWork: 00

#### dmAddressItems

*   issueDate
    *   year: 2024
    *   month: 06
    *   day: 19
*   dmTitle
    *   techName: Bicycle
    *   infoName: Time limits

### dmStatus

*   issueType: changed
*   security
    *   securityClassification: 01
    *   commercialClassification: cc51
    *   caveat: cv51
*   dataRestrictions
    *   restrictionInstructions
        *   dataDistribution: To be made available to all S1000D users.
        *   exportControl
            *   exportRegistrationStmt: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   dataHandling: There are no specific handling instructions for this data module.
        *   dataDestruction: Users may destroy this data module in accordance with their own local procedures.
        *   dataDisclosure: There are no dissemination limitations that apply to this data module.
    *   restrictionInfo
        *   copyright
            *   copyrightPara: *Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   copyrightPara: *Publishers:*
            *   randomList
                *   Aerospace, Security and Defence Industries Association of Europe
                *   Aerospace Industries Association of America
                *   ATA e-Business Program
            *   copyrightPara: *Limitations of liability:*
            *   randomList
                *   simplePara: This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
                *   simplePara: Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages arising out of the use of this material.
                *   simplePara: The use of this material is at your own risk.
            *   policyStatement
                *   simplePara: The user agrees to indemnify and hold harmless ASD, its officers, directors, employees and agents from any and all claims, damages, liabilities, costs and expenses, including attorneys' fees, arising out of or relating to the use of this material.
            *   policyStatement
                *   simplePara: This material is subject to change without notice.

### responsiblePerson

*   name: John Doe
*   organization: Example Org.

### applicability

*   applicabilityCode: A
*   applicabilityDescription: Applicable to all models

### systemBreakdownCode

*   systemBreakdownCode: BY

### skillLevel

*   skillLevel: sk01

### reasonForUpdate

*   id: rfu_general
*   updateReasonType: urt03
*   simplePara: S1000D upissued

### content

#### referencedApplicGroup

*   applic
    *   id: MK1MK9
    *   displayText
        *   simplePara: Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
    *   evaluate
        *   assert
            *   applicPropertyIdent: type
            *   applicPropertyType: prodattr
            *   applicPropertyValues: Mountain bicycle
        *   evaluate
            *   assert
                *   applicPropertyIdent: model
                *   applicPropertyType: prodattr
                *   applicPropertyValues: Mountain storm
            *   assert
                *   applicPropertyIdent: version
                *   applicPropertyType: prodattr
                *   applicPropertyValues: Mk1
            *   evaluate
                *   assert
                    *   applicPropertyIdent: model
                    *   applicPropertyType: prodattr
                    *   applicPropertyValues: Brook trekker
                *   assert
                    *   applicPropertyIdent: version
                    *   applicPropertyType: prodattr
                    *   applicPropertyValues: Mk9

#### timeLimit

*   timeLimitItem
    *   applicRef: MK1MK9
    *   equip
        *   name: Bicycle
        *   ident
            *   manufacturerCode: KZ555
            *   partNumber: Ch-001
    *   timeLimit
        *   limitType: lt05
        *   threshold
            *   unitMeas: th03
            *   value: 1
*   timeLimitItem
    *   applicRef: MK1MK9
    *   equip
        *   name: Hub bearings
        *   ident
            *   manufacturerCode: KZ555
            *   partNumber: HB-001
    *   timeLimit
        *   limitType: lt06
        *   threshold
            *   unitMeas: th03
            *   value: 6
        *   tolerance
            *   toleranceType: plusorminus
            *   toleranceValue: 1