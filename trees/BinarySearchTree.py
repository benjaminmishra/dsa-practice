class BinarySearchTree :

    def __init__(self, val) -> None:
        self.data : int= val
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




def min_value(root: BinarySearchTree)->int:
    curr = root
    if root is None:
        return -1
    
    # keep goin left, as long as we have left
    while curr.left_child: curr = curr.left_child

    return curr.data



def max_value(root: BinarySearchTree)->int:
    curr = root
    if root is None:
        return -1

    # keep going riht
    while curr.right_child : curr = curr.right_child

    return curr
    



def height(root:BinarySearchTree)-> int :
    left_depth : int = 0
    right_depth : int = 0

    if root is None:
        return -1

    if root.left_child :
        left_depth = height(root.left_child)
        
    if root.right_child:
        right_depth = height(root.right_child)

    return max(left_depth,right_depth) + 1    




def delete_node(root : BinarySearchTree, value : int) -> BinarySearchTree:
    '''Delete a node in BST when its root and the value of node to be delete is provided'''
    curr = root

    # if the root node is none , just return it
    if root is None:
        return root

    if curr.data > value:
        curr.left_child = delete_node(curr.left_child, value)
    elif curr.data < value:
        curr.right_child = delete_node(curr.right_child, value)
    else:
        # if no child nodes
        if curr.left_child is None and curr.right_child is None:
            curr = None

        # if only ight child node present
        elif curr.left_child is None and curr.right_child:
            curr = curr.right_child

        # if only left child node present
        elif curr.right_child is None and curr.left_child:
            curr = curr.left_child

        # if both present
        else:
            curr.data = min_value(curr.right_child)
            curr.right_child = delete_node(curr.right_child, curr.data)

    return curr





