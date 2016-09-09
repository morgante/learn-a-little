'''
https://www.interviewcake.com/question/python/reverse-linked-list
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    print "printing list!"

    node = head
    print node.value
    while (node.next != None):
        node = node.next
        print node.value

def reverse_linked_list(head):
    node = head
    previous_node = None

    while node != None:
        next_node = node.next

        node.next = previous_node
        previous_node = node

        node = next_node

    return previous_node

a = Node("Angel Food")
b = Node("Bundt")
c = Node("Cheese")
d = Node("Devil's Food")
e = Node("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print("Original:")
print_list(a)

print("Reversed:")
reversed_list = reverse_linked_list(a)
print_list(reversed_list)

print("Null:")
print(reverse_linked_list(None))
