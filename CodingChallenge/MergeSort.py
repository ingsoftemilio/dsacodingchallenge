"""
Divide and Conquer is an algorithmic paradigm used to solve complex problems
by recursively breaking them into smaller, simpler subproblems, 
solving these subproblems individually, and then merging or combining 
the solutions to solve the original problem.
"""

"""
SPLIT CASE DIVIDE AND CONQUER
Base case: The recursion stops when the array has only one element (len(arr) <= 1), as a single element is trivially sorted.
Divide: The array is split into two halves using the mid index.
Recursive calls: The function calls itself on both the left_half and right_half of the array to continue splitting and sorting them.
Merge step: After both halves are sorted, the merge() function is called to merge them back into the original array.
"""
def split_array(_array):
    
    # Only half if size > 1, 1 is already trivially sorted
    if len(_array)>1:
    
        """DIVIDE
        You start by splitting the array into two halves. For example, with the array
        """
        # Split the array into halves
        mid_array=len(_array) // 2
        left_half=_array[:mid_array]
        right_half=_array[mid_array:]
        
        """RECURSIVE
        After reaching arrays with a single element, 
        you consider each of these as being trivially sorted. 
        Now the recursive function starts returning from the base case 
        and merges these sorted arrays:
        """
        # Call me to get of both halves
        split_array(left_half)
        split_array(right_half)

        # Merge the 2 sorted halves back into the original array
        """CONQUER -  COMBINE
        Now, the sorted subarrays are merged back together 
        to form the complete sorted array:
        """
        #i, j, and k are initialized to 0. These are pointers that track the current position in the left_half, right_half, and arr respectively:
        i = j = k = 0
        # Compare elements from both halves and merge them in sorted order
        # This loop compares and merges elements from the two subarrays only while both subarrays still have elements to compare.
        while i<len(left_half) and j<len(right_half):
            # If element on the left array is smaller than right element, then save the left current value into the original array
            if left_half[i] < right_half[j]:
                _array[k] = left_half[i]
                #Advance one value
                i+=1
            else: #Left is bigger so I assign the right value into the original array
                _array[k] = right_half[j]
                j+=1

            #Adance the position of the original array
            k+=1

        # The remaining left elements
        while i<len(left_half):
            _array[k] = left_half[i]
            #Advance one value
            i+=1
            #Adance the position of the original array
            k+=1

                # The remaining right elements
        while j<len(right_half):
            _array[k] = right_half[j]
            #Advance one value
            j+=1
            #Adance the position of the original array
            k+=1


# List to be sorted
list_values=[38, 27, 43, 3, 82, 10]
# list_values=[38, 27]
# Divide conquer and combine to get the merged sort
split_array(list_values)

print(list_values)
