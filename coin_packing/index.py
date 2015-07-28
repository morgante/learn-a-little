'''
https://www.interviewcake.com/question/coin
'''

def count_ways(amount, coins):
    countages = [0] * (amount + 1)
    countages[0] = 1

    for coin in coins:
        for new_amount in range(coin, amount + 1):
            amount_left = new_amount - coin
            countages[new_amount] += countages[amount_left]

    return countages[amount]

print count_ways(4, (1, 2, 3))
