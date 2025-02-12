"""Problem Description:
Write a Python function to check if two strings are valid anagrams under the following rules:

Ignore all spaces, punctuation, and special characters.
Treat uppercase and lowercase letters as the same (case-insensitive).
Numbers and other symbols (e.g., !@#$) are ignored.
Only consider alphabetic characters (A-Z or a-z)."""

# Lower case or upper case the string

def is_anagram(s1,s2):

    # For string one
    s1aux=[]
    for ch1 in s1:
        # if char is Alpha
        if ch1.isalpha():
            s1aux.append(ch1.lower())
    # Sort and join
    s1aux = "".join(sorted(s1aux))
    # print(s1aux)
    
    #For string two, a different approach
    s2aux="".join(sorted(ch2.lower() for ch2 in s2 if ch2.isalpha()))
    # print(s2aux)

    return s1aux==s2aux
    
assert is_anagram("Tom*.", "Mot")==True  # Output: True
assert is_anagram("Listen!", "Silent") == True  # True
assert is_anagram("Hello", "Olelh!!") == True  # True
assert is_anagram("Anagram", "Nagaram") == True  # True
assert is_anagram("Test", "Best") == False  # False
assert is_anagram("A1B2C3", "CBA") == True  # True (numbers ignored)
assert is_anagram("", "") == True  # True (both empty)
assert is_anagram("a", "A") == True  # True (case-insensitive)   