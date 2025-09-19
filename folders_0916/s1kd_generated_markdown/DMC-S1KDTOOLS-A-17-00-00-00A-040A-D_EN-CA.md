DMC-S1KDTOOLS-A-17-00-00-00A-040A-D EN CA
============================================

### Ident and Status Section

The `identAndStatusSection` contains information about the identification and status of the data module.

#### DM Address

*   **DM Ident:**
    *   Model Ident Code: `S1KDTOOLS`
    *   System Diff Code: `A`
    *   System Code: `17`
    *   Sub System Code: `0`
    *   Sub Sub System Code: `0`
    *   Assy Code: `00`
    *   Disassy Code: `00`
    *   Disassy Code Variant: `A`
    *   Info Code: `040`
    *   Info Code Variant: `A`
    *   Item Location Code: `D`
*   **Language:**
    *   Language Iso Code: `en`
    *   Country Iso Code: `CA`
*   **Issue Info:**
    *   Issue Number: `029`
    *   In Work: `00`

#### DM Address Items

*   **Issue Date:**
    *   Year: `2020`
    *   Month: `09`
    *   Day: `01`
*   **DM Title:**
    *   Tech Name: `s1kd-newddn`
    *   Info Name: `Description`

#### DM Status

*   **Issue Type:** `changed`
*   **Security:**
    *   Security Classification: `01`
*   **Responsible Partner Company:**
    *   Enterprise Name: `khzae.net`
*   **Originator:**
    *   Enterprise Name: `khzae.net`
*   **Applic:**
    *   Display Text: `All`
*   **BrexDm Ref:**
    *   DM Ref Ident:
        *   Model Ident Code: `S1KDTOOLS`
        *   System Diff Code: `A`
        *   System Code: `00`
        *   Sub System Code: `0`
        *   Sub Sub System Code: `0`
        *   Assy Code: `00`
        *   Disassy Code: `00`
        *   Disassy Code Variant: `A`
        *   Info Code: `022`
        *   Info Code Variant: `A`
        *   Item Location Code: `D`

#### Quality Assurance

*   **Unverified:** 

#### Reason for Update

*   **Id:** `rfu-xml-catalog`
*   **Update Highlight:** `1`
*   **Update Reason Type:** `urt02`
*   **Simple Para:** Add --xml-catalog parser option.

### Content

The `content` section contains information about the data module's content.

#### Refs

*   **DM Ref:**
    *   DM Ref Ident:
        *   Model Ident Code: `S1KDTOOLS`
        *   System Diff Code: `A`
        *   System Code: `07`
        *   Sub System Code: `0`
        *   Sub Sub System Code: `0`
        *   Assy Code: `00`
        *   Disassy Code: `00`
        *   Disassy Code Variant: `A`
        *   Info Code: `040`
        *   Info Code Variant: `A`
        *   Item Location Code: `D`
    *   DM Ref Address Items:
        *   DM Title:
            *   Tech Name: `s1kd-newdm`
            *   Info Name: `Description`

#### Description

The `description` section contains a detailed description of the data module.

##### General

*   The `s1kd-newddn` tool creates a new S1000D data dispatch note with the code, metadata, and list of files specified.

##### Usage

*   **Command:** `s1kd-newddn -# EX-12345-54321-2018-00001`

##### Options

The following options are available for the `s1kd-newddn` command:

| Option | Description |
| --- | --- |
| `-#` | Specify the data dispatch note code. |
| `-o` | Specify the sender's enterprise name. |
| `-r` | Specify the receiver's enterprise name. |
| `-n` | Specify the sender's country. |
| `-N` | Specify the receiver's country. |
| `-t` | Specify the sender's city. |
| `-T` | Specify the receiver's city. |
| `-m` | Set the remarks for the new data dispatch note. |
| `-p` | Prompt the user for values left unspecified. |
| `-q` | Do not report an error when the file already exists. |
| `-v` | Print the file name of the newly created DDN. |
| `--version` | Show version information. |

Additional options are available to configure the XML parser:

| Option | Description |
| --- | --- |
| `--dtdload` | Load the external DTD. |
| `--huge` | Remove any internal arbitrary parser limits. |
| `--net` | Allow network access to load external DTD and entities. |
| `--noent` | Resolve entities. |
| `--parser-errors` | Emit errors from parser. |
| `--parser-warnings` | Emit warnings from parser. |
| `--xinclude` | Do XInclude processing. |
| `--xml-catalog` | Use an XML catalog when resolving entities. |

##### .defaults File

Refer to the [s1kd-newdm](#) documentation for information on the `.defaults` file, which is used by all the `s1kd-new*` commands.

##### Example

*   **Command:** `$ s1kd-newddn -# EX-12345-54321-2018-00001`