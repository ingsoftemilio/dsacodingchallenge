"""Problem Description: Write a Python function that determines whether two strings are anagrams. However, before comparing:

Remove all lowercase characters from both strings.
Ignore spaces and punctuation.
Treat uppercase and lowercase letters as the same (case-insensitive).
Constraints:

Only uppercase letters should be considered when checking for anagrams.
The function should return True if the strings are anagrams after applying the above transformations, and False otherwise."""

def is_anagram(s1,s2):
    # Remove all lowercase characters from both strings
    s1aux=(char for char in s1 if char.isupper())
    # Sort the words
    s1aux=sorted(s1aux)
    # Join the arrays of chars
    s1aux="".join(s1aux)
    
    # In one line for s2aux
    s2aux = "".join(sorted(char for char in s2 if char.isupper()))

    print(s1aux)
    print(s2aux)

    # Compare
    return s1aux==s2aux

    
# Example Test Cases
# Example 1
s1 = "Tom Marvolo Riddle"
s2 = "I am Lord Voldemort"
print(is_anagram(s1, s2))  # Output: True

# Example 2
s1 = "Hello"
s2 = "Olelh!!"
print(is_anagram(s1, s2))  # Output: False

# Example 3
s1 = "ABCDE"
s2 = "EDCBA"
print(is_anagram(s1, s2))  # Output: True

# Example 4
s1 = "!@#$%^"
s2 = "!@#$%^"
print(is_anagram(s1, s2))  # Output: True

# Example 5
s1 = "Tom"
s2 = "Not"
print(is_anagram(s1, s2))  # Output: False