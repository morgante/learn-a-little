'''
https://www.interviewcake.com/question/nth-fibonacci
'''

def n_fib(n):
    last_two = (0, 1)
    if (n in last_two):
        return n
    i = len(last_two)

    while i <= n:
        new_value = sum(last_two)
        last_two = (last_two[1], new_value)
        i += 1

    return last_two[1]

for n in range(0, 10):
    print n, n_fib(n)
