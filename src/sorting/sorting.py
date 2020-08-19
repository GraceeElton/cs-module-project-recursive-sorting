# TO-DO: complete the helper function below to merge 2 sorted arrays
arrA = [1, 2, 3, 4, 5]
arrB = [6, 7, 8, 9, 10]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    arrA_idx = 0
    arrB_idx = 0

    # loop over the merged_arr
    for idx in range(elements):
        # check if we are at the end of one of the arrays
        # if so, just use other array
        if arrA_idx >= len(arrA):
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1
        elif arrB_idx >= len(arrB):
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1

         # compare the first element of each array
        #  smaller element goes into merged array
        elif arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1
        else:
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1

    return merged_arr

    # compare first element of each array
    # the smalled one goes into merge array

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        midpoint = len(arr) // 2
        # recurse on the right
        left = merge_sort(arr[:midpoint])
        # and left halves
        right = merge_sort(arr[midpoint:])
        # put things back together
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass


# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass
