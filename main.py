from pygame.locals import*
import sys
import pygame
import random
from utils import puizuBOX
from wolrd import Wold

wold=Wold("bun_v2.csv")

while wold.running :
    wold.process()
