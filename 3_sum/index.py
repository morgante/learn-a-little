'''
Given a list of numbers and a target N,
return a combination of 3 numbers from the list which sums to N.
'''

def get_combination_sum(numbers, n):
    num_tracker = [[] for x in range(0, n)]

    for number in numbers:
        try:
            num_tracker[number].append(number)
        except IndexError:
            pass

    for num1 in numbers:
        for num2 in numbers:
            primitive_sum = num1 + num2
            num3 = n - primitive_sum
            count_search = [num1, num2].count(num3) + 1
            try:
                if len(num_tracker[num3]) >= count_search:
                    return (num1, num2, num3)
            except IndexError:
                break

    print('sum_counter', sum_counter)

print('solution', get_combination_sum([2, 5, 9, 11, 17, 3, 9, 88], 19), '5, 11, 3')
