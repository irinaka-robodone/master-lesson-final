import object
import pygame
import utile


SCREEN_SIZE = (900,425)  #全部大文字のやつは定数  

def init():
    pygame.init()
    pygame.display.set_caption("なんかよくわからないもの")
    window = pygame.display.set_mode(SCREEN_SIZE)
    
    player = object.Player(100,10,10)
    teki = object.Teki(100,10,2)
    return player,teki
    

def main():
    clock = pygame.time.Clock()
    player,teki = init()
    ckock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player.attack(teki)
                    print("player attack!")
        utile.get_who_win([player,teki])           
        
        ckock.tick(40)  
init()
main()
