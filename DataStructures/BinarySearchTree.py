class BinarySearchTree():
    """
    A class representing the Binary Search Tree data structure.
    A BST is a Binary Tree in which the left child of any node is smaller than itself, while the right child is larger than itself.
    
    - Note:
        - Every node of this tree inherits all properties of the class

    - Constructor parameters:
        - data:
            - When individual value is passed, root node is initialised with the value
            - When sorted `list()` or `tuple()` is passed, a BST is initialised with the values in the iterable
    
    - Attributes:
        - left: Left child of current node - 'None' by default
        - right: Right child of current node - 'None' by default
        - data: Value stored in the current node - 'None' by default
    
    - Behaviours:
        - insert(data):
            Automatically inserts data at appropriate position, without duplication
        - insertAll(arr):
            Inserts elements in the iterable `arr` at their appropriate position
        - display():
            Print contents of tree in order
        - display_util():
            Used within display()
        - inOrder():
            Returns an array with elements of tree in-order
        - preOrder():
            Returns an array with elements of tree pre-order
        - postOrder():
            Returns an array with elements of tree post-order
        - height():
            - Returns the height of current node from which it was called
            - Returns the height of tree by default
            - Height of leaf node == 0
        - delete(data):
            - Removes the node which carries the value `data`
            - Raises a `LookupError()` error if not found
        - search(value):
            - Searches for value in the tree and returns node with value if found
    """
    valid_iter_types = [type(list()), type(tuple())]
    def __init__(self, data) -> None:
        self.right = None
        self.left = None
        if type(data) not in self.valid_iter_types:
            self.data = data
        else:
            self.data = data[len(data)//2]
            self.insertAll(data)

    
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
        """
        Inserts the given data at its appropriate position in the tree. Does not allow duplicate entries

        - Returns:
            None
        
        - Time:
            - O(log2(n)) - Balanced or nearly balanced tree
            - O(n) - Skewed tree
        
        - Space:
            O(1)
        """
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
        """
        Inserts all values in the iterable passed, at their appropriate positions in the tree

        - Returns:
            None
        
        - Time: For data sequence of size `k`
            - O(k.log2(n + (k/2)) - Balanced or nearly balanced tree
            - O(k.(n+(k/2)) - Skewed tree
            - n+(k/2) is considered here to account for the average growth in the size of the tree over the course of insertion of `k` elements.

        - Space:
            O(1)
        """
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
        """
        Conducts In-Order traversal of tree
        
        - Returns:
            An array with values of all nodes in In-Order sequence
        
        - Time:
            O(n)
        
        - Space:
            O(n)
        """
        if self:
            if self.left:
                self.left.inOrder(arr)
            arr.append(self.data)
            if self.right:
                self.right.inOrder(arr)
        return arr
    
    
    def preOrder(self, arr):
        """
        Conducts Pre-Order traversal of tree
        
        - Returns:
            An array with values of all nodes in Pre-Order sequence
        
        - Time:
            O(n)

        - Space:
            O(n)
        """
        if self:
            arr.append(self.data)
            if self.left:
                self.left.preOrder(arr)
            if self.right:
                self.right.preOrder(arr)
        return arr
    
    
    def postOrder(self, arr):
        """
        Conducts Post-Order traversal of tree
        
        - Returns:
            An array with values of all nodes in Post-Order sequence
        
        - Time:
            O(n)

        - Space:
            O(n)
        """
        if self:
            if self.left:
                self.left.postOrder(arr)
            if self.right:
                self.right.postOrder(arr)
            arr.append(self.data)
        return arr
    
    
    def height(self):
        """
        Calculates the height of the node from which it was called

        - Returns:
            - Height of the tree when called from root
            - Height of a node when called from it
            - Integer value '0' when called from a leaf node
        
        - Time:
            O(n)

        - Space:
            O(1)
        """
        if self:
            L = R = -1
            if self.left:
                L = self.left.height()
            if self.right:
                R = self.right.height()

            return max(L + 1, R + 1)
        return -1
    
    
    def isLeaf(self):
        """
        Checks if the node it was called from is a Leaf

        - Returns:
            - Boolean `True` if the node is a leaf node
            - Boolean `False` is the node is NOT a leaf node
        
        - Time:
            O(1)
        
        - Space:
            O(1)
        """
        return (self.left is None and self.right is None)
    
    
    def getMin(self):
        """
        Returns node which holds the smallest value

        - Time:
            - O(log2(n)) - Balanced or nearly balanced tree
            - O(n) - Skewed tree
        
        - Space:
            O(1)
        """
        while self.left:
            self = self.left
        return self
    
    
    def delete(self, data):
        """
        Deletes the node carrying the value `data`

        - Time:
            - `Case 1`: Deleting a Leaf Node:
                - O(log2(n)) - Balanced or nearly balanced tree
                - O(n) - Skewed tree
            - `Case 2`: Deleting a node with only 1 child:
                - O(log2(n)) - Balanced or nearly balanced tree
                - O(n) - Skewed tree
            - `Case 3`: Deleting a node with 2 children:
                - InOrder `successor` node is leaf node:
                    - O(log2(n) + O(`Case 2`))
                        - O(log2(n)) - Balanced tree in both cases
                        - O(n) - Skewed tree in any 1 case
                    - O(n) - Skewed tree from the beginning
                - InOrder `successor` node is a node with 1 child. The `successor` is calculated such that it can have at most 1 child, the right child
                    - O(log2(n) + O(`node.getMin()`) + O(`node.delete(successor.data)`))
                        - O(log2(n)) - Balanced tree in all three cases
                        - O(n) - Skewed tree in any 1 case
                    - O(n) - Skewed tree from the beginning
        
        - Space:
            O(1)
        """
        parent = None
        current = self

        while current and current.data != data:
            parent = current

            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            return self
        
        if current.isLeaf():
            if current is not self:
                if parent.left is current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self = None
            return
        
        if current.left and current.right:
            successor = current.right.getMin()
            value = successor.data
            self.delete(value)
            current.data = value
            return
        
        # If we reach this point means exactly 1 child
        if current.left:
            child = current.left
        else:
            child = current.right
        
        if current is not self:
            if current is parent.left:
                parent.left = child
            else:
                parent.right = child
            return
        self = child
        return self
    
    def search(self, value):
        """
        Searches for given value in the tree

        - Parameters
            - value: The value to search for
        
        - Returns:
            - BinarySearchTree() object which holds the given value
            - `None` when value is not found
            - `None` when error occurs while searching
        
        - Time:
            - O(log2(n)) - Balanced or nearly balanced tree
            - O(n) - Skewed tree
        """
        if self:
            try:
                if self.data == value:
                    return self
                if self.left and self.data > value:
                    return self.left.search(value)
                if self.right and self.data < value:
                    return self.right.search(value)
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return


# Test
if __name__ == "__main__":
    bst = BinarySearchTree(0)
    bst.insert(-1)
    bst.insert(1)
    bst.display()
    bst.insertAll([-1,-2,-3,-4,-11,1000,12,0,0,0,0,0,0,0,0,122,16,-67,-78,-97,7,7,5,-9, 100,1024,220, -242,-2354,446,-465,555,-645,10,-45,-232,2233])
    print(*bst.inOrder(list()))
    bst.insertAll([-1,-2,-3,-4,-5,-6,-7,-8,1,2,3,4,5,6,7,8])
    print(*bst.inOrder(list()))
    bst.delete(2233)
    print(*bst.inOrder(list()))
    bst.delete(0)
    print(*bst.inOrder(list()))
    bst.delete(-67)
    print(bst.search(-2354))
    print(*bst.inOrder(list()))
    print(*bst.preOrder(list()))
    print(*bst.postOrder(list()))
    print(bst.height())
    print(bst.left.height())
    print("CHANGING THE BST:")
    bst = BinarySearchTree([1,2,3,4,5,6,7,8,9,10])
    bst.display()