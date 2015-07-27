'''
https://www.interviewcake.com/question/shuffle
'''
import random

def shuffle_in_place(collection):
    for i in range(0, len(collection)):
        value = collection[i]
        swap = random.randint(i, len(collection) - 1)
        collection[i] = collection[swap]
        collection[swap] = value

    return collection


print shuffle_in_place([1, 3, 4, 9, 10])
