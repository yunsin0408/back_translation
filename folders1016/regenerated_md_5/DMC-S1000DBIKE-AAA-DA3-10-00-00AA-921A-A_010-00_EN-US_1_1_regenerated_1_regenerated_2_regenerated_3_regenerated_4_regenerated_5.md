# DMC-S1000DBIKE-AAA-DA3-10-00-00AA-921A-A_010-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated_3_regenerated_4_regenerated

xml
<procedure xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd">
## Title

is_palindrome

## Description

### Paragraph

Checks if a string is a palindrome, ignoring case, spaces, and punctuation.

### Arguments

#### Argument

*   **name**: s
*   **description**: The string to check.

### Returns

#### Return

True if the string is a palindrome, False otherwise.

## Step

### Step 1

*   **step_number**: 1
*   **step_text**: import re

### Step 2

*   **step_number**: 2
*   **step_text**: s = s.lower()

### Step 3

*   **step_number**: 3
*   **step_text**: s = re.sub(r'[^a-z0-9]', '', s)  # Remove non-alphanumeric characters

### Step 4

*   **step_number**: 4
*   **step_text**: return s == s[::-1]