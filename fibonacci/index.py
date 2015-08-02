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

def fast_fib(n):
    if n <= 1:
        return n
    if n % 2 is 1:
        half = (n + 1) / 2
        return fast_fib(half)**2 + fast_fib(half - 1)**2
    else:
        half = n / 2
        half_fib = fast_fib(half)
        half_fib_minus_one = fast_fib(half - 1)
        return ((2 * half_fib_minus_one) + half_fib) * half_fib

for n in range(0, 100):
    print n, n_fib(n), fast_fib(n)
    assert n_fib(n) == fast_fib(n)
