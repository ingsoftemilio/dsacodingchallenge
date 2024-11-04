"""
Problem:
Write a function to find the sum of all elements in an array using the Divide and Conquer approach.

Base case: One element of the array is already the max value
Recursive case:
"""

def sum_of_array(arr,low_index,right_index):

    """DIVIDE"""
    # BASE CASE, when theres only one element left
    if low_index==right_index:
        return arr[low_index]

    # SPLIT into 2 halves
    # RECURSIVE TO GET TWO HALVES
    mid_index=(low_index + right_index) // 2
    left_half_sum=sum_of_array(arr,low_index,mid_index)
    right_half_sum=sum_of_array(arr,mid_index+1,right_index)
   
    """CONQUER"""
    # The operation
    return left_half_sum+right_half_sum


arr = [1, 2, 3, 4, 5]
resp = sum_of_array(arr,0,len(arr)-1)
print(f"Sum of arrays: {resp}")