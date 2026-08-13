def quickselect(arr, k, low, high):
    if low < high:
        i = partition(arr, low, high)
        if k == i:
            return arr[k]
        elif k < i:
            return quickselect(arr, k, low, i - 1)
        else:
            return quickselect(arr, k, i + 1, high)
    return arr[k]

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i
