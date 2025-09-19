Business Rules Document
=======================

## Introduction

This document outlines the business rules for the Bike data set. These rules are designed to ensure consistency and quality in the data.

## Decision Table

The following decisions have been made regarding the Bike data set:

### BIKE-BR-00070: Maintenance Level

* **Decision**: The maintenance level will be one of the following:
	+ Level 1 (home)
	+ Level 2 (authorized workshop)

### BIKE-BR-00071: Origin of Equipment/Harness/Wire

* **Decision**: The origin of equipment/harness/wire will be one of the following:
	+ Manufacturer
	+ Vendor
	+ Partner

### BIKE-BR-00072: Task Code

* **Decision**: The task code will be one of the following:
	+ Detailed inspection (DET)
	+ Discard (DIS)
	+ Functional Check (FNC)
	+ General visual inspection (GVI)
	+ Lubrication (LUB)
	+ Operational check (OPC)
	+ Restoration (RST)
	+ Servicing (SVC)
	+ Visual check (VCK)

### BIKE-BR-00073: Limit Type

* **Decision**: The limit type will be one of the following:
	+ Time between overhaul
	+ Hard time
	+ Since last maintenance
	+ Out time limit
	+ On condition
	+ Check maintenance
	+ Functional check

### BIKE-BR-00074: Unit of Measurement for Threshold Interval

* **Decision**: The unit of measurement for the threshold interval will be one of the following:
	+ Months
	+ Weeks
	+ Years
	+ Days
	+ Shop visits
	+ Auxiliary power unit change
	+ Wheel change
	+ Kilometer

### BIKE-BR-00075: Attribute SourceTypeCode

* **Decision**: The attribute sourceTypeCode will be one of the following:
	+ fec
	+ sample

### BIKE-BR-00076: Attribute SourceCriticality

* **Decision**: The attribute sourceCriticality will be one of the following:
	+ Evident, Safety
	+ Evident, operational
	+ Evident, Economic
	+ Hidden, Safety
	+ Hidden, Non-Safety

### BIKE-BR-00077: Review and Approval Process

* **Decision**: Bike data modules must be reviewed and approved by EPWG before publishing.

### BIKE-BR-00078: Content Requirements

* **Decision**: The Bike data set must contain examples of how to apply constructs and principles representing various levels of concept sophistication.

## Conclusion

These business rules are designed to ensure the quality and consistency of the Bike data set. They cover a range of topics, including maintenance level, origin of equipment/harness/wire, task code, limit type, unit of measurement for threshold interval, attribute sourceTypeCode, attribute sourceCriticality, review and approval process, and content requirements.

## References

* S1000D Issue 4.1
* ASD S3000L Issue 6.2
* ATA iSpec 2200 Issue 3.0

Note: The references provided are examples and may need to be updated based on the specific requirements of your project.