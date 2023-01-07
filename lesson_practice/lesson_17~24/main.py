from pygame.locals import*
import sys
import pygame
import random
from utils import puizuBOX

pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("keyboard event")
font=pygame.font.SysFont("MS UI Gothic", 16)
puizues=puizuBOX("bun.csv")

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type ==K_SPACE:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:  # キーを押したとき
            # ESCキーならスクリプトを終了
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            else:
                puizu = puizues[random.randint(0,len(puizues)-1)]
                print(puizu)
                
                Q=font.render(puizu.question,True, (255,255,255))
                screen.blit(Q,(10,10))
        
        pygame.display.flip()
        pygame.display.update() 
        #"押されたキー = " + pygame.key.name(event.key),