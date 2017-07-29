'''
Find the sum of all primes less than or equal to n
'''

def get_prime_sum(n):
    numbers = set(range(2, n))
    prime_sum = 0
    while len(numbers) > 0:
        p = numbers.pop()
        prime_sum += p
        q = p
        while q <= n:
            q = q + p
            try:
                numbers.remove(q)
            except KeyError:
                pass
    
    return prime_sum

print('sum', get_prime_sum(10))
# print('sum', get_prime_sum(91919))
