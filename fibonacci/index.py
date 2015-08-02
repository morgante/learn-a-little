'''
https://www.interviewcake.com/question/nth-fibonacci
'''

def n_fib(n):
    matrix = ((1, 1), (1, ))
    for result in bin(n)[3:]:
        intermediate = matrix[0][0]*matrix[0][0]
        matrix = ((matrix[0][0]*matrix[0][0] + intermediate,
                   (matrix[0][0] + matrix[1][0]) * matrix[0][1]),
                  (matrix[1][0]*matrix[1][0] + intermediate, ))
        if result is '1':
            matrix = ((matrix[0][0] + matrix[0][1], matrix[0][0]), (matrix[0][1], ))
    return matrix[0][1]

for n in range(0, 10):
    print n, n_fib(n)
