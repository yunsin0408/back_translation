# Units of Measure
## Introduction
The units of measure are used to specify the unit of measurement for a quantity. This can include length, weight, time, etc.

## Customizing Units of Measure
Custom units of measure can be defined in an XML file. The following elements are supported:

### Format Element
*   **Name**: The name of the format.
*   **Decimal Separator**: The decimal separator to use.
*   **Grouping Separator**: The grouping separator to use.

Example:
```xml
<format name="custom" decimalSeparator="." groupingSeparator=","></format>
```

### Group Type Prefixes Element
This element specifies prefixes which are added for specific group types. Supported child elements include:

*   **Nominal**: Text placed before a nominal group.
*   **Minimum**: Text placed before a minimum group.
*   **Minimum Range**: Text placed before a minimum group that is followed by a maximum group to specify a range.
*   **Maximum**: Text placed before a maximum group.
*   **Maximum Range**: Text placed before a maximum group that is preceded by a minimum group to specify a range.

Example:
```xml
<groupTypePrefixes>
    <nominal>Approx. </nominal>
    <minimum>Min. </minimum>
    <maximum>Max. </maximum>
</groupTypePrefixes>
```

### Wrap Into Element
This element contains one child element of any type, which quantities will be wrapped in to after formatting.

Example:
```xml
<wrapInto>
    <span></span>
</wrapInto>
```

### Units of Measure Element
*   **Name**: The name of the unit of measure.
*   Child elements: Mixed content that will be used for the display of the unit of measure. This can include XSLT elements.

Example:
```xml
<uoms>
    <uom name="meter">m</uom>
    <uom name="kilogram">kg</uom>
</uoms>
```

### Currencies Element
*   Child elements: Currency elements that define the display of a currency.
*   XSLT elements can be used to handle complex cases of currency display.

Example:
```xml
<currencies>
    <currency name="USD">
        <prefix>$</prefix>
        <postfix></postfix>
    </currency>
    <currency name="EUR">
        <prefix>€</prefix>
        <postfix></postfix>
    </currency>
</currencies>
```

## Common Use Cases
Here are some common use cases for custom units of measure:

*   Converting between different units of measurement (e.g., length, weight).
*   Displaying quantities with custom units of measure.
*   Handling complex cases of unit display, such as pluralization.

### Example Usage

```xml
<uoms>
    <uom name="foot">
        <xsl:choose>
            <xsl:when test=". = 1">ft</xsl:when>
            <xsl:otherwise>ft</xsl:otherwise>
        </xsl:choose>
    </uom>
</uoms>
```

This example uses XSLT to display the unit "foot" as "ft" for both singular and plural quantities.

## Best Practices
Here are some best practices for working with custom units of measure:

*   Use meaningful names for your custom units of measure.
*   Keep your XML files well-organized and easy to read.
*   Test your custom units of measure thoroughly to ensure they work as expected.