# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        guess = arr[middle]
        if guess == target:
            return middle

        else:
            binary_search(len(arr)-1, target, start, end)

    return -1

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
