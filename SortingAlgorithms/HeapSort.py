def heapify(arr, size, root):
    """
        Heapifies the given array. Here, creates/repairs a max-heap.

        - Parameters:
            - arr: Iterable in which is to be heapified
            - size: Size of the iterable
            - root: current
        - Returns:
            - Array heapified by reference, but also returned
        - Time:
            - When used as buildHeap() from scratch:
                - O(n) - When we use the siftDown() process. Start on top and go down
                - O(n.log2(n)) - When we use siftUp() process. Start at the bottom and go up
            - When used to repair a slightly incorrect heap:
                - O(log2(n)) - Only heapifies the incorrectly placed nodes
        - Space:
            O(1)
    """
    largest = root          # Index of largest value set to index of root
    rnode = 2 * root + 2    # Index of right child of root
    lnode = 2 * root + 1    # Index of left child of root

    if lnode < size and arr[largest] < arr[lnode]:
        largest = lnode     # If value at left child is greater than root, largest index is left child
    
    if rnode < size and arr[largest] < arr[rnode]:
        largest = rnode     # If value at right child is greater than value at current largest, largest index is right child
    
    if largest != root:     # If root is not largest, exchange value at root with value at largest
        arr[root], arr[largest] = arr[largest], arr[root]
        
        # Heapify the largest value
        heapify(arr, size, largest)
    return arr

def heapSort(arr):
    """
    Sorts the given sequence
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted in place, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n.log2(n))
            - O(n) for traversing the array
            - O(log2(n)) for deleting the max element from heap
            - O(log2(n)) for heapifying again
            - Total: O(n.log2(n) + log2(n))
    - Space:
        O(1)
    - Stability:
        Not Stable
    - Adaptivity:
        Not Adaptive
    - Use case:
        - When the Maximum or Minimum value is needed instantly (even in the middle of sorting)
    """
    # Security Checks
    if arr is None:
        return
    try:
        if len(arr) == 0:
            return
    except:
        raise TypeError("Argument does not seem to be iterable")

    # Finishing Trivial Cases
    if len(arr) == 1:
        return arr
    try:
        if len(arr) == 2:
            if arr[0] < arr[1]:
                return arr
            else:
                arr[0], arr[1] = arr[1], arr[0]
                return arr
    except Exception as exp:
        print("The following error occured: {}".format(*exp.args))
        return arr      # Prints error message and returns iterable in current state

    # Main Sort
    for i in range(len(arr)//2 - 1, -1, -1):    # Heapify node wise, till second last row. No need to touch leaves
        heapify(arr, len(arr), i)
    
    for i in range(len(arr)-1, 0, -1):          
        arr[i], arr[0] = arr[0], arr[i]         # Put largest value at end, bring random small value at root.
        heapify(arr, i, 0)                      # Heapify the remainder, let the sorted ones be untouched
    
    return arr


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,-34,-44,-0,0]
    print(*heapSort(arr))

    arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    print(*heapSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*heapSort(arr))
