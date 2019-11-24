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

    @staticmethod
    def get_image():
        image = pygame.image.load(const.RESOURCE_PATH + "player.png")
        image = image.convert_alpha()
        image_width, image_height = image.get_size()
        back_dimension = max((image_height, image_width))
        background = pygame.Surface((back_dimension, back_dimension),
                                    pygame.SRCALPHA)
        difference = image_height - image_width
        blit_coordinate = (int(difference / 2) if difference > 0 else 0,
                           abs(int(difference / 2)) if difference < 0 else 0)
        background.blit(image, blit_coordinate)

        image = pygame.transform.scale(background, (int(const.DIMENSION_SPRITE / 2), int(const.DIMENSION_SPRITE / 2)))
        background = pygame.Surface((const.DIMENSION_SPRITE, const.DIMENSION_SPRITE),
                                    pygame.SRCALPHA)
        blit_coordinate = (int(const.DIMENSION_SPRITE / 4),
                           int(const.DIMENSION_SPRITE / 4))
        background.blit(image, blit_coordinate)
        return background

    def blit(self):
        player = self.get_image()

        return player, (self.x, self.y)


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
            self.blit(self.get_image(box.content.name + '.png'), (0, 0))

    def get_image(self, name):
        image = pygame.image.load(const.RESOURCE_PATH + name)
        image = image.convert_alpha()
        image_width, image_height = image.get_size()
        back_dimension = max((image_height, image_width))
        background = pygame.Surface((back_dimension, back_dimension),
                                    pygame.SRCALPHA)
        difference = image_height - image_width
        blit_coordinate = (int(difference / 2) if difference > 0 else 0,
                           abs(int(difference / 2)) if difference < 0 else 0)
        background.blit(image, blit_coordinate)

        image = pygame.transform.scale(background, (int(const.DIMENSION_SPRITE / 2), int(const.DIMENSION_SPRITE / 2)))
        background = pygame.Surface((const.DIMENSION_SPRITE, const.DIMENSION_SPRITE),
                                    pygame.SRCALPHA)
        blit_coordinate = (int(const.DIMENSION_SPRITE / 4),
                           int(const.DIMENSION_SPRITE / 4))
        background.blit(image, blit_coordinate)
        return background

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
