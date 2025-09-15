# ICN Catalog Tool
## Description

The ICN catalog tool is used to resolve ICNs (Illustrated Parts Catalog Numbers) to filenames and notations. It uses an XML-based catalog file to map ICNs to their corresponding resolutions.

### Command Line Options

* `-c`, `--catalog`: Specify the path to the ICN catalog file.
* `-m`, `--media`: Specify the output media type (e.g., "pdf", "web").
* `-h`, `--help`: Display help information.
* `-v`, `--version`: Display version information.

### Catalog Schema

The ICN catalog file is an XML document that follows a specific schema. The root element is `<icnCatalog>`, which contains the following child elements:

#### Notation
* **Markup Element:** `<notation>`
* **Attributes:**
	+ `name`: The NDATA name.
	+ `publicId`: The optional PUBLIC ID of the notation.
	+ `systemId`: The optional SYSTEM ID of the notation.
* **Child Elements:** None

#### Media
* **Markup Element:** `<media>`
* **Attributes:**
	+ `name`: The identifier of the output media.
* **Child Elements:**
	+ `<icn>`

#### ICN
* **Markup Element:** `<icn>`
* **Attributes:**
	+ `type`: The type of ICN entry, with one of the following values:
		- `"single"` (D): Specifies a single ICN to resolve.
		- `"pattern"`: Specifies a pattern to resolve one or more ICNs.
	+ `infoEntityIdent`: The ICN, or pattern used to match ICNs.
	+ `uri`: The filename the ICN will resolve to.
	+ `notation`: A reference to a previously declared `<notation>` element.
* **Child Elements:** None

### Example ICN Catalog
```xml
<icnCatalog>
  <notation name="jpg" systemId="jpg"/>
  <notation name="png" systemId="png"/>
  <notation name="svg" systemId="svg"/>
  <media name="pdf">
    <icn infoEntityIdent="ICN-12345-00001-001-01"
         uri="ICN-12345-00001-001-01.JPG" notation="jpg"/>
  </media>
  <media name="web">
    <icn infoEntityIdent="ICN-12345-00001-001-01"
         uri="ICN-12345-00001-001-01.SVG" notation="svg"/>
  </media>
  <icn infoEntityIdent="ICN-12345-00001-001-01"
       uri="ICN-12345-00001-001-01.PNG" notation="png"/>
</icnCatalog>
```

### ICN Pattern Rules

By default, each catalog entry matches a single ICN, but multiple ICNs can be resolved with a single entry by using a pattern rule. An entry with attribute `type="pattern"` specifies a regular expression to use to match ICNs and a template used to construct the resolved URI.

For example:
```xml
<icn type="pattern"
     infoEntityIdent="ICN-(.{5})-(.*)"
     uri="graphics/\1/ICN-\1-\2.PNG"
     notation="PNG"/>
```
This entry would match a series of CAGE-based ICNs, resolving them to a subfolder of "graphics" based on their CAGE code.

### Use Cases

* Resolving ICNs to filenames and notations for a specific output media type.
* Using pattern rules to resolve multiple ICNs with a single catalog entry.
* Creating an ICN catalog file that maps ICNs to their corresponding resolutions.