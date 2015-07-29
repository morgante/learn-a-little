import random

def merge_tuples(left, right):
    result = []
    point_left = 0
    point_right = 0

    while point_left < len(left) and point_right < len(right):
        if (left[point_left] <= right[point_right]):
            result.append(left[point_left])
            point_left += 1
        else:
            result.append(right[point_right])
            point_right += 1

    if point_left < len(left):
        result.extend(left[point_left:])

    if point_right < len(right):
        result.extend(right[point_right:])

    return tuple(result)

def merge_sort(items):
    if len(items) <= 1:
        return (items[0], )
    else:
        middle = len(items) / 2
        left = merge_sort(items[:middle])
        right = merge_sort(items[middle:])
        return merge_tuples(left, right)

numbers = [random.randint(0, 100) for x in xrange(0, 25)]
print sorted(numbers)

print merge_sort(numbers)
