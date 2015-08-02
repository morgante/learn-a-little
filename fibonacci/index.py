'''
https://www.interviewcake.com/question/nth-fibonacci
'''

def n_fib(n):
    if (n == 0):
        return 0
    elif (n <= 2):
        return 1;
    last_two = (1, 1)
    i = 3

    while i <= n:
        new_value = sum(last_two)
        last_two = (last_two[1], new_value)
        i += 1

    return last_two[1]

print n_fib(5)
