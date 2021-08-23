import BinarySearchTree as b

def create_bst():
    bst = b.BinarySearchTree(30)
    bst.left_child = b.BinarySearchTree(7)
    bst.right_child = b.BinarySearchTree(70)
    bst.left_child.left_child = b.BinarySearchTree(6)
    bst.left_child.right_child = b.BinarySearchTree(10)
    bst.right_child.left_child = b.BinarySearchTree(50)
    bst.right_child.right_child = b.BinarySearchTree(85)
    bst.right_child.right_child.right_child = b.BinarySearchTree(90)
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