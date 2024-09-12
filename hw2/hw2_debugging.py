''' Following module has two functions-
1. mergrSort(arr): Takes an array as an input performs merge sort.
2. recombine(left_array, right_array): Merges both arrays in a sorted manner'''


import rand


def merge_sort(arr_func):
    '''Performs recursive merge sort to the input array'''
    if len(arr_func) == 1:
        return arr_func

    half = len(arr_func) // 2

    return recombine(merge_sort(arr_func[:half]), merge_sort(arr_func[half:]))


def recombine(left_arr, right_arr):
    ''' The current function merges both arrays in a sorted manner '''

    left_index = 0
    right_index = 0
    merge_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1

        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr

array = rand.random_array([None] * 20)
arr_out = merge_sort(array)

print(arr_out)
