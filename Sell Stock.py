def max_profit(prices):
    min_price = float('inf')   # ab tak ka sabse sasta din
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price          # naya sabse sasta din mila
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit

# Example
print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5 (buy at 1, sell at 6)
print(max_profit([7, 6, 4, 3, 1]))     # Output: 0 (price hamesha gir raha hai)