class BinarySearchTree():
    """
    A class representing the Binary Search Tree data structure.
    A BST is a Binary Tree in which the left child of any node is smaller than itself, while the right child is larger than itself.
    
    - Note:
        - Every node of this tree inherits all properties of the class
    
    - Attributes:
        - left: Left child of current node - 'None' by default
        - right: Right child of current node - 'None' by default
        - data: Value stored in the current node - 'None' by default
    
    - Behaviours:
        - insert(data): Automatically inserts data in appropriate position, without duplication
        - insertAll(arr): Inserts elements in the iterable in their appropriate position
        - display(): Print contents of tree in order
        - display_util(): Used within display()
        - inOrder(): Returns an array with elements of tree in-order
        - preOrder(): Returns an array with elements of tree pre-order
        - postOrder(): Returns an array with elements of tree post-order
        - height():
            - Returns the height of current node from which it was called.
            - Returns the height of tree by default
            - Height of leaf node == 0
    """
    data = left = right = None
    
    def __init__(self, data) -> None:
        self.data = data
    
    def display(self):      # Can also use a decorator instead of this setup
        if self:
            self.display_util()
        print()
    
    def display_util(self):
        if self:
            if self.left:
                self.left.display_util()
            print(self.data, end="\t")
            if self.right:
                self.right.display_util()
    
    def insert(self, data):
        if self:
            if self.data is None:
                self.data = data
                return
            try:
                if data < self.data:
                    if self.left:
                        self.left.insert(data)
                        return
                    self.left = BinarySearchTree(data)
                    return
                if data > self.data:
                    if self.right:
                        self.right.insert(data)
                        return
                    self.right = BinarySearchTree(data)
                    return
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return
        self = BinarySearchTree(data)
    
    def insertAll(self, arr):
        if arr is None:
            raise TypeError("'None' was passed instead of iterable")
        
        try:
            if len(arr) == 0:
                return
        except Exception as exp:
            print("The following error occured: {}".format(*exp.args))
            return
        
        if len(arr) == 1:
            self.insert(arr[0])
            return
        
        try:
            if len(arr) > 1:
                for i in arr:
                    self.insert(i)
                return
        except Exception as exp:
            print("The following error occured: {}".format(*exp.args))
            return
    
    def inOrder(self, arr):
        if self:
            if self.left:
                self.left.inOrder(arr)
            arr.append(self.data)
            if self.right:
                self.right.inOrder(arr)
        return arr
    
    def preOrder(self, arr):
        if self:
            arr.append(self.data)
            if self.left:
                self.left.preOrder(arr)
            if self.right:
                self.right.preOrder(arr)
        return arr
    
    def postOrder(self, arr):
        if self:
            if self.left:
                self.left.postOrder(arr)
            if self.right:
                self.right.postOrder(arr)
            arr.append(self.data)
        return arr
    
    def height(self):
        if self:
            L = R = -1
            if self.left:
                L = self.left.height()
            if self.right:
                L = self.right.height()

            return max(L + 1, R + 1)
        return -1


# Test
if __name__ == "__main__":
    bst = BinarySearchTree(0)
    bst.insert(-1)
    bst.insert(1)
    bst.display()
    bst.insertAll([-1,-2,-3,-4,-11,1000,12,0,0,0,0,0,0,0,0,122,16,-67,-78,-97,7,7,5,-9])
    print(*bst.inOrder(list()))
    print(*bst.preOrder(list()))
    print(*bst.postOrder(list()))
    print(bst.height())
    print(bst.left.height())