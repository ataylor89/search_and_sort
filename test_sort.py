from sort import quicksort, simplesort
from time import perf_counter
from random import randint

def test(r, a, b, n, qs=True, ss=True, sl=False, nl=False):
    print('Round %d (a=%d b=%d n=%d)' %(r, a, b, n))
    a, b, n = int(a), int(b), int(n)
    arr = [randint(a, b) for i in range(n)]
    if sl:
        print('Unsorted list: %s' %arr)
    if qs:
        arr1 = arr.copy()
        start_time = perf_counter()
        quicksort(arr1, 0, len(arr1) - 1)
        quicksort_time = perf_counter() - start_time
        if sl:
            print('Quicksort result: %s' %arr1)
        print(f'Quicksort execution time: {quicksort_time:.6f} seconds')
    if ss:
        arr2 = arr.copy()
        start_time = perf_counter()
        simplesort(arr2)
        simplesort_time = perf_counter() - start_time
        if sl:
            print('Simplesort result: %s' %arr2)
        print(f'Simplesort execution time: {simplesort_time:.6f} seconds')
    if qs and ss:
        assert arr1 == arr2
    if nl:
        print('')

if __name__ == '__main__':
    test(1, 0, 20, 20, sl=True, nl=True)
    test(2, 0, 100, 100, nl=True)
    test(3, 0, 1000, 1000, nl=True)
    test(4, 0, 1e4, 1e4, nl=True)
    test(5, 0, 2e4, 2e4, nl=True)
    test(6, 0, 3e4, 3e4, nl=True)
    test(7, 0, 4e4, 4e4, nl=True)
    test(8, 0, 5e4, 5e4, nl=True)
    test(9, 0, 1e5, 1e5, ss=False, nl=True)
    test(10, 0, 1e6, 1e6, ss=False)
