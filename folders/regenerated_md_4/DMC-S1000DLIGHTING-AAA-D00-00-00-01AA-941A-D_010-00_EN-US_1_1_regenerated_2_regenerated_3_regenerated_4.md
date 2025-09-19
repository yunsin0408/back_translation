# DMC-S1000DLIGHTING Configuration Document

This document represents the configuration for the DMC-S1000DLIGHTING system, adhering to the S1000D standard.

## dmc_s1000dlighting

*   **xmlns:dc**: [http://www.purl.org/dc/elements/1.1/](http://www.purl.org/dc/elements/1.1/)
*   **xmlns:rdf**: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#)
*   **xmlns:xlink**: [http://www.w3.org/1999/xlink](http://www.w3.org/1999/xlink)
*   **xmlns:xsi**: [http://www.w3.org/2001/XMLSchema-instance](http://www.w3.org/2001/XMLSchema-instance)
*   **xsi:noNamespaceSchemaLocation**: [http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd](http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd)

## dmc_s1000dlighting_configuration

### configuration_name

`DMC-S1000DLIGHTING Configuration`

### configuration_version

`AAA-D00-00-00-01AA-941A-D_010-00`

### localization

*   **language**: `EN`
*   **country**: `US`
*   **version**: `1.1`

### system_configuration

#### general_settings

*   **system_name**: `Main Lighting System`
*   **timezone**: `America/Los_Angeles`
*   **units**: `Imperial`

#### network_settings

*   **ip_address**: `192.168.1.100`
*   **subnet_mask**: `255.255.255.0`
*   **gateway**: `192.168.1.1`

### lighting_zones

#### zone 1

*   **id**: `1`
*   **name**: `Living Room`
*   **description**: `Main living area lighting`

##### lights

*   **light 1**
    *   **type**: `Ceiling`
    *   **id**: `101`
    *   **brightness**: `100`
    *   **color**: `WarmWhite`

*   **light 2**
    *   **type**: `Lamp`
    *   **id**: `102`
    *   **brightness**: `60`
    *   **color**: `CoolWhite`

#### zone 2

*   **id**: `2`
*   **name**: `Kitchen`
*   **description**: `Kitchen area lighting`

##### lights

*   **light 1**
    *   **type**: `Ceiling`
    *   **id**: `201`
    *   **brightness**: `80`
    *   **color**: `Daylight`

### schedules

#### schedule 1

*   **id**: `1`
*   **name**: `WeekdayMorning`
*   **start_time**: `06:00`
*   **end_time**: `08:00`
*   **brightness**: `50`

##### zones

*   **zone_id**: `1`
*   **zone_id**: `2`