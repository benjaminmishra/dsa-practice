from trees import height, BinarySearchTree, create_bst, bfs_print




bst : BinarySearchTree = create_bst()

bst.insert(53)

print("Depth of tree : " + str(height(bst)))

inorder_result  = bst.inorder()
print("Inroder Traversal : " + str(inorder_result))

preorder_result = bst.preorder()
print("Preorder Traversal : " + str(preorder_result))

postorder_result = bst.postorder()
print("Postorder Traversal : " + str(postorder_result))


bfs_print(bst)