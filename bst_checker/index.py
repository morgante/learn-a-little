'''
https://www.interviewcake.com/question/python/bst-checker

Run me with this command:
```
python3 -m bst_checker.index
```

'''

from common.bst import BinaryTreeNode, build_tree

def is_valid_bst(node, max_value=float('inf'), min_value=-float('inf')):
    if node.value >= max_value:
        # print('too big', node.value, max_value)
        return False
    if node.value <= min_value:
        # print('too small', node.value, min_value)
        return False
    
    if node.left:
        left_valid = is_valid_bst(node.left, max_value=node.value, min_value=min_value)
    else:
        left_valid = True
    
    if node.right:
        right_valid = is_valid_bst(node.right, min_value=node.value, max_value=max_value)
    else:
        right_valid = True

    return left_valid and right_valid

my_tree = build_tree(3, 5, 500)

my_tree.print_tree()

print('should be valid:', is_valid_bst(my_tree))

my_tree.left.right.value = my_tree.value + 1
print('should be invalid:', is_valid_bst(my_tree))

new_tree = BinaryTreeNode(50)
new_tree.left = BinaryTreeNode(30)
new_tree.left.left = BinaryTreeNode(20)
new_tree.left.right = BinaryTreeNode(60)
new_tree.right = BinaryTreeNode(80)
new_tree.right.left = BinaryTreeNode(70)
new_tree.right.right = BinaryTreeNode(90)

print('should be invalid:', is_valid_bst(new_tree))
