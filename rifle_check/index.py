'''
https://www.interviewcake.com/question/single-rifle-check
'''
import random

def is_rifle_shuffled(shuffled_deck, half1, half2):
    """checks of a deck was shuffled using the random method"""
    # copy our halves, to avoid side effects
    first_pointer = 0
    second_pointer = 0
    for x in shuffled_deck:
        if first_pointer < len(half1) and half1[first_pointer] is x:
            first_pointer += 1
            continue
        elif second_pointer < len(half2) and half2[second_pointer] is x:
            second_pointer += 1
            continue
        else:
            return False

    return True

def random_split(deck):
    """splits a deck into two random halfs"""
    # split deck into two halves
    length = len(deck)
    half1 = deck[:length/2]
    half2 = deck[length/2:]

    # shuffle each half randomly
    random.shuffle(half1)
    random.shuffle(half2)

    return (deck, half1, half2)


def random_pop(stack):
    """pops a random number of elements off the front of a list"""
    number = random.randint(0, len(stack))
    additions = stack[:number]
    left = stack[number:]

    del stack[:number]

    return additions

def rifle_shuffle(deck):
    """rifle shuffles a deck, returning the halfs and the deck"""
    deck, half1, half2 = random_split(deck)

    # start building our results
    shuffled_deck = []
    response = (shuffled_deck, list(half1), list(half2))

    while len(half1) > 0:
        shuffled_deck.extend(random_pop(half1))
        shuffled_deck.extend(random_pop(half2))

    shuffled_deck.extend(half2)

    return response

def random_shuffle(deck):
    """randomly shuffles a deck"""
    deck, half1, half2 = random_split(deck)

    random.shuffle(deck)

    return (deck, half1, half2)

deck = rifle_shuffle(range(1, 53))
print is_rifle_shuffled(deck[0], deck[1], deck[2])

deck2 = random_shuffle(range(1, 53))
print is_rifle_shuffled(deck2[0], deck2[1], deck2[2])
