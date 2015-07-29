'''
Write an efficient algorithm to calculate the minimum number of operations to turn a given string into another string.

Only 3 operation types are allowed:
* Delete character
* Replace a character
* Add character
'''

def count_ops(a, b):
    op_count = 0

    if len(a) < len(b):
        op_count += abs(len(b) - len(a))

    print op_count
    return op_count

assert count_ops("a", "ab") is 1
assert count_ops("kitten", "sitting") is 3
