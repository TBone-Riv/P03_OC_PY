#! /usr/bin/env python3
# coding: utf-8


import pygame
import source.model as model
import source.view as view

from source.constants import *


list_item = [model.Item(i) for i in ['item1', 'item2', 'item3']]

player = model.Player(list_item)


pygame.init()
window = pygame.display.set_mode((DIMENSION_LABYRINTH, DIMENSION_LABYRINTH))
running = True

key_arrow = {pygame.K_UP: 'north', pygame.K_DOWN: 'south', pygame.K_RIGHT: 'east', pygame.K_LEFT: 'west'}

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in key_arrow.keys():
                direction = key_arrow[event.key]
                player.move_to(direction)

        window.blit(view.Labyrinth(player.labyrinth), (0, 0))
        window.blit(*view.Player(player).blit())

        pygame.display.update()


