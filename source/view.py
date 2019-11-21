#! /usr/bin/env python3
# coding: utf-8
"""View module"""


import pygame
import source.constants as const


class Player:
    """Format blit argument to handel player position"""

    def __init__(self, line, column):
        self.x = column * const.DIMENSION_SPRITE
        self.y = line * const.DIMENSION_SPRITE

    def blit(self):
        return pygame.image.load(const.RESOURCE_PATH + "player.png").\
                   convert_alpha(), (self.x, self.y)


class Box(pygame.Surface):
    """Build one surface for all visual component from a box"""

    def __init__(self, box):
        super().__init__((const.DIMENSION_SPRITE, const.DIMENSION_SPRITE))

        image_wall = \
            pygame.image.load(const.RESOURCE_PATH + "wall.png").convert_alpha()

        self.blit(pygame.image.load(const.RESOURCE_PATH + "ground.png").
                  convert_alpha(), (0, 0))
        for wall in [box.north, box.west, box.south, box.east]:
            if not wall:
                self.blit(image_wall, (0, 0))

            # Rotate wall image for next iteration
            # to use only one image for all wall
            image_wall = pygame.transform.rotate(image_wall, 90).\
                convert_alpha()

        if box.content is not None:
            self.blit(pygame.image.load(const.RESOURCE_PATH +
                                        box.content.name + '.png').
                      convert_alpha(), (0, 0))


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
