"""
Dado un array de números enteros nums, mueve todos los ceros al final de la lista mientras mantienes el orden relativo de los elementos no-cero. 
Hazlo en su lugar (sin crear otra lista) y con la menor cantidad de operaciones posible.
"""

def move_zeros(arr):

    virtual_index=0
    for current_index,current_value in enumerate(arr):
        print(arr)
        print(f"current_index: {current_index}")
        print(f"current_value: {current_value}")
        print(f"virtual_index: {virtual_index}")
        
        # Define if not 0 then is a number
        if current_value!=0:
            arr[virtual_index]=current_value
            virtual_index+=1

        print(arr)

        print("****************")
        print("")

    # Fill 0s, in the virtual index is the position where we start pushing the 0 removed until my array len-1
    for pos in range(virtual_index,len(arr)):
        arr[pos] = 0

nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(f"{nums}")