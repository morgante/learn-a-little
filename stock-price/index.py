'''
https://www.interviewcake.com/question/python/stock-price
'''


def get_max_profit(prices):
    previous_min = prices[0]
    max_profit = prices[1] - prices[0]

    for price in prices[1:]:
        current_profit = price - previous_min
        if current_profit > max_profit:
            max_profit = current_profit

        if price < previous_min:
            previous_min = price

    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices_yesterday), 6)

print(get_max_profit([11, 9]), -2)

print(get_max_profit([3, 10, 4, 19, 1]), 16)

print(get_max_profit([2, 2, 2]), 0)


print(get_max_profit([10, 4, 3]), -1)
