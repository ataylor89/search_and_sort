from sort import quicksort, simplesort
from time import perf_counter
from random import randint

def test(r, a, b, n, qs=True, ss=True, show=False, newline=False):
    print('Round %d (a=%d b=%d n=%d)' %(r, a, b, n))
    a, b, n = int(a), int(b), int(n)
    arr = [randint(a, b) for i in range(n)]
    if show:
        print('Unsorted list: %s' %arr)
    if qs:
        arr1 = arr.copy()
        start_time = perf_counter()
        quicksort(arr1, 0, len(arr1) - 1)
        quicksort_time = perf_counter() - start_time
        if show:
            print('Quicksort result: %s' %arr1)
        print(f'Quicksort execution time: {quicksort_time:.6f} seconds')
    if ss:
        arr2 = arr.copy()
        start_time = perf_counter()
        simplesort(arr2)
        simplesort_time = perf_counter() - start_time
        if show:
            print('Simplesort result: %s' %arr2)
        print(f'Simplesort execution time: {simplesort_time:.6f} seconds')
    if newline:
        print('')

if __name__ == '__main__':
    test(1, 0, 20, 20, show=True, newline=True)
    test(2, 0, 100, 100, newline=True)
    test(3, 0, 1000, 1000, newline=True)
    test(4, 0, 1e4, 1e4, newline=True)
    test(5, 0, 2e4, 2e4, newline=True)
    test(6, 0, 1e5, 1e5, ss=False)
