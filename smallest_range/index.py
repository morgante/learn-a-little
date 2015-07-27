'''
http://www.careercup.com/question?id=16759664

Find the smallest range which includes at least one number from each sorted list

'''

def range_length(range):
    return range[1] - range[0]

def smallest_sample(lists):
    pointers = [0] * 3
    min_range = None

    while True:
        values = [lists[i][j] for i, j in enumerate(pointers)]
        new_range = (min(values), max(values))
        if (min_range is None or range_length(new_range) < range_length(min_range)):
            min_range = new_range
        min_list = values.index(new_range[0])
        pointers[min_list] += 1

        if (pointers[min_list] >= len(lists[min_list])):
            break

    return min_range

print smallest_sample([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])
