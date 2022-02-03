def jumpSearch(key, arr):
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
        O(sqrt(n))
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
    
    # Optimisation, to finish trivial search in Constant Time and Space
    if len(arr) <= 2:
        if key is arr[0]:
            return 0
        if key is arr[-1]:
            return len(arr)-1
        raise LookupError("Element not found in iterable")
    
    # Main Search
    step = int(len(arr)**.5)
    for i in range(0, len(arr), step):
        if key is arr[i]:
            return i
        if key < arr[i]:
            j = i
            while j > i-step:   # Occurs only once - Added time, not multiplied
                if key is arr[j]:
                    return j
                j -= 1
            raise LookupError("Element not found in iterable")  # Checks for missing values larger than elements
    raise LookupError("Element not found in iterable")  # Checks for missing values smaller than elements


# Test
if __name__ == "__main__":
    arr = [-1,0,1,2,3,4,5,6,7,8,9]
    try:
        print(jumpSearch(10, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(jumpSearch(-1, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(jumpSearch(3, arr))
    except Exception as exp:
        print(exp.args[0])