"""
Challenge: Two Sum
Given an array of integers and a target sum, find the indices of the two numbers in the array that add up to the target. You can assume that each input will have exactly one solution, and you cannot use the same element twice.

This problem is commonly seen in interviews and is a great way to practice using dictionaries to solve problems efficiently.

Example
Input:
nums = [2, 7, 11, 15]
target = 9
Output: [0, 1]
"""

def two_sum(arr_nums,target):
    container_differences_dict={}

    for index,num_current in enumerate(arr_nums):


        print(f"index: {index}")
        print(f"num_current: {num_current}")

        # GET DIFFERENCE TARGET FROM MY CURRENT VALUE
        difference = target-num_current
        print(f"difference: {difference}")

        # If the difference is in my dictionary, return the index where the difference exists and return my current index
        if num_current in container_differences_dict:
            print(f"the current number {num_current} is found in my dictionary of differences")
            return [container_differences_dict[num_current],index]

        # KEEP A TRACK OF THE DIFFERENCES AND ITS INDEX
        container_differences_dict[difference]=index

        print(container_differences_dict)
        print("")

target=22
arr_nums = [2, 7, 11, 15]    
res = two_sum(arr_nums,target)
print("***")
print(res)