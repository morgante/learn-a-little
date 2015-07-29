'''
Write an efficient algorithm to calculate the minimum number of operations to turn a given string into another string.

Only 3 operation types are allowed:
* Delete character
* Replace a character
* Add character
'''

def count_ops(a, b):
    return 2

assert count_ops("a", "ab") is 2
assert count_ops("kitten", "sitting") is 3
