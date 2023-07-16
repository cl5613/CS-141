"""
implement the immutable list recursively and the mutable list iteratively
file name: linked_lists.py
author: Chen Lin
"""
from node_types import FrozenNode, MutableNode
from linked_list_type import LinkedList


def size_of(head):
    """
    the size of the immutable list
    :param head: a FrozenNode
    :return: the size of the immutable list
    """
    if head is None:
        return 0
    else:
        return 1 + size_of(head.next)


def extend(head1, head2):
    """
    concatenating two immutable lists together into a new immutable list
    :param head1: first element in first immutable list
    :param head2: first element in second immutable list
    :return: the concatenated lists
    """
    if head1 is None and head2 is None:
        return None
    elif head1 is None:
        return head2
    elif head2 is None:
        return head1
    else:
        return FrozenNode(head1.value, extend(head1.next, head2))


def reverse(lst):
    """
    reverse a mutable list
    :param lst: a mutable list
    """
    if lst.head is not None and lst.size != 1:
        node = lst.head
        previous = None
        while node.next is not None:
            result = MutableNode(node.value, previous)
            previous = result
            node = node.next
        result = MutableNode(node.value, previous)
        lst.head = result


def remove_index(lst, index):
    """
    remove value in a mutable list by index
    :param lst: a mutable list
    :param index: the index of a list
    """
    node = lst.head
    if index == 0:
        lst.head = lst.head.next
        lst.size = lst.size - 1
    elif 0 > index or lst.size <= index:
        raise IndexError('Index Out of Bounds!')
    else:
        lst.size = lst.size - 1
        loc = 1
        while node is not None and loc < index:
            node = node.next
            loc += 1
        node.next = node.next.next


