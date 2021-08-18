from Trees import BinarySearchTree


bst = BinarySearchTree.BinarySearchTree(8)
bst.insert(9)
bst.insert(10)
bst.insert(7)
bst.insert(5)


inorder_result  = bst.inorder()
print("Inroder Traversal : " + str(inorder_result))

preorder_result = bst.preorder()
print("Preorder Traversal : " + str(preorder_result))

postorder_result = bst.postorder()
print("Postorder Traversal : " + str(postorder_result))