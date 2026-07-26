from sort import quicksort
from search import linear_search
from search import iterative_binary_search
from search import recursive_binary_search

def test(arr, target):
    result1 = linear_search(arr, target)
    result2 = iterative_binary_search(arr, target)
    result3 = recursive_binary_search(arr, target, 0, len(arr) - 1)
    if result1 >= 0 and result1 == result2 == result3:
        print('Target value %d was found in the array at index %d' %(target, result1))
    else:
        print('Target value %d was not found in the array (res1 = %d, res2 = %d, res3 = %d)' %(target, result1, result2, result3))

if __name__ == '__main__':
    # Let's do some tests
    arr = [1, 8, 6, 3, 5, 9, 0, 2, 4, 5, 9, 11, 12, 14, 10]
    print('Unsorted list: %s' %arr)
    quicksort(arr, 0, len(arr) - 1)
    print('Sorted list: %s' %arr)
    test(arr, 0)
    test(arr, 1)
    test(arr, 6)
    test(arr, 12)
    test(arr, 14)
    test(arr, 15)
    test(arr, 16)
