def insertSort(arr):
    """
    Sorts the given sequence
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted in place, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n^2) - Worst Case
        - O(nk)
            - Adaptive: Stops once sorted
            - 1 <= k <= n
    - Space:
        O(1)
    - Swaps:
        O(n^2)
    - Stability:
        Stable
    - Adaptivity:
        Adaptive - O(n) when nearly sorted
    - Use case:
        - Inserting incoming data into pre-existing sequence
        - Nearly-sorted sequence
        - Small sequence
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
    
    # Main Sorting
    for i in range(1, len(arr)):
        val = arr[i]
        j = i-1
        try:
            while j >= 0 and val < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = val
        except Exception as exp:
            print("The following error occured: {}".format(*exp.args))
            return arr      # Prints error message and returns iterable in current state
    
    return arr


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,-34,-44,-0,0]
    print(*insertSort(arr))

    arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    print(*insertSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*insertSort(arr))