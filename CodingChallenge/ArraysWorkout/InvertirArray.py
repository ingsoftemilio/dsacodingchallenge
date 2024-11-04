"""
1. Reverse Elementos de un Array a la Izquierda o Derecha
"""

def reverse_slicing(arr):
    return arr[::-1]

def reverse_loop(arr):

    pos_inverted = len(arr)-1 #Starting from 5 and decrease  
    aux_arr=arr[::] # Copy the array or I will be working on the same array thats the [::] for
    for i in range(0,len(arr)):
        aux_arr[i] = arr[pos_inverted] 
        # print(pos_inverted)
        pos_inverted-=1

    return aux_arr

arr = [1, 2, 3, 4, 5]
arr = reverse_loop(arr)
print(f"arr: {arr}")
arr = reverse_slicing(arr)
print(f"arr: {arr}")