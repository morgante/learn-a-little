'''
https://www.interviewcake.com/question/single-rifle-check
'''
import random

def is_rifle_shuffled(shuffled_deck, half1, half2):
    return True

def random_pop(stack):
    """pops a random number of elements off the front of a list"""
    number = random.randint(0, len(stack))
    additions = stack[:number]
    left = stack[number:]

    del stack[:number]

    return additions

def rifle_shuffle(deck):
    """rifle shuffles a deck, returning the halfs and the deck"""
    # split deck into two halves
    length = len(deck)
    half1 = deck[:length/2]
    half2 = deck[length/2:]

    # shuffle each half randomly
    random.shuffle(half1)
    random.shuffle(half2)

    # start building our results
    shuffled_deck = []
    response = (shuffled_deck, list(half1), list(half2))

    while len(half1) > 0:
        shuffled_deck.extend(random_pop(half1))
        shuffled_deck.extend(random_pop(half2))

    shuffled_deck.extend(half2)

    return response

deck = rifle_shuffle(range(1, 53))
print is_rifle_shuffled(deck[0], deck[1], deck[2])
