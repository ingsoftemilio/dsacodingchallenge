"""
Rotar Elementos de un Array a la Izquierda o Derecha
Ejercicio: Dado un array, rota sus elementos una posición a la izquierda o a la derecha

Ejemplo Izquierda: [1, 2, 3, 4, 5] → [2, 3, 4, 5, 1]
Ejemplo Derecha: [1, 2, 3, 4, 5] → [5, 1, 2, 3, 4]
"""

def rotar_array(arr,type="left"):
    print(arr)
    if len(arr)>0:
        if type=="left":
            # Get first value to set it to the last index of the array
            first_value = arr[0]
            for i,value in enumerate(arr):
                # First element wont do anyhting
                if i==0:
                    continue

                # To the previous index I will assign the cur value so it will be move one position left
                arr[i-1]=value

            # Last element add the first value
            arr[len(arr)-1] = first_value
        
        if type=="right":
            last_value = arr[-1]
            previous_value=None
            for i,value in enumerate(arr):
                previous_value = value
                # First element wont do anything
                if i==0:
                    continue
                # Assign the previous value to the current index
                arr[i] = arr[i-1]

            # First element assign the last value
            arr[0] = last_value
    
    print(arr)

arr = [1, 2, 3, 4, 5]
rotar_array(arr,"right")
# print(arr)