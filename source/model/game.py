#! /usr/bin/env python3
# coding: utf-8
"""Class Game from model"""


from source.model.player import Player
from source.model.labyrinth import Labyrinth
from source.model.actor import Item, Guardian


LIST_ITEM = ['item1', 'item2', 'item3']


class Game:
    """Build all object and handle their interaction"""

    def __init__(self):

        self.player = Player()
        self.labyrinth = Labyrinth()

        list_item = [Item(i) for i in LIST_ITEM]
        list_actor = list_item + [Guardian("guardian", list_item)]

        self.set_actor_on_labyrinth(list_actor)
        self.player.set_random_position(self.labyrinth)

        self.win_condition = None

    def set_actor_on_labyrinth(self, list_actor):
        """Take a list of actor and put them in a random box"""
        for actor in list_actor:
            self.labyrinth.\
                set_box_content(*self.labyrinth.get_valid_box(), actor)

    def set_player_position(self, direction):
        """Handle player movement"""
        if self.labyrinth.get_valid_move(self.player.coordinate_line,
                                         self.player.coordinate_column,
                                         direction):
            self.player.set_move(direction)

        # Call "Box.event" method if exist
        self.labyrinth.call_event(self)

    def set_win_condition(self, list_item):
        """Check win condition"""
        # Check if itch guardian list element are in player list
        self.win_condition = \
            bool(all([item in self.player for item in list_item]))
