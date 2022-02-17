def binarySearch(key, arr):
    """
    Searches for the key value in the given sorted sequence
    
    - Parameters:
        - key: Value to be searched
        - arr: Iterable in which 'key' is to be searched
    - Returns:
        0-based index of 'key', if found
    - Raises:
        LookupError() when element is not found
    - Time:
        O(log2(n))
    - Space:
        O(1)
    """
    # Security Checks
    if arr is None:
        raise TypeError("Passed None where Iterable was expected")
    if len(arr) == 0:
        raise ValueError("Tried to search in empty list")
    if type(key) is not type(arr[0]):
        raise TypeError("Tried to search for {} in list of {}".format(type(key), type(arr[0])))
    
    # Optimisation, to finish trivial searches in Constant Time and Space
    if len(arr) <= 2:
        if key is arr[0]:
            return 0
        if key is arr[-1]:
            return len(arr)-1
        raise LookupError("Element not found in iterable")
    
    # Main Search
    hi = len(arr)-1
    lo = 0
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if key is arr[hi]:  # Check rightmost
            return hi
        if key is arr[lo]:  # Check leftmost
            return lo
        if key is arr[mid]: # Check middle
            return mid
        if key < arr[mid]:  # Optimisation - Update both hi and lo, to save iteration time
            hi = mid-1
            lo += 1
        elif key > arr[mid]:    # Optimisation -  Update both hi and lo, to save iteration time
            lo = mid+1
            hi -= 1
    raise LookupError("Element not found in iterable")
    

# Test
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    try:
        print(binarySearch(5, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(binarySearch(4, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(binarySearch(3, arr))
    except Exception as exp:
        print(exp.args[0])