# DMC-S1KDTOOLS-A-00-00-00-00A-920A-D_EN-CA
## Introduction to S1KD Tools
The s1kd-tools are a set of software tools used for building, installing, and uninstalling. This document provides guidelines on how to install, upgrade, or uninstall the s1kd-tools using a package manager or by building from source.

### Identifiers and Status
* **Model Identifier Code:** S1KDTOOLS
* **System Difference Code:** A
* **System Code:** 00
* **Sub-System Code:** 0
* **Sub-Sub-System Code:** 0
* **Assembly Code:** 00
* **Disassembly Code:** 00
* **Disassembly Code Variant:** A
* **Info Code:** 920
* **Info Code Variant:** A
* **Item Location Code:** D
* **Language:** English (en)
* **Country:** Canada (CA)
* **Issue Number:** 007
* **In Work:** 00

### Status Information
* **Issue Type:** status
* **Security Classification:** 01
* **Responsible Partner Company:** khzae.net
* **Originator:** khzae.net
* **Application:** All
* **Quality Assurance:** Unverified
* **Reason for Update:** Upissue

## Content
### Description
#### General
There are multiple ways to install the s1kd-tools:
* Using a package manager and pre-compiled Debian (.deb) or Red Hat (.rpm) packages
* Building from source

#### Using a Package Manager
Debian (.deb) and Red Hat (.rpm) packages are provided to easily install, upgrade, or uninstall the s1kd-tools on Linux systems using a package manager.

##### Installing
To install the s1kd-tools using a package manager:
1. Download the latest release from [http://khzae.net/1/s1000d/s1kd-tools/releases/latest](http://khzae.net/1/s1000d/s1kd-tools/releases/latest)
2. Use one of the following commands to install:
	* **Debian:** `# dpkg -i s1kd-tools_[version]_[arch].deb`
	* **Red Hat:** `# rpm -i s1kd-tools.[version].[arch].rpm`

##### Uninstalling
To uninstall using the package manager, use one of the following commands:
* **Debian:** `# dpkg -r s1kd-tools`
* **Red Hat:** `# rpm -e s1kd-tools`

#### Building from Source
To build the executables from source:

##### Requirements
The following are required to build the executables:
* coreutils and binutils
* xxd
* pkg-config
* [libxml2, libxslt, libexslt](http://xmlsoft.org)

To build the documentation from source:
* [s1kd2db](http://github.com/kibook/s1kd2db)
* [pandoc](https://pandoc.org/)

##### Windows Build Environment
To build the executables on Windows, an environment such as MinGW or Cygwin is recommended.

##### Building and Installing
Run the following commands to build the executables and install both the executables and documentation:
```bash
$ make
# make install
```
To change where these are installed, specify the PREFIX make variable. The default value of this variable is `/usr/local`.

For example:
```bash
# make PREFIX=/usr install
```

##### Uninstalling
To uninstall the executables and documentation:
```bash
# make uninstall
```
Remember to specify the PREFIX make variable if a different prefix was used during installation.

## References
The s1kd-tools reference the same schema as the original XML file, which can be found at [http://www.s1000d.org/S1000D_5-0/xml_schema_flat/descript.xsd](http://www.s1000d.org/S1000D_5-0/xml_schema_flat/descript.xsd).