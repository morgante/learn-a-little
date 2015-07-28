'''
https://www.interviewcake.com/question/coin
'''

def count_ways(amount, denominations):
    if amount is 0:
        return 1
    elif amount < 0:
        return 0
    elif len(denominations) is 0:
        return 0

    print "checking it", amount, denominations

    coin = denominations[0]
    count = 0

    while amount >= 0:
        count += count_ways(amount, denominations[1:])
        amount -= coin

    return count

print count_ways(4, (1, 2, 3))
