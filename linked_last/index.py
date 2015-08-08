'''
https://www.interviewcake.com/question/kth-to-last-node-in-singly-linked-list
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class ListLength(Exception):
    pass

def get_kth_to_last_node(k, head):
    processed = 0
    next = head
    last_k = head

    while (next.next is not None):
        next = next.next

        if (processed >= k - 1):
            last_k = last_k.next

        processed += 1

    if (processed < k - 1):
        raise IndexError("k must be less than the list length")

    return last_k

a = Node("Angel Food")
b = Node("Bundt")
c = Node("Cheese")
d = Node("Devil's Food")
e = Node("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print get_kth_to_last_node(2, a).value, "Devil's Food"

print get_kth_to_last_node(0, a).value

print get_kth_to_last_node(5, a).value

print get_kth_to_last_node(6, a).value
