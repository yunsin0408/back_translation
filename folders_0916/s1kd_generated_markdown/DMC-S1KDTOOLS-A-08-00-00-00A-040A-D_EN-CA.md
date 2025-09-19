# S1KD Reference Tool
=====================================

## Overview
---------------

The S1KD reference tool is designed to generate references for various types of documents and entities in the S1000D standard. This tool supports multiple reference types, including data modules, comments, information control numbers, publication modules, SCORM content packages, and external publications.

## Command-Line Options
-------------------------

The following command-line options are available:

* `-d`: Include all information (data module code, issue info, language, title, and date) in the reference.
* `-i`: Include issue info (issue number and in-work) in the reference.
* `-l`: Include language info (language ISO code and country ISO code) in the reference.
* `-t`: Include title info (technical name and information name) in the reference.
* `-u`: Include URL or filename of the referenced document.
* `-S`: Generate a source identification for a data module, publication module, or SCORM content package.
* `-R`: Generate a repository source identification for a CIR data module.

## Reference Types
---------------------

The tool supports the following reference types:

1. **Data Module (DM)**: A data module is a self-contained unit of information that describes a specific aspect of an aircraft or system.
2. **Comment**: A comment is a response to a data module or other document, providing additional context or clarification.
3. **Information Control Number (ICN)**: An ICN is a unique identifier assigned to a document or set of documents for tracking and control purposes.
4. **Publication Module (PM)**: A publication module is a collection of data modules and other information that comprise a published document, such as a manual or guide.
5. **SCORM Content Package**: A SCORM content package is a self-contained unit of learning content that can be delivered through an LMS.
6. **External Publication**: An external publication is a document or resource that is not part of the S1000D standard but may be referenced within it.

## Examples
-------------

### Data Module Reference

* `s1kd-ref -d DMC-EX-A-00-00-00-00A-040A-D_001-03_EN-CA.XML`
```xml
<dmRef>
  <dmRefIdent>
    <dmCode modelIdentCode="EX" systemDiffCode="A" systemCode="00"
      subSystemCode="0" subSubSystemCode="0" assyCode="00" disassyCode="00"
      disassyCodeVariant="A" infoCode="040" infoCodeVariant="A"
      itemLocationCode="D"/>
    <issueInfo issueNumber="001" inWork="03"/>
    <language languageIsoCode="en" countryIsoCode="CA"/>
  </dmRefIdent>
  <dmRefAddressItems>
    <dmTitle>
      <techName>Example</techName>
      <infoName>Description</infoName>
    </dmTitle>
    <issueDate year="2018" month="06" day="25"/>
  </dmRefAddressItems>
</dmRef>
```

### Comment Reference

* `s1kd-ref COM-EX-12345-2018-00001-Q`
```xml
<commentRef>
  <commentRefIdent>
    <commentCode modelIdentCode="EX" senderIdent="12345"
      yearOfDataIssue="2018" seqNumber="00001" commentType="q"/>
  </commentRefIdent>
</commentRef>
```

### Information Control Number Reference

* `s1kd-ref ICN-EX-A-000000-A-00001-A-001-01`
```xml
<infoEntityRef infoEntityRefIdent="ICN-EX-A-000000-A-00001-A-001-01"/>
```

### Publication Module Reference

* `s1kd-ref PMC-EX-12345-00001-00`
```xml
<pmRef>
  <pmRefIdent>
    <pmCode modelIdentCode="EX" pmIssuer="12345" pmNumber="00001"
      pmVolume="00"/>
  </pmRefIdent>
</pmRef>
```

### SCORM Content Package Reference

* `s1kd-ref SMC-EX-12345-00001-00`
```xml
<scormContentPackageRef>
  <scormContentPackageRefIdent>
    <scormContentPackageCode
      modelIdentCode="EX"
      scormContentPackageIssuer="12345"
      scormContentPackageNumber="00001"
      scormContentPackageVolume="00"/>
  </scormContentPackageRefIdent>
</scormContentPackageRef>
```

### External Publication Reference

* `s1kd-ref ABC`
```xml
<externalPubRef>
  <externalPubRefIdent>
    <externalPubCode>ABC</externalPubCode>
  </externalPubRefIdent>
</externalPubRef>
```

## Source Identification
---------------------------

The tool can generate source identification for data modules, publication modules, and SCORM content packages using the `-S` option.

### Data Module Source Identification

* `s1kd-ref -S DMC-EX-A-00-00-00-00A-040A-D_001-03_EN-CA.XML`
```xml
<sourceDmIdent>
  <dmCode modelIdentCode="EX" systemDiffCode="A" systemCode="00"
    subSystemCode="0" subSubSystemCode="0" assyCode="00" disassyCode="00"
    disassyCodeVariant="A" infoCode="040" infoCodeVariant="A"
    itemLocationCode="D"/>
  <language languageIsoCode="en" countryIsoCode="CA"/>
  <issueInfo issueNumber="001" inWork="03"/>
</sourceDmIdent>
```

### Publication Module Source Identification

* `s1kd-ref -S PMC-EX-12345-00001-00_001-03_EN-CA.XML`
```xml
<sourcePmIdent>
  <pmCode modelIdentCode="EX" pmIssuer="12345" pmNumber="00001"
    pmVolume="00"/>
  <language languageIsoCode="en" countryIsoCode="CA"/>
  <issueInfo issueNumber="001" inWork="03"/>
</sourcePmIdent>
```

### SCORM Content Package Source Identification

* `s1kd-ref -S SMC-EX-12345-00001-00_001-03_EN-CA.XML`
```xml
<sourceScormContentPackageIdent>
  <scormContentPackageCode
    modelIdentCode="EX"
    scormContentPackageIssuer="12345"
    scormContentPackageNumber="00001"
    scormContentPackageVolume="00"/>
  <language languageIsoCode="en" countryIsoCode="CA"/>
  <issueInfo issueNumber="001" inWork="03"/>
</sourceScormContentPackageIdent>
```

### Repository Source Identification

* `s1kd-ref -R DMC-EX-A-00-00-00-00A-00GA-D_001-03_EN-CA.XML`
```xml
<repositorySourceDmIdent>
  <dmCode modelIdentCode="EX" systemDiffCode="A" systemCode="00"
    subSystemCode="0" subSubSystemCode="0" assyCode="00" disassyCode="00"
    disassyCodeVariant="A" infoCode="00G" infoCodeVariant="A"
    itemLocationCode="D"/>
  <language languageIsoCode="en" countryIsoCode="CA"/>
  <issueInfo issueNumber="001" inWork="03"/>
</repositorySourceDmIdent>
```