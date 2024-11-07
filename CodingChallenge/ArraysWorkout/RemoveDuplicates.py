"""
Exercise: Remove Duplicates from a Sorted Array
Given a sorted array of integers, remove the duplicates in place so that each unique element appears only once. Return the length of the modified array after duplicates are removed. Do not use any extra space for another array; modify the input array directly.

You only need to keep the unique elements at the beginning of the array. It’s okay if the extra elements after the unique ones are not removed, as long as the length returned is correct.

Example
Input: [0, 0, 1, 1, 2, 3, 3]
Output: 4, with the modified array as [0, 1, 2, 3, _, _, _] (where _ represents any value, as these indices are irrelevant)
"""

def remove_duplicates(arr):

    # Only if there are 2 elements or more
    if len(arr)>1:
        track_index=0 # Pointer to place unique elements
        for current_index,current_value in enumerate(arr):
            # Compare with my previous element if I am a duplicate only if I am after the first element
            if current_index>0:
                # Compare to the previous elment
                if current_value!=arr[track_index]:
                    # DUPLICATE
                    # THIS INDEX WORK TO KEEP A TRACK ON THE NEW POSITIONS OF THE ARRAY
                    track_index+=1
                    # ASSIGN THE CURRENT VALUE TO THE MUST UPDATED POSITION
                    arr[track_index]=current_value
                    

        print(track_index)
        # Add the spaces left
        for i in range(track_index+1,len(arr)):
            arr[i] = "_"

    return arr

arr = [0, 0, 1, 1, 2, 3, 3] 
res = remove_duplicates(arr)
print(res)
