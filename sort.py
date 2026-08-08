# How can we remember the implementation of the quicksort algorithm?
#
# How can we produce it on demand many months or many years after we learn it?
#
# I think it helps to remember several key ideas
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
# Fourth, j is the loop variable, and we loop from low to high - 1,
# which is equivalent to range(low, high) in Python,
# and the reason we use high - 1 is that arr[high] is initially our pivot
#
# Fifth, we increment i before every swap
#
# Sixth, the quicksort method is recursive,
# and the base case for terminating the recursion is low >= high
# (Alternatively, the recursive case is low < high)

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high + 1):
        # If you can swap it, you swap it
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Now, every element from index low to index i - 1 is less than or equal to our pivot,
    # every element from index i + 1 to index high is greater than our pivot,
    # and our pivot is stored at index i
    return i

# We are going to include a simpler, less efficient sorting algorithm for comparison
def simplesort(arr):
    for i in range(len(arr)):
        target = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[target]:
                target = j
        arr[i], arr[target] = arr[target], arr[i]
