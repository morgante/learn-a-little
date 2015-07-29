'''
Write an efficient algorithm to calculate the minimum number of operations to turn a given string into another string.

Only 3 operation types are allowed:
* Delete character
* Replace a character
* Add character
'''

def count_ops(a, b):
    # create a matrix for our distances
    matrix = []

    # fill in the first row of the matrix
    matrix.append([x for x in range(0, len(b))])

    for row_number in xrange(1, len(a)):
        row = [matrix[row_number - 1][0] + 1]
        matrix.append(row)

        for col_number in xrange(1, len(b)):
            top = matrix[row_number - 1][col_number]
            left = row[col_number - 1]

            row.append(min(top, left) + 1)

    print matrix

    return 1

# print count_ops("cb", "ab"), 1
# print count_ops("a", "ab"), 1
print count_ops("kitten", "sitting"), 3
