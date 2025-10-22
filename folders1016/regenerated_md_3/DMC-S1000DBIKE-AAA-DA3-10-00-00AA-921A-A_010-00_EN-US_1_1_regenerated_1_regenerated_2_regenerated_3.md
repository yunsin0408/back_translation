# DMC-S1000DBIKE-AAA-DA3-10-00-00AA-921A-A_010-00_EN-US_1_1_regenerated_1_regenerated_2_regenerated

xml
<procedure xmlns:dc="http://www.purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd">
  <title>is_palindrome</title>
  <description>
    <paragraph>Checks if a string is a palindrome, ignoring case, spaces, and punctuation.</paragraph>
    <arguments>
      <argument>
        <name>s</name>
        <description>The string to check.</description>
      </argument>
    </arguments>
    <returns>
      <return>True if the string is a palindrome, False otherwise.</return>
    </returns>
  </description>
  <step>
    <step_number>1</step_number>
    <step_text>import re</step_text>
  </step>
  <step>
    <step_number>2</step_number>
    <step_text>s = s.lower()</step_text>
  </step>
  <step>
    <step_number>3</step_number>
    <step_text>s = re.sub(r'[^a-z0-9]', '', s)  # Remove non-alphanumeric characters</step_text>
  </step>
  <step>
    <step_number>4</step_number>
    <step_text>return s == s[::-1]</step_text>
  </step>
</procedure>