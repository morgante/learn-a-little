'''
https://www.interviewcake.com/question/python/find-rotation-point
'''

def find_rotation_point(words, first_value=None, front_i=0):
    if first_value is None:
        first_value = words[0]

    pivot_i = int(len(words) / 2)
    pivot = words[pivot_i]
    previous_value = words[pivot_i - 1]

    print('compare', pivot, first_value, previous_value)

    if previous_value >= pivot:
        return front_i + pivot_i

    if first_value < pivot:
        # We are too far to the front
        return find_rotation_point(
            words[pivot_i:],
            first_value=first_value,
            front_i=(pivot_i + front_i)
        )

    # We are too far to the end
    return find_rotation_point(
        words[:pivot_i],
        first_value=first_value,
        front_i=front_i
    )

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

print('comapre', find_rotation_point(words), words.index('asymptote'))
