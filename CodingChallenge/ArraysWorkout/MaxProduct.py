"""
Find the Maximum Product of Two Elements in an Array
Given an integer array, find the maximum product of any two elements.

Example: For [3, 4, 5, 2], the maximum product is 20 (4 * 5).
"""

def max_product(arr):

    # base case
    if len(arr)<=1:
        return 0
    
    max1 = 0
    max2 = 0

    # Traverse trough the array
    for current_value in arr:

        if current_value > max1:
            # Assign the previous max value to max2
            max2=max1
            # Assign the new max value found to max1
            max1=current_value
        elif current_value > max2: # In case is not enough big for max1 then I have to compare it to max2
            max2=current_value


    

    print(f"max1: {max1}")
    print(f"max2: {max2}")

    # Return the product of the 2 found values
    return max1*max2


arr = [3, 4, 5, 2]
res = max_product(arr)
print(res)