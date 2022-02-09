def bucketSort(arr):
    """
    Sorts the given sequence of non-negative floating point numbers
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted by reference, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n + k)
            - For traversal of array of length n, followed by sorted insertion among k elements
            - 0 <= k <= n
    - Space:
        O(n)
            - k is the maximum number of elements in the same bucket
            - 0 <= k <= (n/bucket_width)
    - Stability:
        Stable
    - Use case:
        - Counting Sort, but for floating point numbers
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
    lo = min(arr)
    size = hi-lo
    numbuckets = 10     # Actually, there is 1 more bucket for max-value case, but we cannot count it here
    width = size/numbuckets
    buckets = []
    for _ in range(numbuckets+1):
        buckets.append(list())
    
    if size == 1:
        # Use simple bucket sort
        for num in arr:
            try:
                insert_sorted(buckets[int(numbuckets*num)],num)
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return arr      # Prints error message and returns iterable in current state
    else:
        # Use bigger bucket sort
        for num in arr:
            try:
                insert_sorted(buckets[int((num - lo)/width)], num)
            except Exception as exp:
                print("The following error occured: {}".format(*exp.args))
                return arr      # Prints error message and returns iterable in current state
        
    # Join into array
    arr.clear()
    for i in range(numbuckets+1):
        arr.extend(buckets[i])

    return arr

def insert_sorted(arr, val):
    if len(arr) == 0:       # If list is empty, add element
        arr.append(val)
        return
    i = 0
    while i < len(arr):     # Find place to insert in middle
        if arr[i] > val:
            arr.insert(i,val)
            return
        i += 1
    arr.append(val)         # If code reaches here means element is largest. Append at end
    return


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,34,44,0,0]
    print(*bucketSort(arr))
    
    arr = [0, 0.1, 0.5, 1, 0.33, 0.5, 0.5555, 0.999999, 0.1234, 0.768, 0.785, 0.8888, 0.8524, 0.325, 0.578]
    print(*bucketSort(arr))

    # arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    # print(*bucketSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*bucketSort(arr))