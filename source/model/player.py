#! /usr/bin/env python3
# coding: utf-8
"""Class Player from model"""


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
        self.labyrinth.matrix[self.box_position[0]][self.box_position[1]].content = None

    def move_to(self, direction):
        """Handle player movement"""
        if self.labyrinth.valid_move(self.box_position, direction):
            if direction == 'north':
                self.box_position[0] += -1
            elif direction == 'south':
                self.box_position[0] += 1
            elif direction == 'east':
                self.box_position[1] += 1
            else:
                self.box_position[1] += -1

        # Call "Box.event" method if exist
        self.labyrinth.event(self, self.box_position)
