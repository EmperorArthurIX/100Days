def linearSearch(key, arr):
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
        O(n/2)
    - Space:
        O(1)
    """
    for i in range(len(arr)//2 + 1):
        j = (len(arr) - 1) - i
        if arr[i] is key:
            return i
        if arr[j] is key:
            return j
    raise LookupError("Element not found in iterable")


if __name__== '__main__':
    arr = [1,2,3,4,1,2,3,4,1,2,3,4]
    try:
        print(linearSearch(5, arr))
    except Exception as exp:
        print(exp.args[0])
    try:
        print(linearSearch(3, arr))
    except Exception as exp:
        print(exp.args[0])