#! /usr/bin/env python3
# coding: utf-8


import pygame
import source.constants as const
from source.model.game import Game
import source.view as view


if __name__ == '__main__':
    game = Game()

    pygame.init()

    window = pygame.display.set_mode((const.DIMENSION_LABYRINTH, const.DIMENSION_LABYRINTH))
    running = True

    key_arrow = {pygame.K_UP: 'north', pygame.K_DOWN: 'south', pygame.K_RIGHT: 'east', pygame.K_LEFT: 'west'}

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in key_arrow.keys():
                    direction = key_arrow[event.key]
                    game.set_player_position(direction)

            window.blit(view.Labyrinth(game.labyrinth), (0, 0))
            window.blit(*view.Player(*game.player.get_position()).blit())

            if game.win_condition is not None:
                if game.win_condition:
                    print("""
                        --------------------------------
                                    YOU WIN             
                        --------------------------------
                        """)
                else:
                    print("""
                        --------------------------------
                                    YOU LOSE             
                        --------------------------------
                        """)
                running = False

            pygame.display.update()


