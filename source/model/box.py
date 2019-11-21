#! /usr/bin/env python3
# coding: utf-8
"""Class Box from model"""


class Box:
    """Define structure of labyrinth"""

    def __init__(self, north=False, south=False, east=False, west=False):

        self.north = north
        self.south = south
        self.east = east
        self.west = west

        self.content = None

    @property
    def is_valid(self):
        """Return True if box is accessible and empty"""
        # Check if box is accessible and empty
        return any([self.north, self.south, self.east, self.west]) and self.content is None

    def get_direction(self, direction):
        """Take a direction (string) and return direction's accessibility (Boolean)"""
        return getattr(self, direction)
