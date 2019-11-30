#! /usr/bin/env python3
# coding: utf-8
"""Constants"""

RESOURCE_PATH = "./resource/"

SPRITE_LABYRINTH = 15
DIMENSION_SPRITE = 60
DIMENSION_LABYRINTH = SPRITE_LABYRINTH * DIMENSION_SPRITE
DIMENSION_WINDOW = DIMENSION_LABYRINTH + 250

KEY = {"□": [],
       "←": ["west"],
       "↑": ["north"],
       "→": ["east"],
       "↓": ["south"],
       "━": ["west", "east"],
       "┃": ["north", "south"],
       "┏": ["south", "east"],
       "┓": ["south", "west"],
       "┗": ["north", "east"],
       "┛": ["north", "west"],
       "┣": ["north", "south", "east"],
       "┫": ["north", "south", "west"],
       "┳": ["south", "west", "east"],
       "┻": ["north", "west", "east"],
       "╋": ["north", "south", "west", "east"]
       }
