# DMC-S1000DBIKE-AAA-DA4-10-00-00AA-414A-A_008-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated

## dmAddress

### dmIdent
*   modelIdentCode: `S1000DBIKE
*   systemDiffCode: `AAA
*   systemCode: `DA4
*   subSystemCode: `1
*   subSubSystemCode: `0
*   assyCode: `00
*   disassyCode: `00
*   disassyCodeVariant: `AA
*   infoCode: `414
*   infoCodeVariant: `A
*   itemLocationCode: `A
### language
*   countryIsoCode: `US
*   languageIsoCode: `en
### issueInfo
*   issueNumber: `008
*   inWork: `00
### dmAddressItems
*   issueDate
    *   year: `2024
    *   month: `06
    *   day: `19
*   dmTitle
    *   techName: `Drive train
    *   infoName: `Correlated fault
## dmStatus

*   issueType: `changed
### security
*   securityClassification: `01
*   commercialClassification: `cc51
*   caveat: `cv51
### dataRestrictions
*   restrictionInstructions
    *   dataDistribution: `To be made available to all S1000D users.
    *   exportControl
        *   exportRegistrationStmt
            *   simplePara: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
    *   dataHandling: `There are no specific handling instructions for this data module.
    *   dataDestruction: `Users may destroy this data module in accordance with their own local procedures.
    *   dataDisclosure: `There are no dissemination limitations that apply to this data module.
*   restrictionInfo
    *   copyright
        *   copyrightPara emphasis="true": `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD
        *   copyrightPara emphasis="true": `Publishers:
        *   randomList listItemPrefix="pf01"
            *   listItem: `Aerospace, Security and Defence Industries Association of Europe
            *   listItem: `Aerospace Industries Association of America
            *   listItem: `ATA e-Business Program
        *   copyrightPara emphasis="true": `Limitations of liability:
        *   randomList listItemPrefix="pf02"
            *   listItem: `This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.
            *   listItem: `Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.
            *   listItem: `Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.
        *   copyrightPara: `The details for copyright can be found in the S1000D Specification.
    *   policyStatement: `S1000D-SC-2016-017-002-00 Steering Committee TOR
    *   dataConds: `There are no known conditions that would change the data restrictions for, or security classification of, this data module.
### responsiblePartnerCompany
*   enterpriseCode: `B6865
*   enterpriseName: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
### originator
*   enterpriseCode: `B6865
*   enterpriseName: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE
### applicCrossRefTableRef
*   dmRef
    *   dmRefIdent
        *   dmCode
            *   modelIdentCode: `S1000DBIKE
            *   systemDiffCode: `AAA
            *   systemCode: `D00
            *   subSystemCode: `0
            *   subSubSystemCode: `0
            *   assyCode: `00
            *   disassyCode: `00
            *   disassyCodeVariant: `AA
            *   infoCode: `00W
            *   infoCodeVariant: `A
            *   itemLocationCode: `D
### applic
*   displayText
    *   simplePara: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)
*   evaluate andOr="and"
    *   assert
        *   applicPropertyIdent: `type
        *   applicPropertyType: `prodattr
        *   applicPropertyValues: `Mountain bicycle
*   evaluate andOr="or"
    *   evaluate andOr="and"
        *   assert
            *   applicPropertyIdent: `model
            *   applicPropertyType: `prodattr
            *   applicPropertyValues: `Mountain storm
        *   assert
            *   applicPropertyIdent: `version
            *   applicPropertyType: `prodattr
            *   applicPropertyValues: `Mk1
    *   evaluate andOr="and"
        *   assert
            *   applicPropertyIdent: `model
            *   applicPropertyType: `prodattr
            *   applicPropertyValues: `Brook trekker
        *   assert
            *   applicPropertyIdent: `version
            *   applicPropertyType: `prodattr
            *   applicPropertyValues: `Mk9
## content

### faultReporting
*   correlatedFault id="cflt-0001"
    *   basicCorrelatedFaults
        *   bitMessage
            *   fault
                *   faultCode: `100FC01
                *   faultDescr
                    *   descr: `The pedal mechanism is jammed
        *   bitMessage
            *   fault
                *   faultCode: `200FC01
                *   faultDescr
                    *   descr: `The derailleur is jammed
    *   isolateDetectedFault
        *   lruItem
            *   lru
                *   name: `Bicycle chain
                *   identNumber
                    *   manufacturerCode: `KZ120
                    *   partAndSerialNumber
                        *   partNumber: `Tchain-120
    *   remarks
        *   simplePara: `Prepare the derailleur to put transmission chain back on pedal mechanism.