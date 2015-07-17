'''
This problem is around finding the minimum number of moves for moving between two positions on a chess board.

We need to support 3 different kinds of pieces: rooks, bishops, and kings.
The chess board is numbered 0 through 63.
'''
import math

def get_coordinates(number):
    return ((number % 8), math.floor(number / 8))

def count_moves(start, end, piece="bishop"):
    if (piece != "bishop"):
        raise Exception("Cannot handle non-bishop pieces yet")

    start_location = get_coordinates(start)
    end_location = get_coordinates(end)

    horizontal_diff = abs(start_location[0] - end_location[0])
    vertical_diff = abs(start_location[1] - end_location[1])

    if horizontal_diff == vertical_diff:
        return 1
    elif (horizontal_diff % 2) == (vertical_diff % 2):
        return 2
    else:
        return 0


print count_moves(35, 14), 1
print count_moves(45, 46), 0
print count_moves(4, 9), 2
