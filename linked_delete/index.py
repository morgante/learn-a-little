'''
https://www.interviewcake.com/question/delete-node
'''

class Node:
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

def delete_node(node):
    print "deleting" + node.value
    node.value = node.next.value

    try:
        node.value = node.next.value
        node.next = node.next.next
    except:
        raise Exception("cannot delete last node")

a = Node('A')
b = Node('B')
c = Node('C')

a.next = b
b.next = c

print_list(a)

delete_node(b)

print_list(a)
