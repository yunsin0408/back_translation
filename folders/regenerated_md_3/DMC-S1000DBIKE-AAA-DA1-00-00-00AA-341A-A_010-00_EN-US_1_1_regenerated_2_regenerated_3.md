# DMC-S1000DBIKE-AAA-DA1-00-00-00AA-341A-A_010-00_EN-US_1_1_regenerated_2_regenerated

This document represents a data module conforming to the S1000D standard.  It uses the following schema: `http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd`

## dmIdent

This section identifies the data module.

*   `modelIdentCode`: `S1000DBIKE`
*   `systemDiffCode`: `AAA`
*   `systemCode`: `DA1`
*   `subSystemCode`: `0`
*   `subSubSystemCode`: `0`
*   `assyCode`: `00`
*   `disassyCode`: `00`
*   `disassyCodeVariant`: `AA`
*   `infoCode`: `341`
*   `infoCodeVariant`: `A`
*   `itemLocationCode`: `A`
*   `language`:
    *   `countryIsoCode`: `US`
    *   `languageIsoCode`: `en`

## dmAddress

This section provides addressing information for the data module.

*   `dmIdent`: (Same as above)
    *   `modelIdentCode`: `S1000DBIKE`
    *   `systemDiffCode`: `AAA`
    *   `systemCode`: `DA1`
    *   `subSystemCode`: `0`
    *   `subSubSystemCode`: `0`
    *   `assyCode`: `00`
    *   `disassyCode`: `00`
    *   `disassyCodeVariant`: `AA`
    *   `infoCode`: `341`
    *   `infoCodeVariant`: `A`
    *   `itemLocationCode`: `A`
*   `dmAddressItems`:
    *   `issueDate`:
        *   `year`: `2024`
        *   `month`: `06`
        *   `day`: `19`
    *   `techName`: `Brake system`
    *   `infoName`: `Manual test`

## dmStatus

This section details the status of the data module.

*   `issueType`: `deleted`
*   `security`:
    *   `securityClassification`: `01`
    *   `commercialClassification`: `cc51`
    *   `caveat`: `cv51`
*   `dataRestrictions`:
    *   `restrictionInstructions`:
        *   `dataDistribution`: `To be made available to all S1000D users.`
        *   `exportControl`:
            *   `exportRegistrationStmt`: `Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.`
        *   `dataHandling`: `There are no specific handling instructions for this data module.`
        *   `dataDestruction`: `Users may destroy this data module in accordance with their own local procedures.`
        *   `dataDisclosure`: `There are no dissemination limitations that apply to this data module.`
    *   `restrictionInfo`:
        *   `copyright`:
            *   `copyrightText`: `Copyright (C) 2024 by AeroSpace, Security and Defence Industries Association of Europe - ASD`
            *   `publishers`:
                *   `publisher`: `Aerospace, Security and Defence Industries Association of Europe`
                *   `publisher`: `Aerospace Industries Association of America`
                *   `publisher`: `ATA e-Business Program`
            *   `limitationsOfLiability`:
                *   `limitation`: `This material is provided "As is" and neither ASD nor any person who has contributed to the creation, revision or maintenance of the material makes any representations or warranties, express or implied, including but not limited to, warranties of merchantability or fitness for any particular purpose.`
                *   `limitation`: `Neither ASD nor any person who has contributed to the creation, revision or maintenance of this material shall be liable for any direct, indirect, special or consequential damages or any other liability arising from any use of this material.`
                *   `limitation`: `Revisions to this document may occur after its issuance. The user is responsible for determining if revisions to the material contained in this document have occurred and are applicable.`
            *   `copyrightDetails`: `The details for copyright can be found in the S1000D Specification.`
        *   `policyStatement`: `S1000D-SC-2016-017-002-00 Steering Committee TOR`
        *   `dataConds`: `There are no known conditions that would change the data restrictions for, or security classification of, this data module.`

## responsiblePartnerCompany

*   `enterpriseCode`: `B6865`
*   `enterpriseName`: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`

## originator

*   `enterpriseCode`: `B6865`
*   `enterpriseName`: `AEROSPACE, SECURITY AND DEFENCE INDUSTRIES ASSOCIATION OF EUROPE`

## applicCrossReferenceTableRef

*   `dmRefIdent`:
    *   `dmCode`:
        *   `modelIdentCode`: `S1000DBIKE`
        *   `systemDiffCode`: `AAA`
        *   `systemCode`: `D00`
        *   `subSystemCode`: `0`
        *   `subSubSystemCode`: `0`
        *   `assyCode`: `00`
        *   `disassyCode`: `00`
        *   `disassyCodeVariant`: `AA`
        *   `infoCode`: `00W`
        *   `infoCodeVariant`: `A`
        *   `itemLocationCode`: `D`

## applic

*   `displayText`: `Mountain bicycle and (Mountain storm Mk1 or Brook trekker Mk9)`
*   `evaluate`:
    *   `andOr`: `and`
    *   `assert`:
        *   `applicPropertyIdent`: `type`
        *   `applicPropertyType`: `prodattr`
        *   `applicPropertyValues`: `Mountain bicycle`
    *   `evaluate`:
        *   `andOr`: `or`
        *   `evaluate`:
            *   `andOr`: `and`
            *   `assert`:
                *   `applicPropertyIdent`: `type`
                *   `applicPropertyType`: `prodattr`
                *   `applicPropertyValues`: `Mountain storm Mk1`
        *   `evaluate`:
            *   `andOr`: `and`
            *   `assert`:
                *   `applicPropertyIdent`: `type`
                *   `applicPropertyType`: `prodattr`
                *   `applicPropertyValues`: `Brook trekker Mk9`

## brexDMRef

*   `dmRefIdent`:
    *   `dmCode`:
        *   `modelIdentCode`: `S1000DBIKE`
        *   `systemDiffCode`: `AAA`
        *   `systemCode`: `D00`
        *   `subSystemCode`: `0`
        *   `subSubSystemCode`: `0`
        *   `assyCode`: `00`
        *   `disassyCode`: `00`
        *   `disassyCodeVariant`: `AA`
        *   `infoCode`: `00W`
        *   `infoCodeVariant`: `A`
        *   `itemLocationCode`: `D`

## procedure

*   `taskSequence`:
    *   `task`:
        *   `taskDescription`: `Put the bicycle on a flat surface.`
    *   `task`:
        *   `taskDescription`: `Put the bicycle on a flat surface.`
    *   `task`:
        *   `taskDescription`: `Put the bicycle on a flat surface.`
*   `step`:
    *   `stepNumber`: `1`
    *   `stepDescription`: `Put the bicycle on a flat surface.`

## closeRequirements

This section is empty.