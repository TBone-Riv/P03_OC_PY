#! /usr/bin/env python3
# coding: utf-8


import pygame
import source.constants as const
from source.model.game import Game
from source.view.game import Game as View


if __name__ == '__main__':
    game = Game()

    pygame.init()

    window = pygame.display.set_mode((const.DIMENSION_WINDOW, const.DIMENSION_LABYRINTH))
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

            View().blit(game, window)

            if game.win_condition is not None:
                running = False
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        if game.win_condition:
            window.fill((255, 255, 255))
            font = pygame.font.Font(None, 24)
            text = font.render("You win", 1, (0, 0, 0))

            window.blit(text, (int(const.DIMENSION_LABYRINTH / 2), 10))
        else:
            window.fill((255, 255, 255))
            font = pygame.font.Font(None, 24)
            text = font.render("You lose", 1, (0, 0, 0))

            window.blit(text, (int(const.DIMENSION_LABYRINTH / 2), 10))

        pygame.display.update()


