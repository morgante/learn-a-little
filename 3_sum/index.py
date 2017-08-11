'''
Given a list of numbers and a target N,
return a combination of 3 numbers from the list which sums to N.

This solution is O(n^2)

O(n log n + n*n) = O(n*(log n + n)) = O(n^2)
'''

def get_combination_sum(numbers, n):
    numbers = sorted(numbers)

    for i, num1 in enumerate(numbers[0:-2]):
        left_j = i + 1
        right_k = len(numbers) - 1

        while left_j < right_k:
            num2 = numbers[left_j]
            num3 = numbers[right_k]
            my_sum = num1 + num2 + num3
            if my_sum == n:
                return (num1, num2, num3)
            elif my_sum >= n:
                right_k -= 1
            else:
                left_j += 1

    return None

print('solution', get_combination_sum([2, 5, 9, 11, 17, 3, 9, 88], 19), '5, 11, 3')
