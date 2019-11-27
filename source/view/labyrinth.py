#! /usr/bin/env python3
# coding: utf-8
"""View module"""


import pygame
import source.constants as const
from source.view.box import Box


class Labyrinth(pygame.Surface):
    """Build one surface with all box sprite"""

    def __init__(self, labyrinth):
        super().__init__((const.DIMENSION_LABYRINTH,
                          const.DIMENSION_LABYRINTH))
        x, y = 0, 0

        for line_box in labyrinth.matrix:
            for box in line_box:
                self.blit(Box(box), (0 + x, 0 + y))
                x += const.DIMENSION_SPRITE
            x = 0
            y += const.DIMENSION_SPRITE