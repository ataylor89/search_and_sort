# How can we remember the quicksort implementation?
#
# How can we produce it on demand many months or many years after we learn it?
#
# I think we have to remember several key ideas
#
# First, we partition the array into a left subarray, a pivot, and a right subarray,
# where every element in the left subarray is less than or equal to the pivot,
# and every element in the right subarray is greater than the pivot,
# and we do this over and over again, recursively
#
# Second, we use variables i and j for swapping
#
# Third, we initialize variable i to low - 1
#
# Fourth, j is the loop variable, and we loop from low to high
#
# Fifth, we increment i before every swap

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
    # and our pivot is stored at index i + 1
    return i + 1
