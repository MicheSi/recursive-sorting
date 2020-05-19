# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # put back together here
    # assign new arrays
    a = 0
    b = 0
    
    for c in range(0, elements):
        # compare a & b
        # if a is out of range, push b and iterate
        if a >= len(arrA): # going through a
            # push b
            merged_arr[c] = arrB[b]
            b += 1
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[c] = arrA[a]
            a += 1
        # if a is smaller, put it in array and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        # if b is smaller, put in arr and iterate both
        else:
            merged_arr[c] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # split array here
    # base case - arr > 1
    if len(arr) > 1:
        # find middle of arr
        # sort left & add items in left to left
        mid = len(arr) // 2
        left = merge_sort(arr[0:mid]) # takes arr and splits left half into left
        # sort right & add items in right to right
        right = merge_sort(arr[mid:]) # takes arr and puts right half into right
        # merge left and right
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
