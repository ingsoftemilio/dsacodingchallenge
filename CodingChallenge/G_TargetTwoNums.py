# You are given an array of integers and a target number. Your goal is to find two numbers in the array that add up to the target 
# and return their indices. Each input will have exactly one solution, and you cannot use the same element twice.

def two_num(arr_nums,target):
    my_hash_map={}
    print(f"target: {target}")
    for index,num in enumerate(arr_nums):      
        dif = target-num # For example, 9 - 2 = 7

        print(f"index in course: {index}")
        print(f"num in course: {num}")
        print(f"dif num in course with target: {dif}")

        # If the difference in HashMap then that means I have to return my index and the index of the found value
        if dif in my_hash_map:
            arr_return = []
            arr_return.append(my_hash_map[dif]) # The dif number in the HashMap
            arr_return.append(index) # The current number index
            return arr_return
        else:
            # Push current element into 
            my_hash_map[num] = index
        
        print("***************************")

print(f"{two_num([2,7,11,15],9)}")