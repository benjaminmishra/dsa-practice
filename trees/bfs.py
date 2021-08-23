from BinarySearchTree import BinarySearchTree
from generatebst import create_bst
from queue import SimpleQueue


bst : BinarySearchTree= create_bst()


def bfs_print(root : BinarySearchTree)-> None:
    q :  SimpleQueue = SimpleQueue()
    curr = root
    q.put(curr)
    
    if bst is None: return None

    while not q.empty():
        curr : BinarySearchTree = q.get()

        if curr is not None:
            print(curr.data)
            
            if curr.right_child is not None:
                q.put(curr.left_child)

            if curr.right_child is not None:
                q.put(curr.right_child)