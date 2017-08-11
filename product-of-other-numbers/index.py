'''
https://www.interviewcake.com/question/python/product-of-other-numbers

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

Do not use division in your solution.
'''

def get_products_of_other_ints(ints):
    left_product = 1
    right_product = 1
    left_products = [1] * len(ints)
    right_products = [1] * len(ints)
    final_products = [0] * len(ints)

    for i in range(1, len(ints)):
        left_val = ints[i - 1]
        right_val = ints[len(ints) - i]
        print('analysis', left_val, right_val)

        left_product *= left_val
        left_products[i] = left_product

        right_product *= right_val
        right_products[len(ints) - i - 1] = right_product

    for i in range(0, len(ints)):
        final_products[i] = left_products[i] * right_products[i]

    return final_products

print(get_products_of_other_ints([1, 7, 3, 4]), 'should be', [84, 12, 28, 21], 'for', [1, 7, 3, 4])