'''
https://www.interviewcake.com/question/python/find-in-ordered-set
'''

def does_contain_value(needle, haystack):
    if len(haystack) <= 0:
        return False

    pivot_i = int(len(haystack) / 2)
    pivot = haystack[pivot_i]

    if needle == pivot:
        return True

    if needle < pivot:
        return does_contain_value(needle, haystack[:pivot_i])
    else:
        return does_contain_value(needle, haystack[(pivot_i + 1):])

my_haystack = [3, 9, 11, 30, 99, 103, 108, 200, 3000, 3302]

print("assert true", does_contain_value(11, my_haystack))
print("assert true", does_contain_value(103, my_haystack))
print("assert false", does_contain_value(13, my_haystack))
