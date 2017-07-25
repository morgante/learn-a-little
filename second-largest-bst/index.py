'''
https://www.interviewcake.com/question/python/second-largest-item-in-bst
'''
import random

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def insert_value(self, value):
        if (value <= self.value):
            if (self.left):
                return self.left.insert_value(value)
            else:
                return self.left = self.insert_left(value)
        else:
            if (self.right):
                return self.right.insert_value(value)
            else:
                return self.right = self.insert_right(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.value)

def build_tree(depth, min_value, max_value):
    value = random.randint(min_value, max_value)
    node = BinaryTreeNode(value)
    if depth > 0:
        node.left = build_tree(depth - 1, min_value, value)
        node.right = build_tree(depth - 1, value + 1, max_value)
    return node

tree = build_tree(5, 3, 100)
tree.print_tree()
