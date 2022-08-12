import bst

# test the bst class

tree = bst.BST()

tree.put(11)
tree.put(2)
tree.put(33)
tree.put(4)
tree.put(15)
tree.put(26)
tree.put(7)
tree.put(3)
tree.put(81)
tree.put(19)
tree.put(1)


tree.delete(1)
tree.delete(2)

tree.delete(3)

# tree traversal
print('inorder traversal:')
tree.inorder()

print('preorder traversal:')
tree.preorder()

print('postorder traversal:')
tree.postorder()

print('levelorder traversal:')
tree.levelorder()

print('height of the tree:')
print(tree.height())

print('is the tree balanced:')
print(tree.is_balanced())

