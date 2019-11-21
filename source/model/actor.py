#! /usr/bin/env python3
# coding: utf-8
"""Class Actor from model"""


class ActorMixin:
    """Mixin class for all actor-like object"""

    def __init__(self, name: str):
        self.name = name

    def event(self, game):
        """Need to be overridden to call different Player methods"""
        raise NotImplementedError()


class Item(ActorMixin):
    """Collectible item"""

    def event(self, game):
        game.player.append(self)
        game.labyrinth.emptying_box(*game.player.get_position())


class Guardian(ActorMixin):
    """Actor handling win condition"""

    def __init__(self, name: str, list_item: list):
        super().__init__(name)
        self.list_item = list_item

    def event(self, game):
        game.set_win_condition(self.list_item)
