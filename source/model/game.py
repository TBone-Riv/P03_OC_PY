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

    def set_actor_on_labyrinth(self, list_actor):
        """Take a list of actor and put them in a random box"""
        for actor in list_actor:
            self.labyrinth.set_box_content(*self.labyrinth.get_valid_box(), actor)

    def set_player_position(self):
        pass

    def set_win_condition(self):
        pass
