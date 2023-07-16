"""
use quick select algorithm to find the optimal location, sum distances and elapsed time.
file name: select_median.py
author: Chen Lin
"""
import time
import store_location
import tools


def quick_select(lst, k):
    """
    a quick select algorithm
    :param lst: a list of numbers
    :param k: kth smallest number
    precondition: k in range (0, len(lst)-1)
    """
    smaller_list = []
    larger_list = []
    count = 0
    if lst != []:
        pivot = lst[(len(lst) // 2)]
        for e in lst:
            if e < pivot:
                smaller_list.append(e)
            elif e > pivot:
                larger_list.append(e)
            else:
                count += 1
        m = len(smaller_list)
        if k >= m and k < (m + count):
            return pivot
        if m > k:
            return quick_select(smaller_list, k)
        else:
            return quick_select(larger_list, k - m - count)


def optimal_location(lst):
    """
    a function to find optimal_location using midpoint strategy
    calculate the optimal location
    :param lst: a list
    """
    if len(lst) % 2 != 0:
        return quick_select(lst, len(lst) // 2)
    else:
        x = quick_select(lst, len(lst) // 2)
        y = quick_select(lst, len(lst) // 2 - 1)
        return (x + y) / 2


def main():
    """
    prompt the file name and calculate and print the store location, sum of distances and elapsed time
    """
    file = input("Enter file name:")
    lst = tools.read_file(file)

    start = time.perf_counter()
    print("optimum new store location: ", store_location.optimal_location(lst))
    print("sum of distances to the new store: ", tools.sum_distance(lst, optimal_location(lst)))
    elapsed = time.perf_counter() - start
    print("elapsed time :", elapsed)


if __name__ == '__main__':
    main()
