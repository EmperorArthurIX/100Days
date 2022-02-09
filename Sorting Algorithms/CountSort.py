def countSort(arr):
    """
    Sorts the given sequence of non-negative integers
    
    - Parameters:
        - arr: Iterable in which is to be sorted
    - Returns:
        - None: If 'arr' is None or Empty
        - Sorted sequence: Passed iterable is sorted by reference, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n)
    - Space:
        O(k)
            - k is the size of the range of values
            - k == (max(arr) - min(arr))
    - Stability:
        Stable
            - Stability can be ensured in dictionary like structures by making a second counts array
            - Counts array can be made like: counts[i] = counts[i] + counts[i-1]
            - Read more [here](https://stackoverflow.com/questions/2572195/how-is-counting-sort-a-stable-sort#:~:text=the%20counts%20array%3A-,counts%20array,-%3A%20%5B0%2C%202%2C%202)
    - Use case:
        - Few Unique Values like age of students in a school
        - Integers in small range like 0 to 100
        - Numerically representable data, like alphabets
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
    
    lo = min(arr)
    hi = max(arr)
    try:
        size = hi-lo
    except Exception as exp:
        print("The following error occured: {}".format(*exp.args))
        return arr      # Prints error message and returns iterable in current state
    
    # Make Result array of size of range of numbers, initialise frequency counts to zero
    freqs = [-1]*size

    # Count the frequency of each number in the array
    for i in arr:
        try:
            freqs[i%size] += 1
        except TypeError as exp:
            print("The following error occured: {}".format(*exp.args))
            return arr      # Prints error message and returns iterable in current state
    
    for i in range(1, len(freqs)):
        for j in range(freqs[i]):
            arr[j] = i
    
    return arr


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,34,44,0,0]
    print(*countSort(arr))

    # arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    # print(*countSort(arr))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*countSort(arr))