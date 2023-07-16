"""
find the store location given the lists
file name: store_location.py
author: Chen Lin
"""
import tools
import quick_sort
import time


def optimal_location(lst):
    """
    a function to find optimal_location using midpoint strategy
    calculate the optimal location
    :param lst: a list
    """
    lst = quick_sort.quick_sort(lst)
    if len(lst) % 2 != 0:
        return lst[len(lst) // 2]
    else:
        x = lst[len(lst)//2]
        y = lst[len(lst)//2 - 1]
        return (x + y) / 2


def main():
    """
    prompt the file name and print the store location and sum of distances
    """
    file = input("Enter file name:")
    lst = tools.read_file(file)

    start = time.perf_counter()
    print("optimum new store location: ", optimal_location(lst))
    print("sum of distances to the new store: ", tools.sum_distance(lst, optimal_location(lst)))
    elapsed = time.perf_counter() - start
    print("elapsed time :", elapsed)


if __name__ == '__main__' :
    main()