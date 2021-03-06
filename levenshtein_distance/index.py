'''
Write an efficient algorithm to calculate the minimum number of operations to turn a given string into another string.

Only 3 operation types are allowed:
* Delete character
* Replace a character
* Add character
'''

def print_matrix(matrix):
    for row in matrix:
        print row

def count_ops(a, b):
    if len(a) < len(b):
        return count_ops(b, a)

    # create a matrix for our distances
    matrix = []

    # fill in the first row of the matrix
    matrix.append([x for x in range(0, len(b) + 1)])

    for row_number in xrange(1, len(a) + 1):
        row = [matrix[row_number - 1][0] + 1]
        matrix.append(row)

        for col_number in xrange(1, len(b) + 1):
            diagnol = matrix[row_number - 1][col_number - 1]
            left = matrix[row_number][col_number - 1]
            top = matrix[row_number - 1][col_number]
            a_letter = a[row_number - 1]
            b_letter = b[col_number - 1]
            if a_letter == b_letter:
                val = matrix[row_number - 1][col_number - 1]
            else:
                # find shortest path to the current value:
                val = min(
                    diagnol, # substitution
                    left, # insertion
                    top # deletion
                ) + 1
            row.append(val)

    return matrix[len(a) - 1][len(b) - 1]

print count_ops("cb", "ab"), 1
print count_ops("a", "ab"), 1
print count_ops("kitten", "sitting"), 3
