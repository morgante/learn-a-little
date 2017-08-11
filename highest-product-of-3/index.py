'''
https://www.interviewcake.com/question/highest-product-of-3
'''

from operator import mul

def find_max_product(numbers):
	max_number = max(numbers[0], numbers[1])
	min_number = min(numbers[0], numbers[1])

	max_double = numbers[0] * numbers[1]
	min_double = numbers[0] * numbers[1]

	max_product = numbers[0] * numbers[1] * numbers[2]

	for x in numbers[2:]:
		max_product = max(max_product, max_double * x, min_double * x)

		max_double = max(max_double, x * max_number, x * min_number)
		min_double = min(min_double, x * max_number, x * min_number)

		max_number = max(max_number, x)
		min_number = min(min_number, x)

	return max_product


print find_max_product([1, 3, 4, 8, 2, 3, 4, 9, 11, 15]);
