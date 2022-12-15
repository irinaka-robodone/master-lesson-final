import pygame

SCREEN_SIZE=(900,600)

def init():
    pygame.init()
    pygame.display.set_caption("しりとりゲーム")
    Window = pygame.display.set_mode(SCREEN_SIZE)
    Window.fill((255,255,255))    
def mian():

    init()
    clook = pygame.time.Clock()
    ckock = pygame.time.Clock()

    running = True 
    while running:
        pygame.display.flip()
        ckock.tick(40)

mian()