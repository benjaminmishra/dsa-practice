class BinarySearchTree :

    def __init__(self, val) -> None:
        self.data = val
        self.left_child = None
        self.right_child = None


    def depth()-> int :


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


    def inorder(self) -> list[int]:
        result : list[int] = []
        if self :
            if self.left_child :
                result.extend(self.left_child.inorder())

            result.append(self.data)

            if self.right_child:
                result.extend(self.right_child.inorder())

        return result


    def preorder(self)-> list[int]:
        result : list[int] = []
        if self:
            result.append(self.data)

            if self.left_child:
                result.extend(self.left_child.preorder())

            if self.right_child:
                result.extend(self.right_child.preorder())

        return result


    def postorder(self)-> list[int]:
        result : list[int] = []

        if self:
            if self.left_child:
                result.extend(self.left_child.postorder())

            if self.right_child:
                result.extend(self.right_child.postorder())
            
            result.append(self.data)

        return result
            

