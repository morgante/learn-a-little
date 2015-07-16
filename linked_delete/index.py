'''
https://www.interviewcake.com/question/delete-node
'''

class Node:
    def __init__(self, value):
        self.value = value

        if (self.value != None):
            self.next = Node(None)

def print_list(head):
    print "printing list!"

    node = head
    print node.value
    while (node.next.value != None):
        node = node.next
        print node.value

def delete_node(node):
    print "deleting" + node.value
    node.value = node.next.value

    try:
        node.value = node.next.value
        node.next = node.next.next
    except:
        node.value = None
        # raise Exception("cannot delete last node")

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

print_list(a)

delete_node(b)

print_list(a)

delete_node(d)

print_list(a)
