'''
https://www.interviewcake.com/question/python/product-of-other-numbers

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

Do not use division in your solution.
'''

'''
Solution analysis:

time complexity: O(n)
space complexity: O(n)
'''

def get_products_of_other_ints(ints):
    left_product = 1
    final_products = [1] * len(ints)

    for i in range(1, len(ints)):
        left_product *= ints[i - 1]
        final_products[i] = left_product

    right_product = 1
    for j in range(0, len(ints)):
        right_index = len(ints) - j - 1
        final_products[right_index] *= right_product
        right_product *= ints[right_index]

    return final_products

print(get_products_of_other_ints([1, 7, 3, 4]), 'should be', [84, 12, 28, 21], 'for', [1, 7, 3, 4])
print(get_products_of_other_ints([2, 0, 2]))
