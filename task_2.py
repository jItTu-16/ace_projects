def maximize_profit(prices):
    profit = 0

    l_prices = len(prices)

    for i in range(l_prices):
        for j in range(i + 1, l_prices):
            diff = prices[j] - prices[i]

            profit = max(profit, diff)

    return profit


print(maximize_profit([7, 1, 5, 3, 6, 4]))
print(maximize_profit([7, 6, 4, 3, 1]))
print(maximize_profit([3, 5, 8, 7, 6, 1]))
