import csv
import pygame
from pygame.locals import*
from .object import Puizu

def puizuBOX(file):
    puizus=[]
    with open(file, encoding="utf-8") as f:
        #print(f.read())
        reader=csv.reader(f)

        for i,row in enumerate(reader):
            #print(row)
            if i < 1:
                pass
            else:
                puizu=Puizu()
                puizu.question=row[0]
                puizu.type=row[1]
                puizu.answer=row[2]
                puizu.choices=[]
                puizu.choices.append(row[3])
                puizu.choices.append(row[4])
                puizu.choices.append(row[5])
                puizu.choices.append(row[6])
                
                
                puizus.append(puizu)
    return puizus

def render_text(screen: pygame.Surface, text: str, size: int, color: tuple, font_name: str = "MS UI Gothic", pos: list[2] = "center", bold: bool = True, italic: bool = False, padding_top: int = 0):
    font = pygame.font.SysFont(font_name, size, bold, italic)
    rend = font.render(text, True, color)
    frame_size = rend.get_rect()
    
    if pos == "center":
        screen.blit(rend, (screen.get_width()//2 - frame_size.w//2, screen.get_height()//2 - frame_size.h//2 + padding_top))
    else:
        screen.blit(rend, pos)
        
#puizues=puizuBOX()
# puizues = puizues[random.randint(0,2)]
# print(puizues)
