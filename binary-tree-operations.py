from trees.BinarySearchTree import height, BinarySearchTree


# create a BST
bst = BinarySearchTree(30)
bst.left_child = BinarySearchTree(7)
bst.right_child = BinarySearchTree(80)
bst.left_child.left_child = BinarySearchTree(6)
bst.left_child.right_child = BinarySearchTree(10)
bst.right_child.left_child = BinarySearchTree(50)
bst.right_child.right_child = BinarySearchTree(85)

bst.insert(53)

print("Depth of tree : " + str(height(bst)))

inorder_result  = bst.inorder()
print("Inroder Traversal : " + str(inorder_result))

preorder_result = bst.preorder()
print("Preorder Traversal : " + str(preorder_result))

postorder_result = bst.postorder()
print("Postorder Traversal : " + str(postorder_result))