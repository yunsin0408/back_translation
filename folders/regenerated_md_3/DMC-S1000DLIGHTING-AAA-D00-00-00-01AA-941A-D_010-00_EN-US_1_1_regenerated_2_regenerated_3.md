# DMC-S1000DLIGHTING Configuration

This document represents the configuration for the DMC-S1000D Lighting System. It adheres to the S1000D standard and references the `proced.xsd` schema.

## Configuration Details

*   **Configuration Name:** DMC-S1000DLIGHTING Configuration
*   **Configuration Version:** AAA-D00-00-00-01AA-941A-D\_010-00

### Localization

*   **Language:** EN
*   **Country:** US
*   **Version:** 1.1

## System Configuration

### General Settings

*   **System Name:** Main Lighting System
*   **Timezone:** America/Los\_Angeles
*   **Units:** Imperial

### Network Settings

*   **IP Address:** 192.168.1.100
*   **Subnet Mask:** 255.255.255.0
*   **Gateway:** 192.168.1.1

## Lighting Zones

### Zone 1: Living Room

*   **id:** 1
*   **name:** Living Room
*   **Description:** Main living area lighting

#### Lights

| Type     | id   | Brightness | Color       |
| -------- | ---- | ---------- | ----------- |
| Ceiling  | 101  | 100        | WarmWhite   |
| Lamp     | 102  | 60         | CoolWhite   |

### Zone 2: Kitchen

*   **id:** 2
*   **name:** Kitchen
*   **Description:** Kitchen area lighting

#### Lights

| Type     | id   | Brightness | Color     |
| -------- | ---- | ---------- | --------- |
| Ceiling  | 201  | 80         | Daylight  |

## Schedules

### Schedule 1: WeekdayMorning

*   **id:** 1
*   **name:** WeekdayMorning
*   **StartTime:** 06:00
*   **EndTime:** 08:00
*   **Brightness:** 50

#### Zones

*   **ZoneId:** 1
*   **ZoneId:** 2