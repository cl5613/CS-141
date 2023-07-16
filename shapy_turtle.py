"""
interpret and process the commands
file: shapy_turtle.py
author: Chen Lin
"""
from turtle import *


def first_non_numeric(s):
    """
    :param s: a string
    :return: the index of the first non-numeric characters
    """
    for i in range(len(s)):
        if s[i] < '1' or s[i] > '9':
            return i
    return None


def process_string(s):
    """
    process a string
    :param s: a string
    """
    for i in range(len(s)):
        if not s[i].isdigit():
            return True
        else:
            return False


def interpret_command(s):
    """
    interpret commands
    :param s: a string
    """
    global color
    while s != " ":

        if s[0] == '<':
            left(int(s[1]))

        if s[0] == '>':
            right(int(s[1]))

        if s[0] == 'S':
            forward(int(s[1]))

        if s[0] == 'T':
            triangle(int(s[1]))

        if s[0] == 'C':
            circle(int(s[1]))

        if s[0] == 'F':
            forward(int(s[1]))

        if s[0] == 'B':
            backward(int(s[1]))

        if s[0] == 'U':
            penup()

        if s[0] == 'D':
            pendown()

        if s[0] == 'z':
            if s[1] == '0':
                color("red")
            elif s[1] == '1':
                color("blue")
            elif s[1] == '2':
                color("green")
            elif s[1] == '3':
                color("yellow")
            elif s[1] == '4':
                color("brown")
            elif '9' >= s[1] >= '5':
                color("black")


def main():
    """
    a main function will let the user to enter a string and process that
    no param
    """
    s = input('Please enter s: ')
    interpret_command(s)


if __name__ == '__main__':
    main()
