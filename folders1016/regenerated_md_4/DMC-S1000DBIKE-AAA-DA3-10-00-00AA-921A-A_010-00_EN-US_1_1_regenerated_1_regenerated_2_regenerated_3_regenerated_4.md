# DMC-S1000DBIKE-AAA-DA3-10-00-00AA-921A-A_010-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated_3_regenerated

xml
<procedure xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd">
## Title
is_palindrome

## Description

### Paragraph
Checks if a string is a palindrome, ignoring case, spaces, and punctuation.

### Arguments

#### Argument
*   **Name:** s
*   **Description:** The string to check.

### Returns

#### Return
True if the string is a palindrome, False otherwise.

## Step

### Step
*   **Step_number:** 1
*   **Step_text:** import re

## Step

### Step
*   **Step_number:** 2
*   **Step_text:** s = s.lower()

## Step

### Step
*   **Step_number:** 3
*   **Step_text:** s = re.sub(r'[^a-z0-9]', '', s)  # Remove non-alphanumeric characters

## Step

### Step
*   **Step_number:** 4
*   **Step_text:** return s == s[::-1]