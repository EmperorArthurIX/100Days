def mergeSort(arr):
    """
    Sorts the given sequence
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted by reference, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n.log2(n)) - log base 2 since divided into half. Can make log base k for k parts
    - Space:
        - O(n) for arrays
        - O(log2(n)) for linked lists
    - Swaps:
        - Not applicable
    - Stability:
        Stable
    - Use case:
        - When Extra space is available
        - When insertion is cheap
        - When random access to elements is not available
    """

    # Security Checks
    if arr is None:
        return
    try:
        if len(arr) == 0:
            return
    except:
        raise TypeError("Argument does not seem to be iterable")
    
    # Main Sorting
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        try:
            mergeSort(L)
            mergeSort(R)
        except Exception as exp:
            print("The following error occured: {}".format(*exp.args))
            return arr      # Prints error message and returns iterable in current state
        
        idxL, idxR, idxArr = 0, 0, 0

        while idxL < len(L) and idxR < len(R):
            try:
                if L[idxL] < R[idxR]:
                    arr[idxArr] = L[idxL]
                    idxL += 1
                else:
                    arr[idxArr] = R[idxR]
                    idxR += 1
                idxArr += 1
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return arr      # Prints error message and returns iterable in current state
        
        while idxL < len(L):
            arr[idxArr] = L[idxL]
            idxArr += 1
            idxL += 1
        
        while idxR < len(R):
            arr[idxArr] = R[idxR]
            idxArr += 1
            idxR += 1
    return arr


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,-34,-44,-0,0]
    print(*mergeSort(arr))

    arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    print(*mergeSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*mergeSort(arr))