# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # create a middle
    middle = (start + end) // 2
    # check if the target is above or below the middle

    if len(arr) == 0:
        return -1  # array empty
    elif start > end:
        return -1  # not found
    elif arr[middle] == target:
        return middle
    else:
        if target < arr[middle]:
            end = middle-1  # eliminate RHS
        else:
            start = middle+1  # eliminate LHS
    return binary_search(arr, target, start, end)

    # STRETCH: implement an order-
    # agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
