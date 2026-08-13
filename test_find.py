from find import quickselect
from sort import quicksort
from time import perf_counter
from random import randint

def test(r, a, b, n, sl=False, nl=False):
    print('Round %d (a=%d b=%d n=%d)' %(r, a, b, n))
    a, b, n = int(a), int(b), int(n)
    arr = [randint(a, b) for i in range(n)]
    if sl:
        print('Unsorted list: %s' %arr)
    cpy1, cpy2 = arr.copy(), arr.copy()
    low, high = 0, len(arr) - 1
    start_time = perf_counter()
    median1 = quickselect(cpy1, n // 2, low, high)
    time1 = perf_counter() - start_time
    print(f'Quickselect result. Median: {median1} Time elapsed: {time1:.6f} seconds')
    start_time = perf_counter()
    quicksort(cpy2, low, high)
    median2 = cpy2[n // 2]
    time2 = perf_counter() - start_time
    print(f'Quicksort result. Median: {median2} Time elapsed: {time2:.6f} seconds')
    assert median1 == median2, 'The results from quickselect and quicksort do not match'
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
    test(9, 0, 1e5, 1e5, nl=True)
    test(10, 0, 1e6, 1e6)
