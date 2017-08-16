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
                self.left = self.insert_left(value)
                return self.left
        else:
            if (self.right):
                return self.right.insert_value(value)
            else:
                self.right = self.insert_right(value)
                return self.right

    def print_tree(self, depth=0):
        if not self.left and not self.right:
            print("I am a leaf node of value {value} and depth {depth}".format(
                value=self.value,
                depth=depth
            ))
            return
        if self.left:
            self.left.print_tree(depth + 1)
        print(self.value)
        if self.right:
            self.right.print_tree(depth + 1)

def build_tree(depth, min_value, max_value):
    if max_value <= min_value:
        return None
    value = random.randint(min_value, max_value)
    node = BinaryTreeNode(value)
    if depth > 0:
        node.left = build_tree(depth - 1, min_value, value)
        node.right = build_tree(depth - 1, value + 1, max_value)
    return node
