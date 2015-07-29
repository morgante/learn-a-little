import random

def merge_sort(items):
    items.sort()
    return items

print merge_sort([random.randint(0, 100) for x in xrange(0, 25)])
