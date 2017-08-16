'''
https://www.interviewcake.com/question/python/balanced-binary-tree

Run me with this command:
```
python3 -m balanced_binary_tree.index
```

'''

from common.bst import BinaryTreeNode, build_tree

def get_max_leaf_difference(tree):
    to_traverse = [(0, tree)]
    min_depth = None
    max_depth = 0

    while len(to_traverse) > 0:
        current_depth, node = to_traverse.pop()
        if not node.left and not node.right:
            min_depth = min(min_depth, current_depth) if min_depth is not None else current_depth
            max_depth = max(max_depth, current_depth)
            continue
        if node.left:
            to_traverse.append((current_depth + 1, node.left))
        if node.right:
            to_traverse.append((current_depth + 1, node.right))
        
    return max_depth - min_depth

def is_superbalanced(tree):
    diff = get_max_leaf_difference(tree)
    if diff <= 1:
        return True
    return False

my_tree = build_tree(14, 5, 200)

# my_tree.left.left.left = None
# my_tree.left.left.right = None

print('is superbalanced?', get_max_leaf_difference(my_tree))

my_tree.print_tree()
