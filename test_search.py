from sort import quicksort
from search import linearsearch, binarysearch
from time import perf_counter
from random import randint

def test(r, a, b, n, ls=True, bs=True, sl=False, nl=False):
    print('Round %d (a=%d b=%d n=%d)' %(r, a, b, n))
    a, b, n = int(a), int(b), int(n)
    arr = [randint(a, b) for i in range(n)]
    target = randint(a, b)
    if sl:
        print('Unsorted list: %s' %arr)
    cpy = arr.copy()
    quicksort(arr, 0, len(arr) - 1)
    assert arr == sorted(cpy)
    if sl:
        print('Sorted list: %s' %arr)
    if ls:
        start_time = perf_counter()
        ls_result = linearsearch(arr, target)
        ls_time = perf_counter() - start_time
        if ls_result >= 0:
            print(f'Linear search: Found {target} at index {ls_result}. Search time: {ls_time:.6f} seconds.')
        else:
            print(f'Linear search: {target} not found. Search time: {ls_time:.6f} seconds.')
    if bs:
        start_time = perf_counter()
        bs_result = binarysearch(arr, target)
        bs_time = perf_counter() - start_time
        if bs_result >= 0:
            print(f'Binary search: Found {target} at index {bs_result}. Search time: {bs_time:.6f} seconds.')
        else:
            print(f'Binary search: {target} not found. Search time: {bs_time:.6f} seconds.')
    if ls and bs:
        assert (ls_result ^ bs_result) >= 0, f'ls_result={ls_result} and bs_result={bs_result} have different signs'
    if nl:
        print('')

if __name__ == '__main__':
    test(1, 0, 1000, 100, nl=True)
    test(2, 0, 1000, 1000, nl=True)
    test(3, 0, 1e4, 1000, nl=True)
    test(4, 0, 1e4, 1e4, nl=True)
    test(5, 0, 1e5, 1e4, nl=True)
    test(6, 0, 1e5, 1e5, nl=True)
    test(7, 0, 5e5, 5e4, nl=True)
    test(8, 0, 5e5, 5e5, nl=True)
    test(9, 0, 1e6, 1e5, nl=True)
    test(10, 0, 1e6, 1e6)
