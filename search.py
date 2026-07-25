def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def iterative_binary_search(arr, target):
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

def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)

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
    sorted_arr = sorted(arr)
    print('Sorted list: %s' %sorted_arr)
    test(sorted_arr, 0)
    test(sorted_arr, 1)
    test(sorted_arr, 6)
    test(sorted_arr, 12)
    test(sorted_arr, 14)
    test(sorted_arr, 15)
    test(sorted_arr, 16)
