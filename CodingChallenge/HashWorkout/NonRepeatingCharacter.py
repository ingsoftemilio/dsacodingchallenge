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

    # Create dictionary with processed chars
    chars_count_dict={}
    
    # For each character count how many times I found the character 
    for character in my_string:
        # 0 is the default value that get will return if the character key does not exist in the dictionary
        chars_count_dict[character] = chars_count_dict.get(character,0)+1

    # Find the first non-repeating character by checking `my_string` order
    for index,character in enumerate(my_string):
        if chars_count_dict[character]==1:
            return index

    # If no non-repeating character is found, return -1
    return -1

res = nonrepeat_character("abcabcde") #→ Expected: 6 ("d", the first unique character)
print(res)