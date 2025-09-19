Applicability Display
======================
### Introduction

The applicability display is used to show the applicability of a specific data module or set of data modules. 

### Applicability Assertion

An applicability assertion is an expression that specifies which data items are applicable for a particular product or situation.

#### Example Use Cases

* Data modules with applicability assertions can be combined into a single data package, allowing for easier management and maintenance.
* The applicability display can be used to create user-friendly interfaces for selecting and viewing applicable data.

### Displaying Applicability

To display the applicability of a data module or set of data modules, the following information is required:

* The data module(s) to be displayed
* The product or situation for which the applicability is being determined
* Any relevant conditions or constraints that affect the applicability

#### Steps to Display Applicability

1. **Determine the applicable data items**: Use the applicability assertion to determine which data items are applicable for the given product or situation.
2. **Filter out non-applicable data items**: Remove any data items that do not match the conditions specified in the applicability assertion.
3. **Display the applicable data items**: Show the remaining data items in a clear and concise manner, using a format that is easy to understand.

### Display Rules

The display rules are used to determine how the applicability of a data module or set of data modules should be displayed. 

#### Types of Display Rules

* **Simple display rule**: Displays the applicable data items in a simple list or table.
* **Conditional display rule**: Displays different information depending on the conditions specified in the applicability assertion.

### Example Display Rule

The following is an example of a display rule:
```markdown
IF condition = "temperature" THEN
  DISPLAY "Temperature: " + value
ELSE IF condition = "pressure" THEN
  DISPLAY "Pressure: " + value
END IF
```
This display rule checks the condition specified in the applicability assertion and displays different information depending on the value of the condition.

### Formatting Applicability Display

The formatting of the applicability display can be customized using a variety of options, including:

* **Text formatting**: Font size, color, and style can be used to highlight important information or make the display more visually appealing.
* **Tables and lists**: Data items can be displayed in tables or lists to make it easier to compare and contrast different values.

### Customizing Applicability Display

The applicability display can be customized using a variety of techniques, including:

* **Using custom labels**: Custom labels can be used to replace default text with more descriptive or user-friendly language.
* **Adding conditional logic**: Conditional logic can be added to the display rule to handle complex conditions or exceptions.

### Best Practices for Applicability Display

The following are some best practices for displaying applicability:

* **Keep it simple**: Avoid using complicated or confusing language in the display rule.
* **Use clear and concise formatting**: Use tables, lists, and other formatting options to make the display easy to read and understand.
* **Test thoroughly**: Test the display rule with different inputs and conditions to ensure that it is working correctly.

### Conclusion

The applicability display is a powerful tool for showing the applicability of data modules or sets of data modules. By using custom display rules, formatting options, and best practices, users can create clear and concise displays that meet their specific needs. 

Display Rules
-------------

### Introduction to Display Rules

A display rule is used to determine how the applicability of a data module or set of data modules should be displayed.

### Types of Display Rules

There are two types of display rules:

* **Simple display rule**: Displays the applicable data items in a simple list or table.
* **Conditional display rule**: Displays different information depending on the conditions specified in the applicability assertion.

### Example Display Rule

The following is an example of a display rule:
```markdown
IF condition = "temperature" THEN
  DISPLAY "Temperature: " + value
ELSE IF condition = "pressure" THEN
  DISPLAY "Pressure: " + value
END IF
```
This display rule checks the condition specified in the applicability assertion and displays different information depending on the value of the condition.

### Creating Custom Display Rules

To create a custom display rule, follow these steps:

1. **Determine the conditions**: Determine which conditions will be used to determine the applicability of the data module or set of data modules.
2. **Specify the display format**: Specify how the applicable data items should be displayed, including any text formatting, tables, or lists.
3. **Add conditional logic**: Add conditional logic to the display rule to handle complex conditions or exceptions.

### Example Custom Display Rule

The following is an example of a custom display rule:
```markdown
IF condition = "temperature" AND value > 100 THEN
  DISPLAY "High Temperature: " + value
ELSE IF condition = "pressure" AND value < 50 THEN
  DISPLAY "Low Pressure: " + value
END IF
```
This custom display rule checks the condition and value specified in the applicability assertion and displays different information depending on the values.

### Display Rule Markup Elements
The following markup elements can be used to create custom display rules:

* **`<name>`**: Replaced by the name of the property.
* **`<text>`**: Text that is included as-is.
* **`<values>`**: Replaced by the values specified for the property in the applicability assertion.

### Display Rule Attributes
The following attributes can be used to customize the display rule:

* **`ident`**: The ID of the condition type in the CCT.
* **`type`**: The type of the property, either "condition" or "prodattr".
* **`match`**: The value to apply the custom label for.

### Conclusion

Display rules are a powerful tool for customizing the display of applicability. By using simple and conditional display rules, custom formatting options, and markup elements, users can create clear and concise displays that meet their specific needs. 

Applicability Assertion
----------------------

