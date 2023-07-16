"""
write a function that combined merge_sort and quick_sort to sort a list
file name: merge_quick_sort.py
author: Chen Lin
"""

import merge_sort
import quick_sort


def merge_quick_sort(L):
    """
    combine merge sort and quick sort function
    : param: L: a list
    """
    if L == []:
        if L == []:
            return []
        elif len(L) == 1:
            return L
        else:
            left, right = merge_sort.split(L)
            return merge_sort.merge(merge_sort(left), merge_quick_sort(right))

    if L == []:
        return []
    else:
        pivot = L[0]
        less, same, more = quick_sort.partition(pivot, L)
        return quick_sort.quick_sort(less) + same + quick_sort.quick_sort(more)







