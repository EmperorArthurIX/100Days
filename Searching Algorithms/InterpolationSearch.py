def interpolationSearch(key, arr):
    """
    Searches for the key value in the given sorted sequence
    
    Works best when sequence contains uniformly distributed data
    
    - Parameters:
        key: Value to be searched
        arr: Iterable in which 'key' is to be searched
    - Returns:
        0-based index of 'key', if found
    - Raises:
        LookupError() when element is not found
    - Time:
        Uniform Distribution: O(log2(log2(n)))
        Non-uniform Distribution: O(n)
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
    hi = len(arr) - 1
    lo = 0
    def util_inter(key, arr, lo, hi):
        if lo < hi and arr[lo] < key < arr[hi]:
            pos = lo + (key-arr[lo])*(hi-lo)//(arr[hi] - arr[lo])   # Formula for index of highest likelihood

            if arr[pos] is key:     # Check index of high likelihood
                return pos

            if arr[lo] is key:      # Check lowest index
                return lo
            
            if arr[hi] is key:      # Check highest index
                return hi
            
            if arr[pos] < key:
                return util_inter(key, arr, pos+1, hi-1)    # Optimisation - Update both lo and hi based on test above
            
            if arr[pos] > key:
                return util_inter(key, arr, lo+1, pos-1)    # Optimisation - Update both lo and hi, based on test above
        raise LookupError("Element not found")
    
    try:
        return util_inter(key, arr, lo, hi)
    except LookupError as exp:
        raise LookupError("Element not found in iterable") from exp


# Test
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    try:
        print(interpolationSearch(5, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(interpolationSearch(-1, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(interpolationSearch(3, arr))
    except Exception as exp:
        print(exp.args[0])
    
    # Exception Testing
    # Uncomment the following line to test exception stack trace
    # print(interpolationSearch(100, arr))