class Node():
    """
    The subclass used within a Linked List, to represent each element
    """
    def __init__(self, data) -> None:
        self.data = data
        self.prev = self.next = None

# INCOMPLETE
class LinkedList():
    """
    A class representing the Linked List data structure.

    - Constructor parameters:
        - data:
            - When individual value is passed, head node is initialised with the value
            - When sorted `list()` or `tuple()` is passed, a LinkedList is initialised with the values in the iterable
    - Attributes:
        - size:
            Returns the value of the size of the list
        - head:
            Returns a reference to the `head` node of the list
        - tail:
            Returns a reference to the `tail` node of the list
    - Behaviours:
        - insert(data, index):
            - Inserts `data` at 0-based `index` node of the list
            - Passing `-1` as index appends data
        - append(data):
            Inserts `data` at the end of the list
        - appendAll(arr):
            - Inserts all elements from the iterable `arr` into the list
        - pop(index(optional)):
            - Removes and returns the value of the element at the 0-based `index` node of the list
            - If no index is passed, removes and returns the value of the element at the end of the list
        - display():
            Displays the contents of the list
        - toList():
            Returns a Python List of the contents of this Linked List
    """
    
    def __init__(self, data) -> None:
        if type(data) in [type(list()), type(tuple())]:
            self.head = self.tail = Node(data[0])
            self.size = 1
            if len(data[1:]) > 0:
                self.appendAll(data[1:])
        else:
            self.head = self.tail = Node(data)
            self.size = 1
    
    def insert(self, data, index = -1):
        if index < -1 or index > self.size:
            raise IndexError("Index value must be an integer between -1 and size of list")
        
        if self.head:
            if self.size == 1 and index == 0 or index == -1:
                self.tail == Node(self.head.data)
                self.head.next = self.tail
                self.tail.prev = self.head
                self.size += 1
                return
            
            if self.size == 1 and index == self.size:
                self.tail.data = Node(data)
                self.tail.prev = self.head
                self.head.next = self.tail
                self.size += 1
                return
            
            if self.size > 1 and index == 0:
                new = Node(data)
                new.next = self.head
                self.head.prev = new
                self.head = new
                self.size += 1
                return
            
            if index == -1 or index == self.size:
                new = Node(data)
                self.tail.next = new
                new.prev = self.tail
                self.tail = new
                self.size += 1
                return
            
            if 0 < index < self.size:
                i = 0
                curr = self.head
                while i < index:
                    curr = curr.next
                    i += 1
                new = Node(data)
                new.next = curr.next
                new.prev = curr
                curr.next.prev = new
                curr.next = new
                self.size += 1
                return
            return
        self.head = Node(data)
        self.size += 1
    
    def appendAll(self, arr):
        if type(arr) not in [type(list()), type(tuple())]:
            raise TypeError("A list or tuple of elements must be passed.")
        if len(arr) == 0:
            return
        if len(arr) == 1:
            self.append(arr[0])
        for i in range(len(arr)):
            try:
                self.append(arr[i])
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return
    
    def append(self, data):
        self.insert(data)
    
    def pop(self, index=-1):
        if index <= -1 or index > self.size - 1:
            raise IndexError("Index value must be an integer greater than or equal to -1 and less than size of list")
        if self:
            if self.size < 1:
                raise IndexError("Cannot pop from empty list")
            if self.size == 1:
                temp = self.head.data
                self.head = None
                self.size -= 1
                return temp
            if self.size == 2 and index == -1 or index == self.size-1:
                temp = self.tail.data
                self.tail = None
                self.tail = self.head
                self.tail.prev = self.head
                self.head.next = self.tail
                self.size -= 1
                return temp
            if self.size == 2 and index == 0:
                temp = self.head.data
                self.head = None
                self.head = self.tail
                self.tail.prev = self.head
                self.head.next = self.tail
                self.size -= 1
                return temp
            if index == -1 or index == self.size - 1:
                temp = self.tail.data
                self.tail.prev.next = None
                self.tail = self.tail.prev
                self.size -= 1
                return temp
            if 0 < index < self.size-1:
                i = 0
                curr = self.head
                while i <= index:
                    curr = curr.next
                    i += 1
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr = None
                self.size -= 1
        raise LookupError("Node object not found")
    
    def display(self):
        curr = self.head
        for i in range(self.size):
            print(curr.data, end="\t")
            curr = curr.next
        print()
    
    def toList(self):
        curr = self.head
        arr = list()
        for i in range(self.size):
            arr.append(curr.data)
            curr = curr.next
        return arr
    

# Test
if __name__ == "__main__":
    # ll = LinkedList([1,2,3,4,5,5,4,3,2,1])
    ll = LinkedList(1)
    ll.insert(2,0)
    ll.display()