### Introduction to Applicability Assertions

An applicability assertion is an expression that specifies which data items are applicable for a particular product or situation.

### Creating Applicability Assertions

To create an applicability assertion, follow these steps:

1. **Determine the conditions**: Determine which conditions will be used to determine the applicability of the data module or set of data modules.
2. **Specify the applicable data items**: Specify which data items are applicable for each condition.
3. **Add conditional logic**: Add conditional logic to the applicability assertion to handle complex conditions or exceptions.

### Example Applicability Assertion

The following is an example of an applicability assertion:
```markdown
IF product = "car" AND model = "sedan" THEN
  INCLUDE data_item_1, data_item_2
ELSE IF product = "truck" AND model = "pickup" THEN
  INCLUDE data_item_3, data_item_4
END IF
```
This applicability assertion checks the product and model specified in the condition and includes different data items depending on the values.

### Applicability Assertion Markup Elements
The following markup elements can be used to create custom applicability assertions:

* **`<name>`**: Replaced by the name of the property.
* **`<text>`**: Text that is included as-is.
* **`<values>`**: Replaced by the values specified for the property in the applicability assertion.

### Applicability Assertion Attributes
The following attributes can be used to customize the applicability assertion:

* **`ident`**: The ID of the condition type in the CCT.
* **`type`**: The type of the property, either "condition" or "prodattr".
* **`match`**: The value to apply the custom label for.

### Conclusion

Applicability assertions are a powerful tool for specifying which data items are applicable for a particular product or situation. By using simple and conditional applicability assertions, custom formatting options, and markup elements, users can create clear and concise displays that meet their specific needs. 

Product Attributes
-----------------

### Introduction to Product Attributes

A product attribute is a characteristic of a product that can be used to determine its applicability.

### Types of Product Attributes

There are two types of product attributes:

* **Simple product attribute**: A product attribute with a single value.
* **Complex product attribute**: A product attribute with multiple values or conditional logic.

### Example Product Attribute

The following is an example of a product attribute:
```markdown
PRODUCT ATTRIBUTE: color
VALUES: red, blue, green
```
This product attribute has three possible values: red, blue, and green.

### Creating Custom Product Attributes

To create a custom product attribute, follow these steps:

1. **Determine the characteristic**: Determine which characteristic of the product will be used to determine its applicability.
2. **Specify the values**: Specify the possible values for the characteristic.
3. **Add conditional logic**: Add conditional logic to the product attribute to handle complex conditions or exceptions.

### Example Custom Product Attribute

The following is an example of a custom product attribute:
```markdown
PRODUCT ATTRIBUTE: size
VALUES: small, medium, large
CONDITION: IF product = "car" THEN size = "small"
```
This custom product attribute has three possible values: small, medium, and large. The condition specifies that if the product is a car, then the size must be small.

### Product Attribute Markup Elements
The following markup elements can be used to create custom product attributes:

* **`<name>`**: Replaced by the name of the property.
* **`<text>`**: Text that is included as-is.
* **`<values>`**: Replaced by the values specified for the property in the applicability assertion.

### Product Attribute Attributes
The following attributes can be used to customize the product attribute:

* **`ident`**: The ID of the condition type in the CCT.
* **`type`**: The type of the property, either "condition" or "prodattr".
* **`match`**: The value to apply the custom label for.

### Conclusion

Product attributes are a powerful tool for specifying characteristics of a product that can be used to determine its applicability. By using simple and complex product attributes, custom formatting options, and markup elements, users can create clear and concise displays that meet their specific needs. 

Conditions
----------

### Introduction to Conditions

A condition is a statement that specifies when a particular data item or set of data items is applicable.

### Types of Conditions

There are two types of conditions:

* **Simple condition**: A condition with a single statement.
* **Complex condition**: A condition with multiple statements or conditional logic.

### Example Condition

The following is an example of a condition:
```markdown
CONDITION: product = "car"
```
This condition specifies that the data item or set of data items is applicable when the product is a car.

### Creating Custom Conditions

To create a custom condition, follow these steps:

1. **Determine the statement**: Determine which statement will be used to determine the applicability of the data item or set of data items.
2. **Specify the logic**: Specify the logic that will be used to evaluate the statement.
3. **Add conditional logic**: Add conditional logic to the condition to handle complex conditions or exceptions.

### Example Custom Condition

The following is an example of a custom condition:
```markdown
CONDITION: product = "car" AND model = "sedan"
```
This custom condition specifies that the data item or set of data items is applicable when the product is a car and the model is a sedan.

### Condition Markup Elements
The following markup elements can be used to create custom conditions:

* **`<name>`**: Replaced by the name of the property.
* **`<text>`**: Text that is included as-is.
* **`<values>`**: Replaced by the values specified for the property in the applicability assertion.

### Condition Attributes
The following attributes can be used to customize the condition:

