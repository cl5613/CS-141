"""
a list of commands
file name: commands.py
author: Chen Lin
"""
from dataclasses import dataclass
from typing import Union, Dict
from node_types import MutableNode


@dataclass()
class TrainCar:
    contents: str
    destinations: str


@dataclass()
class Train:
    speed: float
    head: Union[MutableNode, None]
    route: Dict[str, float]


@dataclass()
class Station:
    name: str
    distance: float


train = Train(0, None, {})

def empty_TrainCar(lst):
    """
    empty train car
    :param lst: a list
    """
    return TrainCar(lst[0], lst[1])


def help():
    """
    help command
    """
    print('List of commands:\
        \nset_speed, <speed>\
        \nadd_station <station> <distance>\
        \nadd_car <contents> <station>\
        \nshow_route\
        \nshow_train\
        \nstart\
        \nquit')

    return True


def add_station(station_name, distance):
    """
    add station to a station list using append
    :param station_name: station name
    :param distance: distance from the home station
    """
    lst = []
    new_station = Station(station_name, distance)
    lst.append(new_station)
    return True


def add_car(contents, destinations):
    """
    add cars in a list(linked list) using insert
    :param contents: content in the train
    :param destinations: destination name
    """
    train_car = TrainCar(contents, destinations)
    train_distance = train.route[destinations]
    node = train.head
    predecessor = None
    while train.route[node.value.destination] > train_distance:
        predecessor = node
        node = node.next
    predecessor.next = MutableNode(train_car, node)
    return True


def set_speed(speed):
    """
    set speed for the train
    :param speed: a list
    """
    if float(speed) > 0:
        train.speed = speed
    elif float(speed) < 0:
        return False
    return True


def show_train():
    """
    print contents of the train using to string
    """
    speed = train.speed
    train_speed = set_speed(speed)
    lst = []
    for content in TrainCar.contents:
        content = content.strip().split()
        lst.append(empty_TrainCar(content))

    for destination in TrainCar.destinations:
        destination = destination.strip().split()
        lst.append(empty_TrainCar(destination))

    print('engine', '(', train_speed, ')', '[', lst, ']')

    return True


def show_route():
    """
    show route in order
    """
    for key in train.route:
        print(key, '---', train.route[key], '-->', end="")
    return True


def start():
    """
    start the route
    """
    return True


def quit():
    """
    quit
    """
    print('Train yard simulation ending.')
    return True
