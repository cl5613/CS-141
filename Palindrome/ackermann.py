"""
Write an ack function and a main function to test ackermann function
filename: ackermann.py
author: Chen Lin
"""


def ack(m, n):
    """
    This is an ackermann function
    :param m: non-negative integer
    :param n: non-negative integer
    :return: m and n must be positive to return some ack numbers
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


def main():
    """
    A main function to test ackermann function by entering m and n where both are positive integers.
    """
    m: int = int(input('Enter m: '))
    n: int = int(input('Enter n: '))

    if m < 0 or n < 0:
        print('m and n must all be integers')
    else:
        print('ack(', m, ',', n, ') =', ack(m, n))


if __name__ == '__main__':
    main()
