def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        # If you can swap it, you swap it
        # That is, if you can swap the elements at indices i and j, you swap them
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # i + 1 is the index after the last swap
    # (Substitute low - 1 + n for i where n is the number of swaps we performed)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
