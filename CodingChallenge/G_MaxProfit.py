'''
You are given an array prices where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

{O:7}

'''

# Using divide and conquer to merge sort
def profit(list_prices):
    
    if len(list_prices)==0:
        return 0
    
    min_price=list_prices[0]
    max_profit=0
    for day,price in enumerate(list_prices):
        print(f"day: {day}")
        print(f"price: {price}")

        # No puede haber maximos en el primer dia porque tenemos que comprar para vender

        # Si el precio es menor al precio de ayer entonces min_price es igual al precio de hoy
        min_price=min(price,min_price)
        # Calculate the potential profit
        profit = price-min_price
        # Si el precio es mayor al precio de ayer entonces max_profit es igual al precio de hoy
        max_profit=max(profit,max_profit)   

        print(f"min_price: {min_price}")
        print(f"profit: {profit}")
        print(f"max_profit: {max_profit}")
        print("*********************************")

    return max_profit

# list_prices = [7, 1, 5, 3, 6, 4]
list_prices = [8, 7, 5, 10, 1, 12]
ret = profit(list_prices)
print(f"Response: {ret}")