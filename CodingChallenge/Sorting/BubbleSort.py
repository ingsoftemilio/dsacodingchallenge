
def bubble_sort_asc(nums: list[int]) -> list[int]:

    n = len(nums)-1 # If I dont sustract 1, then range will count the last value

    # Multiple passes, execpt for the last one, the last one is already sorted
    # in a previous
    for i in range(n):
        print(f"i: {i}")
        print(f"val: {nums[i]}")
        is_swap=False
        # Second loop for adjacent swaps, except current
        for j in range(n-i):
            print(f"Comparing {nums[j]} and {nums[j+1]}")
            # Swap if current element is larger than next element
            if nums[j] > nums[j+1]:
                # SWAP!
                print("SWAP!")
                # temp:int = nums[j]
                # nums[j] = nums[j + 1]
                # nums[j + 1] = temp

                nums[j], nums[j + 1] = nums[j + 1], nums[j] # Not necessary multiple lines, because Pythonic uses the element to the right as a tuple
                is_swap = True
        
        if not is_swap:
            break

        print("*******")

my_list = [7,4,5,3,1,8,2,6]
bubble_sort_asc(my_list)
print(my_list)