"""
Challenge: Find the First Non-Repeating Character
Given a string, find the first character that does not repeat and return its index. If all characters repeat, return -1. This is a common interview problem and a good way to practice counting and lookups with dictionaries.

Example
Input: "swiss"
Output: 0 (The first non-repeating character is 's' at index 0)

Input: "aabbcc"
Output: -1 (All characters repeat)
"""

def nonrepeat_character(my_string):

    # Create dictionary with already processed chars
    processed_chars_dict={}

    for index,character in enumerate(my_string):
        print(index)
        print(character)

    # If none in processed_chars_dict then I couldt find a non repeated value
    if len(processed_chars_dict)==0:
        return -1
    else:
        return processed_chars_dict

res = nonrepeat_character("swiss")
print(res)