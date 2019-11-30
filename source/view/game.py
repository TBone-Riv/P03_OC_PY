#! /usr/bin/env python3
# coding: utf-8
"""View module"""

import pygame
import source.constants as const
from source.view.player import Player
from source.view.labyrinth import Labyrinth


class Game:

    def blit(self, game, window):
        window.fill((255, 255, 255))
        window.blit(Labyrinth(game.labyrinth), (0, 0))
        window.blit(*Player(*game.player.get_position()).blit())

        font = pygame.font.Font(None, 24)
        text = font.render("You have :", 1, (0, 0, 0))

        window.blit(text, (const.DIMENSION_LABYRINTH + 10, 10))
        for indices, item in enumerate(game.player):
            window.blit(self.get_image(item.name + '.png'),
                        (const.DIMENSION_LABYRINTH + 20,
                         indices * const.DIMENSION_SPRITE + 40))

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

        image = pygame.transform.scale(background,
                                       (const.DIMENSION_SPRITE,
                                        const.DIMENSION_SPRITE))
        return image
