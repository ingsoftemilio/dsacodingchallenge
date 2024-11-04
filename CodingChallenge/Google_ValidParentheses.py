'''Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:
Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true
'''

def valid_string(input_string):

    hash_map_valids={"(":")","{":"}","[":"]"}
    stack_closer_brackets=[]

    # Traverse each element of my string
    for char_to_validate in (input_string):

        print(f"char_to_validate: {char_to_validate}")
        # Validate if its a key value in the HashMap
        if char_to_validate in hash_map_valids:
            print(f"char_to_validate is a key so its an opener")
            # Add its closer into the stack, that means its waiting for its bracket to have a finish
            stack_closer_brackets.append(hash_map_valids[char_to_validate])

        else:
            print(f"char_to_validate is not a key so it could be a closer or another bracket")

            # If my current char to validate is == the last insert inserted list of closing brackets that means its the closer I am looking for so I keep it true, if not then error
            # Pop remove and return the last element of my array
            # In this approach I clusterd the two wrong possible scenarios
            if len(stack_closer_brackets)==0 or char_to_validate != stack_closer_brackets.pop():
                return False

        print("***********************")

    # There are no brackets to process
    return len(stack_closer_brackets)==0

input_string = '([])'
print(f"{input_string} is valid: {valid_string(input_string)}")
