import string

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        new_node = Node(value)

        tail_node = self
        while (tail_node.next != None):
            tail_node = tail_node.next

        tail_node.next = new_node

def print_list(head):
    node = head
    list_value = [node.value]
    while (node.next != None):
        node = node.next
        list_value.append(node.value)
    print(list_value)

def delete_k(head, k):
    print("deleting the {}th last node".format(k))

    n_ago = 0
    node = head
    n_ago_node = node
    while (node.next != None):
        if n_ago < k:
            n_ago += 1
        else:
            n_ago_node = n_ago_node.next
        node = node.next


    next_node = n_ago_node.next.next
    n_ago_node.next = next_node


items = list(string.ascii_lowercase)
my_list = Node(items[0])
for value in items[1:]:
    my_list.append(value)

print_list(my_list)

delete_k(my_list, 2)

print_list(my_list)
