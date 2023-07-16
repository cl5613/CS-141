"""
Use data structure queue to build droids
Filename: droid_factory.py
Author: Chen Lin
"""

from dataclasses import dataclass
import cs_queue


@dataclass(frozen=False)
class Droid:
    head: bool
    body: bool
    arms: bool
    legs: bool
    serial_number: int


def unload_droid_parts(filename):
    """
    a function to unload all of the droid parts from the file onto the belt.
    :param filename: name of a file to test
    :return: conveyor belt with parts in it
    """
    belt = cs_queue.make_empty_queue()
    with open(filename) as f:
        for line in f.readlines():
            cs_queue.enqueue(belt, line.strip())
    return belt


def build_a_droid(belt, serial_number):
    """
    building a droid
    :param belt: queue
    :param serial_number: serial number of the droid
    """
    Empty_Droid = Droid(False, False, False, False, serial_number)
    print('Building a new droid with serial number', serial_number)
    while Empty_Droid.head == False or Empty_Droid.body == False or Empty_Droid.arms == False or Empty_Droid.legs == False:
        part = cs_queue.dequeue(belt)
        if part == 'head':
            if Empty_Droid.head == False:
                Empty_Droid.head = True
                print('attaching', part, '....')
            elif Empty_Droid.head == True:
                cs_queue.enqueue(belt, part)
                print('placing unneeded part back on belt:', part)

        if part == 'body':
            if Empty_Droid.body == False:
                Empty_Droid.body = True
                print('attaching', part, '....')
            elif Empty_Droid.body == True:
                cs_queue.enqueue(belt, part)
                print('placing unneeded part back on belt:', part)

        if part == 'arms':
            if Empty_Droid.arms == False:
                Empty_Droid.arms = True
                print('attaching', part, '....')
            elif Empty_Droid.arms == True:
                cs_queue.enqueue(belt, part)
                print('placing unneeded part back on belt:', part)

        if part == 'legs':
            if Empty_Droid.legs == False:
                Empty_Droid.legs = True
                print('attaching', part, '....')
            elif Empty_Droid.legs == True:
                cs_queue.enqueue(belt, part)
                print('placing unneeded part back on belt:', part)

    print('Droid', serial_number, 'has been assembled')


def build_droids(belt):
    """
    a function to build multiple droids
    :param belt: queue
    """
    count = 10000
    while not cs_queue.is_empty(belt):
        build_a_droid(belt, count)
        count += 1

    print('All of the droids have been assembled! Time to clock out and play Sabacc..')


def main():
    """
    a main function to prompt the user for the name of the droid parts file and print droids
    """
    filename = input('Enter file name: ')
    print('Starting a shift at the droid factory!')
    belt = unload_droid_parts(filename)

    build_droids(belt)


if __name__ == '__main__':
    main()
