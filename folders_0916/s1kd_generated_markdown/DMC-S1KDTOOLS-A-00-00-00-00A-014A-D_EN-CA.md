# Defaults Configuration
The defaults configuration is used to specify the default values for various parameters in the S1KD data module. The configuration can be provided in either XML or simple text format.

## Parameters
The following parameters can be specified in the defaults configuration:

| Parameter | Description |
| --- | --- |
| act | Activity code |
| assyCode | Assembly code |
| authorization | Authorization identifier |
| brex | BREX data module code |
| city | City name |
| commentPriorityCode | Comment priority code |
| commentType | Comment type |
| countryIsoCode | Country ISO code |
| country | Country name |
| disassyCodeVariant | Disassembly code variant |
| disassyCode | Disassembly code |
| dmlType | DML type |
| infoCodeVariant | Information code variant |
| infoCode | Information code |
| infoName | Information name |
| infoNameVariant | Information name variant |
| inWork | In-work identifier |
| issueNumber | Issue number |
| issueType | Issue type |
| issue | Issue identifier |
| itemLocationCode | Item location code |
| languageIsoCode | Language ISO code |
| learnCode | Learning code |
| learnEventCode | Learning event code |
| maintainedSns | Maintained SNS identifier |
| modelIdentCode | Model identification code |
| omitIssueInfo | Omit issue information flag |
| originatorCode | Originator code |
| originator | Originator identifier |
| pmIssuer | PM issuer identifier |
| pmNumber | PM number |
| pmVolume | PM volume |
| receiver | Receiver identifier |
| receiverCity | Receiver city name |
| receiverCountry | Receiver country name |
| receiverIdent | Receiver identification code |
| remarks | Remarks text |
| responsiblePartnerCompanyCode | Responsible partner company code |
| responsiblePartnerCompany | Responsible partner company identifier |
| schema | Schema file path |
| securityClassification | Security classification identifier |
| senderIdent | Sender identification code |
| seqNumber | Sequence number |
| skillLevelCode | Skill level code |
| sns | SNS identifier |
| snsLevels | SNS levels |
| subSubSystem | Sub-subsystem identifier |
| subSystem | Subsystem identifier |
| systemCode | System code |
| techName | Technical name |
| templates | Templates directory path |
| yearOfDataIssue | Year of data issue |

## Example - XML Format
```xml
<?xml version="1.0"?>
<defaults>
  <default ident="act" value="MYPRJ-A-00-00-00-00A-00WA-D"/>
  <default ident="assyCode" value="00"/>
  <default ident="authorization" value="khzae.net"/>
  <!-- ... -->
</defaults>
```

## Example - Simple Text Format
```
act                            MYPRJ-A-00-00-00-00A-00WA-D
assyCode                       00
authorization                  khzae.net
brex                           MYPRJ-A-00-00-00-00A-022A-D
city                           Toronto
commentPriorityCode            cp01
commentType                    Q
countryIsoCode                 CA
country                        Canada
disassyCodeVariant             A
disassyCode                    00
dmlType                        C
infoCodeVariant                A
infoCode                       258
infoName                       Other procedure to clean
infoNameVariant                Clean with water
inWork                         01
issueNumber                    000
issueType                      new
issue                          5.0
itemLocationCode               D
languageIsoCode                en
learnCode                      H10
learnEventCode                 A
maintainedSns                  General sea vehicles
modelIdentCode                 MYPRJ
omitIssueInfo                  true
originatorCode                 12345
originator                     khzae.net
pmIssuer                       12345
pmNumber                       00000
pmVolume                       00
receiver                       khzae.net
receiverCity                   Toronto
receiverCountry                Canada
receiverIdent                  12345
remarks                        Comments on a data module
responsiblePartnerCompanyCode  12345
responsiblePartnerCompany      khzae.net
schema                         descript.xsd
securityClassification         01
sender                         khzae.net
senderIdent                    12345
seqNumber                      00001
skillLevelCode                 sk01
sns                            MYPRJ-A-00-00-00-00A-022A-D
snsLevels                      1
subSubSystem                   0
subSystem                      0
systemCode                     00
techName                       My project
templates                      /usr/share/s1kd-tools/templ
yearOfDataIssue                2017
```