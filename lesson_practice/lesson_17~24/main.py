from pygame.locals import*
import sys
import pygame
import random
from utils import puizuBOX
from wolrd import Wold

wold=Wold()


running = True
# pygame.init()
# screen=pygame.display.set_mode((400,300))
# pygame.display.set_caption("keyboard event")
# font=pygame.font.SysFont("MS UI Gothic", 16)
# puizues=puizuBOX("bun.csv")

# # ESCキーならスクリプトを終了

# puizuID = random.randint(0,len(puizues)-1)
# puizu = puizues[puizuID]

# print(puizues.pop(puizuID))
while wold.running :
    wold.process()
