import ipdb;

"""
Fibonacci Sequence Code Challenge:
Problem: Write a function that returns the Fibonacci sequence up to the nth term, where n is an integer provided by the user.
n = number of elements in the list returned
"""

def fibonacci(n) -> list:
    
    list_sumatoria = []
    for i in range(0,n):
        # print(f"i: {i}")

        # Fibonacci starts when it hits the first 2 elements and forwards, 3 element of the sequence starting from = 2, if not the first 2 elements are part of the list
        if i<2:
            # Append the first elemtns
            list_sumatoria.append(i)
        else: # Starting 2 is when we can start adding the previous 2 elements
            # print(list_sumatoria)
            sumatory=list_sumatoria[i-1]+list_sumatoria[i-2]           
            list_sumatoria.append(sumatory)

    return list_sumatoria

n = 1
res = fibonacci(n)
print(f"{res}")