'''
You are given an array prices where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

1 <= prices.length <= 10^5 signfica que siempre habra por lo menos un precio y como maximo hasta 100,000 precios almacenados
0 <= prices[i] <= 10^4 signfica que el precio minimo sera 0, y el maximo 10,000 es decir siempre tendremos valores y no habra negativos

'''

def max_profit(arr_prices):

    # Base case
    if len(arr_prices)<=1:
        return 0
    
    min_price = arr_prices[0]
    max_profit = 0

    for i,price in enumerate(arr_prices):
        
        # To get the min price so far, mantain the minimum
        min_price = min(min_price,price)

        # My current price - min price found so far
        profit = price - min_price

        # Compare if the current profit is bigger or lesser than the current max profit
        max_profit = max(max_profit,profit)

    return max_profit

arr_prices=[7, 1, 5, 3, 6, 4]
# arr_prices = [8, 7, 5, 10, 1, 12]
res = max_profit(arr_prices)
print(f"res: {res}")