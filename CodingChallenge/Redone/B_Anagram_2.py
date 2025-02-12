"""Problem Description:
Write a Python function to check if two strings are valid anagrams under the following rules:

Ignore all spaces, punctuation, and special characters.
Treat uppercase and lowercase letters as the same (case-insensitive).
Numbers and other symbols (e.g., !@#$) are ignored.
Only consider alphabetic characters (A-Z or a-z)."""



def is_anagram(s1,s2):

    def clean_string(string):
        # Ignore all special characters # Treat them case insensitive
        # Clean the string character by character

        str_aux=""
        for ch in string:
            if ch.isalpha():
                str_aux+=""+ch.lower()

        # Order the string
        str_aux = sorted(str_aux)

        # Join the string
        str_aux = "".join(str_aux)

        return str_aux

    s1 = clean_string(s1)
    s2 = clean_string(s2)
    return s1==s2       


assert is_anagram("Tom*.", "Mot")==True  # Output: True
assert is_anagram("Listen!", "Silent") == True  # True
assert is_anagram("Hello", "Olelh!!") == True  # True
assert is_anagram("Anagram", "Nagaram") == True  # True
assert is_anagram("Test", "Best") == False  # False
assert is_anagram("A1B2C3", "CBA") == True  # True (numbers ignored)
assert is_anagram("", "") == True  # True (both empty)
assert is_anagram("a", "A") == True  # True (case-insensitive)      