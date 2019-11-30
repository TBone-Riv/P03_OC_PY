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

        image = pygame.transform.scale(background,
                                       (int(const.DIMENSION_SPRITE / 2),
                                        int(const.DIMENSION_SPRITE / 2)))

        background = pygame.Surface((const.DIMENSION_SPRITE,
                                     const.DIMENSION_SPRITE),
                                    pygame.SRCALPHA)

        blit_coordinate = (int(const.DIMENSION_SPRITE / 4),
                           int(const.DIMENSION_SPRITE / 4))

        background.blit(image, blit_coordinate)
        return background

    def blit(self):
        player = self.get_image()

        return player, (self.x, self.y)
