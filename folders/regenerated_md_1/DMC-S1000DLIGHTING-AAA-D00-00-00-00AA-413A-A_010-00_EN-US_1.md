# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-413A-A_010-00_EN-US

## Ident and Status Section

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
*   **infoCode:** 413
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
*   **dmTitle:**
    *   **techName:** Lights
    *   **infoName:** Observed fault

### DM Status

*   **issueType:** changed
*   **security:**
    *   **securityClassification:** 01
    *   **commercialClassification:** cc51
    *   **caveat:** cv51
*   **dataRestrictions:**
    *   **restrictionInstructions:**
        *   **dataDistribution:** To be made available to all S1000D users.
        *   **exportControl:**
            *   **exportRegistrationStmt:**
                *   simplePara: Export of this data module to all countries that are the residence of organizations that are users of S1000D is permitted. Storage of this data module is to be at the discretion of the organization.
        *   **dataHandling:** There are no specific handling instructions for this data module.
        *   **dataDestruction:** Users may destroy this data module in accordance with their own local procedures.
        *   **dataDisclosure:** There are no dissemination limitations that apply to this data module.
    *   **restrictionInfo:**
        *   **copyright:**
            *   copyrightPara: *Copyright (C) 2024* by AeroSpace, Security and Defence Industries Association of Europe - ASD
            *   copyrightPara: *Publishers*
            *   random list item
        *   **remarks:** random remark
*   **applicability:** random applicability
*   **remarks:** random remark

### Additional DM Status Information

*   **responsibleParty:** random responsible party
*   **applicability:** random applicability
*   **remarks:** random remark

## Content

### References

#### DM Ref

*   **modelIdentCode:** S1000DLIGHTING
*   **systemDiffCode:** AAA
*   **systemCode:** D00
*   **subSystemCode:** 0
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 0A5
*   **disassyCodeVariant:** AA
*   **infoCode:** A
*   **itemLocationCode:** A

#### DM Ref

*   **modelIdentCode:** S1000DLIGHTING
*   **systemDiffCode:** AAA
*   **systemCode:** D00
*   **subSystemCode:** 0
*   **subSubSystemCode:** 0
*   **assyCode:** 00
*   **disassyCode:** 0A4
*   **disassyCodeVariant:** AA
*   **infoCode:** A
*   **itemLocationCode:** A

### Warnings and Cautions References

#### Warning Ref

*   **id:** w001
*   **warningIdentNumber:** warning-001
*   **dmRef:**
    *   **modelIdentCode:** S1000DLIGHTING
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 0A4
    *   **disassyCodeVariant:** AA
    *   **infoCode:** A
    *   **itemLocationCode:** A

#### Warning Ref

*   **id:** w002
*   **warningIdentNumber:** warning-002
*   **dmRef:**
    *   **modelIdentCode:** S1000DLIGHTING
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 0A4
    *   **disassyCodeVariant:** AA
    *   **infoCode:** A
    *   **itemLocationCode:** A

#### Caution Ref

*   **id:** c001
*   **cautionIdentNumber:** caution-001
*   **dmRef:**
    *   **modelIdentCode:** S1000DLIGHTING
    *   **systemDiffCode:** AAA
    *   **systemCode:** D00
    *   **subSystemCode:** 0
    *   **subSubSystemCode:** 0
    *   **assyCode:** 00
    *   **disassyCode:** 0A5
    *   **disassyCodeVariant:** AA
    *   **infoCode:** A
    *   **itemLocationCode:** A

### Fault Reporting

#### Preliminary Requirements

*   **reqCondGroup:**
    *   **noConds:**
*   **reqSupportEquips:**
    *   **noSupportEquips:**
*   **reqSupplies:**
    *   **noSupplies:**
*   **reqSpares:**
    *   **noSpares:**
*   **reqSafety:**
    *   **safetyRqmts:** cautionRefs="c001" warningRefs="w001 w002"

#### Observed Fault

*   **id:** flt-0001
*   **faultCode:** NYCJD02
*   **faultDescr:**
    *   descr: The lights are set to the dim position.
*   **contextAndIsolationInfo:**
    *   **faultContext:** During use or maintenance
    *   **isolationInfo:**
        *   **lruItem:**
            *   **lru:**
                *   name: Bulb
                *   identNumber:
                    *   manufacturerCode: KZ111
                    *   partAndSerialNumber:
                        *   partNumber: LiRUs-L1-11
                *   faultIsolationTest:
                    *   testType: Operation
                    *   testCode: O-001
                    *   testDescr:
                        *   testName: Test the bulbs
                    *   testParameters:
                        *   from: 1
                        *   to: 1
                        *   unitOfMeasure: Days
                    *   testProcedure:
                        *   refs:
                            *   dmRef:
                                *   dmRefIdent:
                                    *   dmCode:
                                        *   modelIdentCode: S1000DLIGHTING
                                        *   systemDiffCode: AAA
                                        *   systemCode: D00
                                        *   subSystemCode: 0
                                        *   subSubSystemCode: 0
                                        *   assyCode: 00
                                        *   disassyCode: 341
                                        *   disassyCodeVariant: A
                                        *   infoCode: A
                                        *   itemLocationCode: A
            *   repair:
                *   refs:
                    *   dmRef:
                        *   dmRefIdent:
                            *   dmCode:
                                *   modelIdentCode: S1000DLIGHTING
                                *   systemDiffCode: AAA
                                *   systemCode: D00
                                *   subSystemCode: 0
                                *   subSubSystemCode: 0
                                *   assyCode: 00
                                *   disassyCode: 921
                                *   disassyCodeVariant: A
                                *   infoCode: A
                                *   itemLocationCode: A
*   **remarks:**
    *   simplePara: This is the data module you would visit when you notice that the lights do not operate correctly.