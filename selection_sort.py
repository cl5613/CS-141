"""
Write a program to open, read and sort that file
1. The test case in insertion-sort doesn't need a lot of work to complete sorting.
2. selection_sort performs worse than insertion_sort because selection_sort needs to take many swaps to
sort but insertion_sort take no swap to sort.
file: selection_sort.py
author: Chen Lin
"""


def swap(lst, i, j):
    """
    swap the contents of list at pos i and j.
    :param lst - the list of data
    :param i: index of one data
    :param j: index of another data
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def find_min_from(lst, mark):
    """
    Move value at index mark+1 so that it is in its proper place.
    :param lst: the list of data
    :param mark: represents cutting the list between index mark and index mark+1
    """
    while mark > -1 and lst[mark] > lst[mark + 1]:
        swap(lst, mark, mark + 1)
        mark = mark - 1


def selection_sort(lst):
    """
    a function to sort data
    :param lst: the list of data
    """
    for mark in range(len(lst) - 1):
        find_min_from(lst, mark)


def main():
    """
    main function will prompt the user to open, read and store a file and sort numbers in that file
    precondition: the data isn't sorted
    post-condition: the data is sorted
    """
    file = input("Enter file name:")
    file = open(file)
    data = []
    for line in file:
        data = data + [int(line)]
    print(data)
    file.close()

    selection_sort(data)
    print(data)


if __name__ == '__main__':
    main()
