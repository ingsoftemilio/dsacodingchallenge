"""Problem Statement
Write a function that checks if a string of parentheses is balanced. A string is considered balanced if:

Every opening parenthesis ( has a corresponding closing parenthesis ).
Parentheses close in the correct order."""

def is_balanced_parentheses(string):
    list_of_opening_parenthesis=[]
    # Iterate trough the array
    for ch in string:
        # Check if its an opening parenthesis
        if ch=='(':
            list_of_opening_parenthesis.append(ch)
        # Check if its a closing parenthesis and I have an opener
        if len(list_of_opening_parenthesis)>0 and ch==')':
            list_of_opening_parenthesis.pop()

    # If the parenthesis are balanced, it means I dont have any closing parenthesis, then return true
    return len(list_of_opening_parenthesis)==0

assert is_balanced_parentheses("()") == True  # Balanced
assert is_balanced_parentheses("(())") == True  # Balanced
assert is_balanced_parentheses("(()") == False  # Unbalanced
assert is_balanced_parentheses(")(") == False  # Unbalanced
assert is_balanced_parentheses("") == True  # Balanced (empty string)
assert is_balanced_parentheses("((a+b)*c)") == True  # Balanced with other characters
assert is_balanced_parentheses("())(()") == False  # Unbalanced