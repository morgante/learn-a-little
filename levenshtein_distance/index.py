'''
Write an efficient algorithm to calculate the minimum number of operations to turn a given string into another string.

Only 3 operation types are allowed:
* Delete character
* Replace a character
* Add character
'''

def count_ops(a, b):
    if a is "":
        return len(b)
    elif b is "":
        return len(a)

    if a[-1] == b[-1]:
        op = 0
    else:
        op = 1

    return min(count_ops(a, b[:-1]) + 1, count_ops(a[:-1], b) + 1, count_ops(a[:-1], b[:-1]) + op)

print count_ops("cb", "ab"), 1
print count_ops("a", "ab"), 1
print count_ops("kitten", "sitting"), 3
