'''
Find the sum of all primes less than or equal to n
'''

def get_prime_sum(n):
    numbers = set(range(2, n))
    prime_sum = 0
    while len(numbers) > 0:
        p = numbers.pop()
        prime_sum += p
        c = set()
        print('discard', p, set.update(range(2 * p, n + 1, p)))
        numbers.discard(set(range(p, n + 1, p)))
    
    return prime_sum

print('sum', get_prime_sum(10))
# print('sum', get_prime_sum(91919))
