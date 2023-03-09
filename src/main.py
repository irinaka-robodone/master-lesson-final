import pygame
import sys
from pygame.locals import *
import pygame_gui
from world import World

SCREEN_SIZE=(900,600)
FPS = 60

pygame.init()
clock = pygame.time.Clock()

world = World()

while world.running:
    world.pro()
    clock.tick(60)







