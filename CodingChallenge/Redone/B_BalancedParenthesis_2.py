"""Problem 2: Valid Parentheses
Problem Statement
Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

A string is considered valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order."""


def is_valid(string):

    left_parenthesis=[]
    # Traverse the string and get every character
    for ch in string:
        # Keep track of the left parethesis
        if ch == "(":
            left_parenthesis.append(ch)
        elif ch == ")": 
            if len(left_parenthesis)>0:
            # Validate if its right parenthesis, then pop array tracks left parenthesis, only if the size of my array is >0 
                left_parenthesis.pop()
            else:
                return False


    # If the size of my array is 0 is valid
    print(left_parenthesis)

    # If I dont have any parenthesis left return true, else false
    return len(left_parenthesis)==0

assert is_valid("()") == True  # Balanced
assert is_valid("(())") == True  # Balanced
assert is_valid("(()") == False  # Unbalanced
assert is_valid(")(") == False  # Unbalanced
assert is_valid("") == True  # Balanced (empty string)
assert is_valid("((a+b)*c)") == True  # Balanced with other characters
assert is_valid("())(()") == False  # Unbalanced