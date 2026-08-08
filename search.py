# Notes
# ------
#
# The binarysearch method is an implementation of the binary search algorithm that uses iteration (loops)
# The rbinarysearch method is an implementation of the binary search algorithm that uses recursion
#
# One way to repeat code is to use loops (for loops, while loops, for-each loops, etc) and we call this iteration
# Another way to repeat code is for a function to call itself, and we call this recursion
#
# I wanted to include both an iterative and a recursive implementation of binary search,
# because it helps us understand the difference between iteration and recursion
#
# Binary search is one of those algorithms that can be easily written using either iteration or recursion
#
# I also included a linear search method, because I wanted to compare the performance of linear search and binary search
#
# It's important to keep in mind that the binary search implementations accept a sorted list as their input
# The linear search implementation, on the other hand, can accept a sorted or unsorted list as its input
#
# I wanted to know what is the most efficient algorithm for searching a sorted list
# So I researched the question...
#
# After doing some research, I concluded that binary search is one of the most efficient algorithms for searching a sorted list

def binarysearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def rbinarysearch(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return rbinarysearch(arr, target, mid + 1, high)
    else:
        return rbinarysearch(arr, target, low, mid - 1)

def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
