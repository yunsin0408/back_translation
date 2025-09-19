```markdown
# DMC-S1000DLIGHTING-AAA-D00-00-00-00AA-029A-A_010-00_EN-US_1_1

## Applicability

### DM Address

#### DM Ident

*   **modelIdentCode**: S1000DLIGHTING
*   **systemDiffCode**: AAA
*   **systemCode**: D00
*   **subSystemCode**: 0
*   **subSubSystemCode**: 0
*   **assyCode**: 00
*   **disassyCode**: 00
*   **disassyCodeVariant**: AA
*   **infoCode**: 029
*   **infoCodeVariant**: A
*   **itemLocationCode**: A

#### Language

*   **countryIsoCode**: US
*   **languageIsoCode**: en

#### Issue Info

*   **issueNumber**: 010
*   **inWork**: 0

### DM Issue

*   **issueDate**: 2019-01-28

### DM Status

*   **status**: Released

### DM Configuration Management

*   Not applicable

### DM Related Documents

*   Not applicable

## Content

### Wiring Fields

#### DescrWire

| Field Name                  | Description                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Field Name                  | Description of the field. (Repeated for each field)                                                          |
| Wire                        | Contains the sequential number of the wire, e.g. in the harness.                                              |
| Harness ident               | Harness ident identifies pre-assembled wires, which are installed on the bicycle.                           |
| Wire sequential number      | Contains the sequential number of the wire, e.g. in the harness.                                              |
| Wire information circuit code | Contains the identifier of the circuit to which the wire belongs.                                               |
| Wire information wire section identification | Contains the identifier of the section to which the wire belongs.                                            |
| Length                       | Length identifies the length of the wire. The given value is approximately 10% higher than necessary to install the wire on the bicycle. |
| Color                        | Color identifies the color of the wire sheating.                                                             |
| Twisting                     | Twistig identifies wires, which are twisted together with a unique identifier.                               |
| Electric ident              | Electric ident shows the electrical identification, to which the wire is connected. It is available for all electrical equipment, eg L1. |
| Contact                      | Contact identifies the electrical contact to which the wire is connected.                                       |
| Group code                   | Identifies wires, which are connected to the same terminal lug.                                               |
| Screens                      | Screens identifies all screens that shield the wire. Wires shielded by the same screen are identified by the same screens value. |
| Responsible partner company | The responsible partner company indicates the company responsible for the integration of the wire to the bicycle. |
| Feed-through                 | Identifies bunges through which the wire is routed.                                                           |
| Next higher assembly        | Identifies the next higher assenbly, in which the wire is installed.                                          |

#### DescrHarness

| Field Name              | Description                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| Field Name              | Description of the field. (Repeated for each field)                                                       |
| Harness ident           | Harness ident identifies pre-assembled wires, which are installed on the bicycle.                        |
| Harness Part number     | Harness part number gives the part number of the harness identified by the harness ident.                 |
| Harness variant         | Harness variant identifies the variant of the harness in addition to the harness part number.            |
| Harness issue           | Harness issue identifies the production variant of the harness in addition to the harness part number.     |
| Harness nomenclature    | Harness nomenclature identifies the harness by using a specific name.                                     |
| Harness separation code | Harness separation code gives the separation code of the harness.                                           |
| Minimum temperature     | Minimum temperature gives the minimum environment temperature in which the harness can be used.              |
| Maximum temperature     | Maximum temperature gives the maximum environment temperature in which the harness can be used.              |
| Harness environment     | Harness environment indicates that a harness is used in high vibriation or/and hydraulic areas.             |
| Sleeve                  | Gives the part number and/or the material of the sleeves used on the harness.                               |
| Responsible partner company | The responsible partner company indicates the company responsible for the integration of the harness to the bicycle. |

#### DescrElectricalEquip

| Field Name                | Description                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------- |
| Field Name                | Description of the field. (Repeated for each field)                                                     |
| Electric ident            | Electric ident shows the electrical identification, which is available for all electrical equipment, eg L1. |
| Part identification       | Part identification shows the part number of the equipment. In most cases the part number is identical to the part desciption. |
| Location                  | Location shows the installation position of the equipment on the bicycle.                                  |
| Next higher assenmbly    | Next higher assenmbly identifies the box or panel, in which the equipment is installed.                   |
| Position on next higher assenmbly | Gives the position on the next higher assembly, in which the equipment is installed.                         |
| Maximum number of mounting positions | Gives the maximum number of mounting positions on the next higher assembly.                                |
| Sibling plug identification | Sibling plug identification contains the electric ident of the mating connector.                              |
| Transverse link           | Transverse link shows external or internal electrical connections of the equipment.                         |
| Responsible partner company | The responsible partner company indicates the company responsible for the integration of the equipment to the bicycle. |
| Quantity                   | Gives the quantity of multiple occurence equipment.                                                        |
```