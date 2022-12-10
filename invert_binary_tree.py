

# ------------------------------- Problem Description ----------------------------
# Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and 
# right children of all non-leaf currents interchanged. 
# ---------------------------------------------------------------------------------



# ------------------------------ Iterative Solution BFS ------------------------------
# Using breadth first seach to do the inversion
# Take a queue and start queing each node to starting from the root node into the queue
# First swap the children nodes and then queue each of them into the queue for further processing
# Time Complexity : O(log n) i.e. the height of the tree
#
# Space Complexity : O(n) : Linear time because of the 
# ----------------------------------------------------------------------------------
from trees import BinarySearchTree, generatebst
from queue import SimpleQueue

def invert_bfs(root : BinarySearchTree) -> None:
    q :SimpleQueue = SimpleQueue()
    q.put(root)

    while not q.empty():
        current :BinarySearchTree = q.get()

        if current :
            # swap children currents
            current.left_child , current.right_child = current.right_child , current.left_child

            if current.left_child:
                q.put(current.left_child)

            if current.right_child:
                q.put(current.right_child)




# ----------------------------- Recursive Solution --------------------------------
#
#
#
# Time Complexity:
#
# Space Complexity:
#------------------------------------------------------------------------------------

def function_name_efficient():
    pass



# Driver Code

def main():
    bst : BinarySearchTree = generatebst.create_bst()
    invert_bfs(bst)

    



main()
