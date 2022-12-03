import object
import pygame
player1=object.Player(20,1)
enemy1=object.Enemy(10,1)
running=True
while running():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         running=False
        elif event.type==pygame.KEYDOWN:
            if event.kye==pygame.K_RETURN:
                player1.attack(5,enemy1)
                

enemy1.attack(3,player1)

# print(player1,player1.hp)
# print(enemy1,enemy1.hp)