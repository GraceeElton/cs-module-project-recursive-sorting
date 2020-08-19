# TO-DO: complete the helper function below to merge 2 sorted arrays
arrA = [1, 2, 3, 4, 5]
arrB = [6, 7, 8, 9, 10]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    if arrB[0] < arrB[0]:
        merged_arr.append(arrB[0])
    else:
        merge(arrA[0] + 1, arrB[0] + 1)

    return print(merged_arr, "this is the merged arrary")

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

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
