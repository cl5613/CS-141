"""
sort items into three boxes with same weights
file name: moving.py
author: Chen Lin
"""
from dataclasses import dataclass


@dataclass()
class Box:
    remaining_capacity: int
    total_capacity: int
    lst: list


@dataclass()
class Item:
    name: str
    weight: int

def make_box(i):
    return Box(i, i, [])

def make_items(lst):
    return Item(lst[0], int(lst[1]))


def read_file():
    """
    prompt the user to enter a file name and sort the items reversely
    """
    lst = []
    filename = input('Enter file name: ')
    with open(filename) as fd:
        boxes = fd.readline()
        boxes = boxes.strip().split()
        i = 0
        for item in fd:
            item = item.strip().split()
            lst.append(make_items(item))
        lst = sorted(lst, key=lambda items: items.weight, reverse=True)
        for capacity in boxes:
            boxes[i] = make_box(int(capacity))
            i += 1
    return boxes, lst


def strategy1(boxes, items):
    """
    implementation of strategy 1
    :param boxes: box capacity
    :param items: items
    """
    print('Results from greedy strategy 1')
    leftovers = []
    for item in items:
        max_box = None
        for box in boxes:
            if max_box is None or box.remaining_capacity > max_box.remaining_capacity:
                max_box = box
        if max_box.remaining_capacity >= item.weight:
            max_box.lst.append(item)
        else:
            leftovers.append(item)
    count = 1
    for box in boxes:
        print("box", count, "of weight capacity", box.total_capacity)
        for item in box.lst:
            print(item.name, 'of weight', item.weight)


def strategy2(boxes, items):
    """
    implementation of strategy 2
    :param boxes: box capacity
    :param items: items
    """
    print('Results from greedy strategy 2')
    leftovers = []
    for item in items:
        min_box = None
        for box in boxes:
            if min_box is None or box.remaining_capacity < min_box.remaining_capacity:
                min_box = box
        if min_box.remaining_capacity <= item.weight:
            min_box.lst.append(item)
        else:
            leftovers.append(item)
    count = 1
    for box in boxes:
        print("box", count, "of weight capacity", box.total_capacity)
        for item in box.lst:
            print(item.name, 'of weight', item.weight)


