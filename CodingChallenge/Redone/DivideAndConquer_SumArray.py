"""
Problem:
Write a function to find the sum of all elements in an array using the Divide and Conquer approach.

Base case: One element of the array is already the max value
Recursive case:
"""

def sum_array(arr,lowest_index,highest_index):

    #BASE CASE, WHEN THERES ONLY ONE VALUE THATS THE SUM OF 1 VALUE
    if lowest_index==highest_index:
        return arr[lowest_index]

    """DIVIDE"""
    mid_index=(lowest_index+highest_index) // 2
    # print(f"mid_index {mid_index}")

    #Recursive
    left_sum_value=sum_array(arr,lowest_index,mid_index)
    right_sum_value=sum_array(arr,mid_index+1,highest_index)

    """CONQUER"""
    # Sum values
    return left_sum_value+right_sum_value

arr = [7, -2, 5, 3, -9, 1, 6]
retu=sum_array(arr,0,len(arr)-1)
print(f"retu: {retu}")