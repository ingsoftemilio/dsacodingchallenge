"""
You are given an array prices where prices[i] is the price of a given stock on the i-th day.
Your task is to write a function that calculates the maximum profit you can achieve. 
You may complete as many transactions as you like (buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions simultaneously (you must sell the stock before you buy again).
"""

def max_profit(arr):

    total_profit=0

    # Skip the first day
    for i in range(1,len(arr)):
        # Compare
        if arr[i]>arr[i-1]:
            total_profit+=arr[i]-arr[i-1]

    return total_profit

arr_prices=[7, 1, 5, 3, 6, 4]
print(f"max profit: {max_profit(arr_prices)}")