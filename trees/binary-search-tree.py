from _typeshed import Self
from typing import Union


class BinarySearchTree :

    def __init__(self, val) -> None:
        self.data = val
        self.left_child = None
        self.right_child = None


    def insert(self, value) -> None:
        '''
        Function to insert a node into Binary Search Tree
        '''
        # if the data field is not set the set it
        if not self.data:
            self.data = value

        # if the data field is set and value is greater than data 
        # then insert left child, other wise insert right child
        if self.data > value:
            if self.left_child:
                self.left_child.insert(value)
                return 
            self.left_child = BinarySearchTree(value)
        elif self.data < value:
            if self.right_child:
                self.right_child.insert(value)
                return
            self.right_child = BinarySearchTree(value)

            

