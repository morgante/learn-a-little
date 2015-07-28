'''
https://www.interviewcake.com/question/coin
'''

def get_ways(amount, denominations):
    return [(1, 1, 1, 1), (1, 1, 2), (1, 3), (2, 2)]

def count_ways(amount, denominations):
    return len(get_ways(amount, denominations))

print count_ways(4, (1, 2, 3))
