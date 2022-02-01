def binarySearch(key, arr):
    """
    Searches for the key value in the given sequence
    
    - Parameters:
        key: Value to be searched
        arr: Iterable in which 'key' is to be searched
    - Returns:
        0-based index of 'key', if found
    - Raises:
        LookupError() when element is not found
    - Time:
        O(log2(n))
    - Space:
        O(1)
    """
    
    hi = len(arr)-1
    lo = 0
    if len(arr) <= 2:
        if arr[hi] is key:
            return hi
        if arr[lo] is key:
            return lo
        raise LookupError("Element not found in iterable")
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if key is arr[hi]:  # Check rightmost
            return hi
        if key is arr[lo]:  # Check leftmost
            return lo
        if key is arr[mid]: # Check middle
            return mid
        if key < arr[mid]:  # Update both hi and lo, to save iteration time
            hi = mid-1
            lo += 1
        elif key > arr[mid]:    # Update both hi and lo, to save iteration time
            lo = mid+1
            hi -= 1
        print(1)
    raise LookupError("Element not found in iterable")
    

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,0]
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