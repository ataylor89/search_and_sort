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
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # i + 1 is the index after the last swap, if there was a swap
    # (Substitute low - 1 + n for i where n is the number of swaps we performed)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Now, every element from index low to index i is less than or equal to our pivot,
    # every element from index i + 2 to index high is greater than our pivot,
    # and our pivot is stored at index i + 1, creating the partition we want
    return i + 1
