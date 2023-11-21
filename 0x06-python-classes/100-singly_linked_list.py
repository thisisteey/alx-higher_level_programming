#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list by:"""


class Node:
    """A singly-linked list node represented"""
    def __init__(self, data, next_node=None):
        """initializes the node class
        Args:
        data (int): data of the node
        next_node (Node): the next node of the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets and returns the current data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets the node data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets and returns the next node of the node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the next node of the node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly-linked list represented"""
    def __init__(self):
        """initializes a singlylinkedlist"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node to the singlylinked list at the
        correct ordered index position
        Args:
        value (Node): the node to insert"""
        nnode = Node(value)
        if self.__head is None:
            nnode.next_node = None
            self.__head = nnode
        elif self.__head.data > value:
            nnode.next_node = self.__head
            self.__head = nnode
        else:
            tmpnode = self.__head
            while (tmpnode.next_node is not None and
                    tmpnode.next_node.data < value):
                tmpnode = tmpnode.next_node
            nnode.next_node = tmpnode.next_node
            tmpnode.next_node = nnode

    def __str__(self):
        """returns a string representation of the singlylinkedlist"""
        values = []
        tmpnode = self.__head
        while tmpnode is not None:
            values.append(str(tmpnode.data))
            tmpnode = tmpnode.next_node
        return ('\n'.join(values))
