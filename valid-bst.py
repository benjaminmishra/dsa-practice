from trees import BinarySearchTree
from trees import generatebst


# ------------------------------- Problem Description ----------------------------
#
#
# ---------------------------------------------------------------------------------



# ------------------------------ Brute Force Solution ------------------------------
#
#
#
# Time Complexity :
#
# Space Complexity
# ----------------------------------------------------------------------------------

# main function 
def validate_bst(root : BinarySearchTree)-> bool:
    return is_valid(root, float("inf"), float("-inf"))

# recursive code
def is_valid(node : BinarySearchTree, max, min) -> bool:
    if not node:
        return True

    if node.data < min or node.data > max:
        return False    

    return is_valid(node.left_child, node.data, min) and is_valid(node.right_child, max, node.data)



# Driver Code

def main():
    root_1 : BinarySearchTree = generatebst.create_bst()
    result_1 = validate_bst(root_1)
    print(result_1)

    root_2 : BinarySearchTree = None
    result_2 = validate_bst(root_2)
    print(result_2)




main()
