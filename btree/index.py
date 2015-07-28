'''
Making a b-tree, because why not?
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.tree = BTree(self)
        self.left = BTree()
        self.right = BTree()

class BTree(object):
    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def find(self, value):
        if self.root is None:
            return self
        elif value < self.root.value:
            return self.root.left.find(value)
        else:
            return self.root.right.find(value)

    def insert(self, value):
        tree = self.find(value)
        tree.root = Node(value)

    def depth_print(self):
        if (self.root is not None):
            print self.root.value
            self.root.left.depth_print()
            self.root.right.depth_print()


tree = BTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)

tree.depth_print()
