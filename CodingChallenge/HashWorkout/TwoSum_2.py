"""Two Sum

Problem Statement
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target."""

def two_sum(arr_int):
    # Traverse trough the array
    diff_hash_map={}
    for index,num in enumerate(arr_int):

        # Get the difference between the target and current value
        diff = target-num

        # Find if the num is in hashmap, if it is then we have found my pair, if not store the difference
        if num in diff_hash_map:
            return [diff_hash_map[num],index]
        else:
            # Store the num and its index in my hashmap
            diff_hash_map[diff] = index


arr_int = [3,1,4,5,2]
0,1,2,3,4
target = 7


assert two_sum(arr_int)==[0,2] # True
print(two_sum(arr_int))