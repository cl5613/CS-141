"""
a file to read the files and calculate the sum distances
file name: tools.py
author:Chen Lin
"""


def read_file(file):
    """
    read file function to read a file and print a list of numbers
    :param file: a file name
    """
    with open(file) as f:
        lst = []
        for line in f:
            lst.append(int(line.split()[1]))
        return lst


def sum_distance(lst, optimal_location):
    """
    calculate sum of distances
    :param lst: a list
    :param optimal_location: the optimal location
    :return: result: the expected sum distance
    """
    result = 0
    for numbers in lst:
        result += abs(numbers - optimal_location)
    return result
