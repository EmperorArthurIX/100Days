class BinarySearchTree():
    """
    A class representing the Binary Search Tree data structure
    A BST is a Binary Tree in which the left child of any node is smaller than itself, while the right child is larger than itself
    
    - Attributes:
        - left: Left child of current node - 'None' by default
        - right: Right child of current node - 'None' by default
        - data: Value stored in the current node - 'None' by default
    - Constructors:
        - No arguments: Empty BST
        - data: BST with root value == data
    - Behaviours:
        - insert(data): Automatically inserts data in appropriate position. No duplicacy
    """
    data = left = right = None
    
    def __init__(self) -> None:
        pass
    def __init__(self, data) -> None:
        self.data = data
    