def radixSort(arr):
    """
    Sorts the given sequence of non-negative integers
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted by reference, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(p.n)
            - p is the number of passes = number of digits of largest element
    - Space:
        O(n+k)
            - k is the maximum number of elements with common digit at same place value
            - 0 <= k <= n
    - Stability:
        Stable
    - Use case:
        - Counting sort, but with less space
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
    hi = max(arr)
    radix = []*10

    passes = 0
    try:
        while hi > 0:
            passes += 1
            hi //= 10
    except Exception as exp:
        print("The following error occured: {}".format(*exp.args))
        return arr      # Prints error message and returns iterable in current state
    
    for i in range(passes):     # Appears like 2 Loops, but is actually constant time multiplier
        for j in range(10):
            radix.append(list())
        try:
            for num in (arr):
                digit = (num//pow(10,i))%10
                radix[digit].append(num)
        except Exception as exp:
            print("The following error occured: {}".format(*exp.args))
            return arr      # Prints error message and returns iterable in current state
    
        arr.clear()
        for i in range(10):
            arr.extend(radix[i])
        radix.clear()
    
    return arr


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,34,44,0,0]
    print(*radixSort(arr))

    # arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    # print(*radixSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*radixSort(arr))