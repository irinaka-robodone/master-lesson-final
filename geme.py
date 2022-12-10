import object
import pygame
import utils

SCREEN_SIZE=(960,640)


def init():
    pygame.init()
    pygame.display.set_caption("GEME")
    window=pygame.display.set_mode(SCREEN_SIZE)
    window.fill((255,255,255))
    
    player1=object.Player(20,1)
    enemy1=object.Enemy(10,1)
    player1_image=pygame.image.load("matelal/player.png")
    enemy1_image=pygame.image.load("matelal/enemy.png")
    return window, player1,enemy1

def mein():
    clock=pygame.time.Clock()
    running=True
    window, player1,enemy1=init()
    while running:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    player1.attack(5,enemy1)
                elif event.key==pygame.K_SPACE:
                    enemy1.attack(3,player1)
        who_lose=utils.get_who_lose([player1,enemy1])
        print(who_lose)
        if who_lose != None:
            running=False
        pygame.display.flip()
        clock.tick(30)


mein()
# enemy1.attack(3,player1)

# print(player1,player1.hp)
# print(enemy1,enemy1.hp)