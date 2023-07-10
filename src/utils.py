import csv
import pygame
from pygame.locals import*

def render_text(screen: pygame.Surface, text: str, size: int, color: tuple, font_name: str = "MS UI Gothic", font_pass: str = None, pos: list[2] = "center", bold: bool = True, italic: bool = False, padding_top: int = 0):
    if font_pass == None:
        font = pygame.font.SysFont(font_name, size, bold, italic)
    else:
        font = pygame.font.Font(font_pass, size)
    
    rend = font.render(text, True, color)
    frame_size = rend.get_rect()
    
    if pos == "center":
        screen.blit(rend, (screen.get_width()//2 - frame_size.w//2, screen.get_height()//2 - frame_size.h//2 + padding_top))
    else:
        screen.blit(rend, pos)
