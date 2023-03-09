import lesson_practice.objeckt as objeckt
import pygame
import lesson_practice.utils as utils

SCREEN_SIZE = (960,640)
clock=pygame.time.Clock()

def init():
    pygame.init()
    pygame.display.set_caption("なっでなで")
    window = pygame.display.set_mode(SCREEN_SIZE)
    window.fill((255,255,255))

    player = objeckt.Player(10,1)
    enemy = objeckt.Enemy(23,2)

    player_image=pygame.image.load("material/player.png")
    enemy_image=pygame.image.load("material/enemy.png")

    return window,player,enemy,player_image,enemy_image


def main():
    running=True
    #player,enemy=init()
    
    window,player,enemy,player_image,enemy_image=init() 
    
    font = pygame.font.SysFont(None,36)
    title_player=font.render('Player',True,(50,50,50))
    title_enemy=font.render("enemy",True,(50,50,50))
    
    
    while running:
        
        window.blit(player_image,(50,50))
        window.blit(enemy_image,(500,50))
        window.blit(title_player,(50,20))
        window.blit(title_enemy,(500,20))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:       
                running =False
            elif event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    player.attack(enemy)
                    enemy.X_attck(player)
                    print("player attak")
                elif event.key==pygame.K_SPACE:
                    enemy.X_attck(player)
        who_win=utils.get_who_win([player,enemy])

        #print(who_win)
        if who_win != None:
            text_winer=font.render(f"{who_win} Lose!",True,(0,0,0))
            window.blit(text_winer,(200,50))
            pygame.display.flip()
            pygame.time.wait(3000)
            running=False
            
            
        pygame.display.flip()
        
        
        clock.tick(30)
        


# init()
main()