"""Problem Statement
Write a function that checks if a string of parentheses is balanced. A string is considered balanced if:

Every opening parenthesis ( has a corresponding closing parenthesis ).
Parentheses close in the correct order."""

def is_balanced_parentheses(str):
    # print(str)
    list_openers_to_findpair=[]
    for char in str:
        if char=="(":
            list_openers_to_findpair.append(char)

        if len(list_openers_to_findpair)>0 and char==")":
            # Since I am a closer then I have to pop one of the list openers to find a pair, since I found one closers
            list_openers_to_findpair.pop()

    # IF MY LIST OF OPENERS DOESNT HAVE ANY REMAINING THEN IT WAS BALANCED
    return len(list_openers_to_findpair)==0


assert is_balanced_parentheses("()") == True  # Balanced
assert is_balanced_parentheses("(())") == True  # Balanced
assert is_balanced_parentheses("(()") == False  # Unbalanced
assert is_balanced_parentheses(")(") == False  # Unbalanced
assert is_balanced_parentheses("") == True  # Balanced (empty string)
assert is_balanced_parentheses("((a+b)*c)") == True  # Balanced with other characters
assert is_balanced_parentheses("())(()") == False  # Unbalanced