* **`ident`**: The ID of the condition type in the CCT.
* **`type`**: The type of the property, either "condition" or "prodattr".
* **`match`**: The value to apply the custom label for.

### Conclusion

Conditions are a powerful tool for specifying when a particular data item or set of data items is applicable. By using simple and complex conditions, custom formatting options, and markup elements, users can create clear and concise displays that meet their specific needs. 

Formatting Options
-----------------

### Introduction to Formatting Options

Formatting options are used to customize the display of applicability.

### Types of Formatting Options

There are several types of formatting options:

* **Text formatting**: Font size, color, and style can be used to highlight important information or make the display more visually appealing.
* **Tables and lists**: Data items can be displayed in tables or lists to make it easier to compare and contrast different values.

### Example Formatting Option

The following is an example of a formatting option:
```markdown
FORMAT: table
COLUMNS: product, model, size
```
This formatting option displays the data items in a table with three columns: product, model, and size.

### Creating Custom Formatting Options

To create a custom formatting option, follow these steps:

1. **Determine the format**: Determine which format will be used to display the data items.
2. **Specify the layout**: Specify the layout of the format, including any tables, lists, or text formatting.
3. **Add conditional logic**: Add conditional logic to the formatting option to handle complex conditions or exceptions.

### Example Custom Formatting Option

The following is an example of a custom formatting option:
```markdown
FORMAT: table
COLUMNS: product, model, size
CONDITION: IF product = "car" THEN size = "small"
```
This custom formatting option displays the data items in a table with three columns: product, model, and size. The condition specifies that if the product is a car, then the size must be small.

### Formatting Option Markup Elements
The following markup elements can be used to create custom formatting options:

* **`<name>`**: Replaced by the name of the property.
* **`<text>`**: Text that is included as-is.
* **`<values>`**: Replaced by the values specified for the property in the applicability assertion.

### Formatting Option Attributes
The following attributes can be used to customize the formatting option:

* **`ident`**: The ID of the condition type in the CCT.
* **`type`**: The type of the property, either "condition" or "prodattr".
* **`match`**: The value to apply the custom label for.

### Conclusion

Formatting options are a powerful tool for customizing the display of applicability. By using text formatting, tables and lists, and custom formatting options, users can create clear and concise displays that meet their specific needs. 

Best Practices
--------------

### Introduction to Best Practices

Best practices are guidelines for creating and displaying applicability.

### Types of Best Practices

There are several types of best practices:

* **Keep it simple**: Avoid using complicated or confusing language in the display rule.
* **Use clear and concise formatting**: Use tables, lists, and other formatting options to make the display easy to read and understand.
* **Test thoroughly**: Test the display rule with different inputs and conditions to ensure that it is working correctly.

### Example Best Practice

The following is an example of a best practice:
```markdown
BEST PRACTICE: Keep it simple
DESCRIPTION: Avoid using complicated or confusing language in the display rule.
```
This best practice recommends keeping the display rule simple and easy to understand.

### Creating Custom Best Practices

To create a custom best practice, follow these steps:

1. **Determine the guideline**: Determine which guideline will be used to create the best practice.
2. **Specify the description**: Specify the description of the best practice, including any examples or explanations.
3. **Add conditional logic**: Add conditional logic to the best practice to handle complex conditions or exceptions.

### Example Custom Best Practice

The following is an example of a custom best practice:
```markdown
BEST PRACTICE: Use clear and concise formatting
DESCRIPTION: Use tables, lists, and other formatting options to make the display easy to read and understand.
CONDITION: IF product = "car" THEN size = "small"
```
This custom best practice recommends using clear and concise formatting in the display rule. The condition specifies that if the product is a car, then the size must be small.

### Best Practice Markup Elements
The following markup elements can be used to create custom best practices:

* **`<name>`**: Replaced by the name of the property.
* **`<text>`**: Text that is included as-is.
* **`<values>`**: Replaced by the values specified for the property in the applicability assertion.

### Best Practice Attributes
The following attributes can be used to customize the best practice:

* **`ident`**: The ID of the condition type in the CCT.
* **`type`**: The type of the property, either "condition" or "prodattr".
* **`match`**: The value to apply the custom label for.

### Conclusion

Best practices are guidelines for creating and displaying applicability. By using simple and clear language, formatting options, and custom best practices, users can create clear and concise displays that meet their specific needs. 

Conclusion
----------

Applicability display is a powerful tool for showing the applicability of data modules or sets of data modules. By using custom display rules, formatting options, and best practices, users can create clear and concise displays that meet their specific needs.

The following are some key takeaways from this guide:

* **Use simple and conditional display rules**: Display rules can be used to determine how the applicability of a data module or set of data modules should be displayed.
* **Format the display**: Formatting options such as text formatting, tables, and lists can be used to make the display easy to read and understand.
* **Test thoroughly**: Test the display rule with different inputs and conditions to ensure that it is working correctly.

By following these guidelines and best practices, users can create effective applicability displays that meet their specific needs.