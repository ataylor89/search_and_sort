# The find algorithm (also known as quickselect) is closely related to quicksort
# It finds the kth smallest element in an unsorted list
#
# It's actually faster to use the quickselect algorithm, than to use quicksort and return arr[k]
# This is because the list doesn't have to be fully sorted in order to retrieve the kth smallest element in the list
#
# The find algorithm can be used to find the median value in an unsorted list
# It can also be used to find quartiles

def quickselect(arr, k, low, high):
    i = partition(arr, low, high)
    if k == i:
        return arr[k]
    elif k < i:
        return quickselect(arr, k, low, i - 1)
    else:
        return quickselect(arr, k, i + 1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i
