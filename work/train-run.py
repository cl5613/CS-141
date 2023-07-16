"""
run commands to make train work
file name: train-run.py
author: Chen Lin
"""
from dataclasses import dataclass
from typing import Union, Dict
from node_types import MutableNode
import commands

@dataclass()
class TrainCar:
    contents: str
    stations: str

@dataclass()
class Train:
    speed: float
    head: Union[MutableNode, None]
    route: Dict[str, float]

@dataclass()
class Station:
    name: str
    distance: float


def process_commands():
    """
    process each commands for the train
    """
    while True:
        command_line = input('Enter command:').split()
        command = command_line[0]
        if command == 'help':
            commands.help()

        elif command == 'add_station':
            commands.add_station(command_line[1], command_line[2])

        elif command == 'add_car':
            commands.add_car(command_line[1], command_line[2])

        elif command == 'set_speed':
            commands.set_speed(command_line[1])

        elif command == 'show_train':
            commands.show_train()

        elif command == 'show_route':
            commands.show_route()

        elif command == 'start':
            commands.start()

        elif command == 'quit':
            result = commands.quit()
            break

        else:
            print('Illegal command name.')

    if result is False:
        print('Illegal use or form for this command.')


def main():
    """
    main function that enables user to enter commands and print results.
    """
    print('Welcome to train yard.\
        \nList of commands:\
        \nset_speed, <speed>\
        \nadd_station <station> <distance>\
        \nadd_car <contents> <station>\
        \nshow_route\
        \nshow_train\
        \nstart\
        \nquit')

    process_commands()


if __name__ == '__main__':
    main()
