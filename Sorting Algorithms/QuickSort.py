def quickSort(arr, indL, indR):
    """
    Sorts the given sequence
    
    - Parameters:
        - arr: Iterable in which is to be sorted
        - indL: Index of left-most element
        - indR: Index of right-most element
    - Returns:
        - Sorted sequence: Passed iterable is sorted in place, but also returns a sorted array
        - Unsorted sequence: If exception occurs during sorting
    - Time:
        - O(n.log2(n)) - Average
        - O(n^2) - Worst
    - Space:
        - O(1)
    - Stability:
        Not Stable
    - Use case:
        - One of the fastest algorithms without much auxiliary space
    """
    if indL < indR:
        p = partition(arr, indL, indR)
        quickSort(arr, indL, p-1)
        quickSort(arr, p+1, indR)
    return arr

def partition(arr, indL, indR):     # Finds pivot position to swap with right-most element
    pvt_ind = indL
    pvt = arr[pvt_ind]

    while indL < indR:
        try:
            while indL < len(arr) and arr[indL] <= pvt:     # Find element greater than pivot on LHS
                indL += 1
            while arr[indR] > pvt:      # Find element smaller than pivot on RHS
                indR -= 1
        except Exception as exp:
            print("The following error occured: {}".format(*exp.args))
            raise Exception("Could not find partition index")

        if indR > indL:     # If indexes have not crossed yet, means we have to swap
            arr[indL], arr[indR] = arr[indR], arr[indL]
    arr[indR], arr[pvt_ind] = arr[pvt_ind], arr[indR]       # Swapping right-most element with element at pivot

    return indR


# Test
if __name__ == "__main__":
    arr = [2,1,4,5,52,5,6,8,9,9,2,-34,-44,-0,0]
    print(*quickSort(arr, 0, len(arr)-1))

    arr = ['defdef', 'abcabc', 'xyzxyz', 'abcaaa','a']
    print(*quickSort(arr, 0, len(arr)-1))

    # Exception Test
    # Uncomment the lines below to test the exception block
    # arr = [123, 'a', 'abcabcabc', '', True]
    # print(*quickSort(arr, 0, len(arr)-1))