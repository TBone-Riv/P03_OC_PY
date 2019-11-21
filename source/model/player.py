#! /usr/bin/env python3
# coding: utf-8
"""Class Player from model"""


from source.model.actor import Item


class Player:
    """Core object from model"""

    def __init__(self):
        # Position
        self.coordinate_line = 0
        self.coordinate_column = 0

        # Variable iterable related
        self.list_item = []
        self.index = 0

        # Win condition
        self.is_win = None

    # Iterable related method
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            result = self.list_item[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def set_position(self, line, column):
        """Set player position"""
        self.coordinate_line, self.coordinate_column = line, column

    def set_random_position(self, labyrinth):
        """Set random position"""
        self.set_position(*labyrinth.get_valid_box())

    def append(self, item):
        """Add object to iterable variable and remove it from labyrinth"""
        # Confirm that method is call by an Item
        if not isinstance(item, Item):
            raise TypeError("item is not of type 'Item'")

        # Adding item to the list and remove it from the matrix
        self.list_item.append(item)
