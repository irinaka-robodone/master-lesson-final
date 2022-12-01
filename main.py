import objeckt
import pygame
import utils

SCREEN_SIZE = (960,640)
clock=pygame.time.Clock()

def init():
    pygame.init()
    pygame.display.set_caption("なっでなで")
    window = pygame.display.set_mode(SCREEN_SIZE)

    player = objeckt.Player(100,1)
    enemy = objeckt.Enemy(100,2)
    return player,enemy

def main():
    running=True
    player,enemy=init()
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:       
                running =False
            elif event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    player.attack(enemy)
                    enemy.X_attck(player)
                    print("player attack!!")
        who_win=utils.get_who_win([player,enemy])

        #print(who_win)
        if who_win != None:
            running=False
            
        clock.tick(30)

# init()
main()