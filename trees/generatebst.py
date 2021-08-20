import BinarySearchTree

def create_bst():
    bst = BinarySearchTree(30)
    bst.left_child = BinarySearchTree(7)
    bst.right_child = BinarySearchTree(80)
    bst.left_child.left_child = BinarySearchTree(6)
    bst.left_child.right_child = BinarySearchTree(10)
    bst.right_child.left_child = BinarySearchTree(50)
    bst.right_child.right_child = BinarySearchTree(85)
    return bst