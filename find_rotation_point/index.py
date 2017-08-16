'''
https://www.interviewcake.com/question/python/find-rotation-point
'''

def find_rotation_point_recursive(words, first_value=None, front_i=0):
    if first_value is None:
        first_value = words[0]

    pivot_i = int(len(words) / 2)
    pivot = words[pivot_i]
    previous_value = words[pivot_i - 1]

    if previous_value >= pivot:
        return front_i + pivot_i

    if first_value < pivot:
        # We are too far to the front
        return find_rotation_point_recursive(
            words[pivot_i:],
            first_value=first_value,
            front_i=(pivot_i + front_i)
        )

    # We are too far to the end
    return find_rotation_point_recursive(
        words[:pivot_i],
        first_value=first_value,
        front_i=front_i
    )

def find_rotation_point_iterative(words):
    left_bound = 0
    right_bound = len(words) - 1
    first_value = words[0]

    while left_bound < right_bound:
        pivot_i = left_bound + int((right_bound - left_bound) / 2)
        pivot = words[pivot_i]
        previous_value = words[pivot_i - 1]

        if previous_value >= pivot:
            return pivot_i

        if first_value < pivot:
            left_bound = pivot_i
        else:
            right_bound = pivot_i

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
]

print('comapre', find_rotation_point_recursive(words), find_rotation_point_iterative(words), words.index('asymptote'))
