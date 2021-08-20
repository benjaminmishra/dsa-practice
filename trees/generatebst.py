from .BinarySearchTree import BinarySearchTree

def create_bst():
    bst = BinarySearchTree(30)
    bst.left_child = BinarySearchTree(7)
    bst.right_child = BinarySearchTree(70)
    bst.left_child.left_child = BinarySearchTree(6)
    bst.left_child.right_child = BinarySearchTree(10)
    bst.right_child.left_child = BinarySearchTree(50)
    bst.right_child.right_child = BinarySearchTree(85)
    bst.right_child.right_child.right_child = BinarySearchTree(90)
    return bst




#######################

#           30
#          /   \
#        7      70
#       / \     / \
#      6  10   50  85
#                   \
#                    90
########################