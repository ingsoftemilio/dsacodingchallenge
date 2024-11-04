"""
Problem:
You are given an array of integers. Your task is to find the maximum element in this array using the Divide and Conquer approach.

Steps:
Base Case: If the array has only one element, that element is the maximum.
Recursive Case: Divide the array into two halves and recursively find the maximum in each half, then return the larger of the two.

Explanation:
Divide: The array is split into two halves recursively. Each half is divided until the base case of a single element is reached.
Conquer: For each half, we find the maximum element using the recursive function calls.
Combine: After finding the maximum of the two halves, the function compares them and returns the larger one.
"""

import ipdb

def max_number(arr,low_index,high_index,texto):

    ### WE WILL BE USING INDEX TO AVOID GENERATING MORE ARRAYS
    print("")
    print(texto)
    print(f"low_index: {low_index}")
    print(f"high_index: {high_index}")

    # Base case avoid the infinite loop
    if low_index==high_index: #When this is stablished means that is one element left, this is the base case: that element is the maximum.
        return arr[low_index]
    
    """DIVIDE"""
    # Recursive case, slice the array into two halves
    mid_index=(low_index+high_index) // 2
    print(f"mid_index: {mid_index}")
    
    # Recursively find the maximum value in the left half
    left_half_max_value = max_number(arr,low_index,mid_index,"***LEFT HALF VALUE***")
    print(f"left_half_max_value: {left_half_max_value}")
    # Recursively find the maximum value in the righ half
    right_half_max_value = max_number(arr,mid_index+1,high_index,"***RIGHT HALF VALUE***")
    print(f"right_half_max_value: {right_half_max_value}")

    # ipdb.set_trace()  # The program will pause here
    print("*************")

    """CONQUER"""
    # GET THE MAX OF THE TWO VALUES
    return max(left_half_max_value,right_half_max_value)

    

list_data=[3, 9, 1, 7, 4, 8, 2, 5]
result=max_number(list_data,0,len(list_data)-1,"***ARRAY ORIGINAL***")
print("Maximum element is:", result)