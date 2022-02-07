def selectSort(arr):
    """
    Sorts the given sequence
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted in place, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n^2)
        - Not adaptive
    - Space:
        O(1)
    - Swaps:
        O(n) maximum
    - Stability:
        Unstable
    - Use case:
        When repeated swapping is expensive but time is available
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
    for i in range(len(arr)):
        minidx = i
        for j in range(i+1, len(arr)):
            try:
                if arr[minidx] > arr[j]:        # Find index of minimum value element
                    minidx = j
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return arr      # Prints error message and returns iterable in current state
        if minidx is not i:
            arr[i], arr[minidx] = arr[minidx], arr[i]
    
    return arr


if __name__ == "__main__":
    arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    print(*selectSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = ['123', 'a', 'abcabcabc', '', True]
    # print(*selectSort(arr))