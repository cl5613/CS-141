"""
Write a main function to compare merge_quick_sort to merge_sort and quick_sort
file name: compare_sorts.py
author: Chen Lin
"""
import time
import quick_sort
import merge_sort
import merge_quick_sort
import random
import sys


def main():
    """
    a main function to compare merge_quick_sort to merge_sort and quick_sort
    """
    N = int(input("list size: "))
    if N < 0:
        print('Error: N must be positive integers')
        return None
    else:
        pass

    if N + 10 > sys.getrecursionlimit():
        sys.setrecursionlimit(N + 10)

    for num in (0, N - 1):
        lst = []
        for i in range(num):
            lst.append(i)

    start = time.perf_counter()
    quick_sort.quick_sort(lst)
    elapsed = time.perf_counter() - start
    print('quick_sort (sorted) elapsed time:', elapsed * 1000, 'msec')

    start = time.perf_counter()
    merge_sort.merge_sort(lst)
    elapsed = time.perf_counter() - start
    print('merge_sort (sorted) elapsed time:', elapsed * 1000, 'msec')

    start = time.perf_counter()
    merge_quick_sort.merge_quick_sort(lst)
    elapsed = time.perf_counter() - start
    print('merge_quick_sort (sorted) elapsed time:', elapsed * 1000, 'msec')

    random.shuffle(lst)

    start = time.perf_counter()
    quick_sort.quick_sort(lst)
    elapsed = time.perf_counter() - start
    print('quick_sort (random) elapsed time:', elapsed * 1000, 'msec')

    start = time.perf_counter()
    merge_sort.merge_sort(lst)
    elapsed = time.perf_counter() - start
    print('merge_sort (random) elapsed time:', elapsed * 1000, 'msec')

    start = time.perf_counter()
    merge_quick_sort.merge_quick_sort(lst)
    elapsed = time.perf_counter() - start
    print('merge_quick_sort (random) elapsed time:', elapsed * 1000, 'msec')


if __name__ == '__main__':
    main()
