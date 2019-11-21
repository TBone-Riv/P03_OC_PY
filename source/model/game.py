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
        list_actor = list_item.append(Guardian("guardian", list_item))

    def set_actor_on_labyrinth(self, list_actor):
        pass

    def set_player_position(self):
        pass

    def set_win_condition(self):
        pass
