import pygame
import sys
from pygame.locals import *
import pygame_gui
from world import World

SCREEN_SIZE=(900,600)
FPS = 60
clock = pygame.time.Clock()
world = World()
running = True
while running:
    world.pro()
    clock.tick(config.FPC)

main()
