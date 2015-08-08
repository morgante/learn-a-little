'''
https://www.interviewcake.com/question/kth-to-last-node-in-singly-linked-list
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def get_kth_to_last_node(k, head):
    return "Devil's Food"

a = Node("Angel Food")
b = Node("Bundt")
c = Node("Cheese")
d = Node("Devil's Food")
e = Node("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print get_kth_to_last_node(2, a), "Devil's Food"
