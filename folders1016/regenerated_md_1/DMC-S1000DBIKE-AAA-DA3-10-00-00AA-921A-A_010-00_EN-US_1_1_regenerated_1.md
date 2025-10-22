def is_palindrome(s):
  """
  Checks if a string is a palindrome, ignoring case, spaces, and punctuation.

  Args:
    s: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  import re
  s = s.lower()
  s = re.sub(r'[^a-z0-9]', '', s)  # Remove non-alphanumeric characters
  return s == s[::-1]