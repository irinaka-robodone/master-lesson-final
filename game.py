import object
import pygame
import utile


SCREEN_SIZE = (900,425)  #全部大文字のやつは定数

def init():
    pygame.init()
    pygame.display.set_caption("なんかよくわからないもの")
    window = pygame.display.set_mode(SCREEN_SIZE)
    window.fill((255,255,255))

    player_image = pygame.image.load("material/player.png")
    teki_image = pygame.image.load("material/teki.png")

    player = object.Player(100,10,10)
    teki = object.Teki(100,10,2)
    return window,player,teki, player_image,teki_image



def main():

    clock = pygame.time.Clock()
    window,player,teki,player_image,teki_image = init()
    ckock = pygame.time.Clock()

    font = pygame.font.SysFont(None,36)
    title_player = font.render("Player",True,(0,0,0))
    title_teki = font.render("teki",True,(0,0,0))

    running = True
    while running:

        window.blit(player_image,(50,50))
        window.blit(teki_image,(300,50))
        window.blit(title_player,(50,50))
        window.blit(title_teki,(300,50))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player.attack(teki)
                    print("player attack!")

        who_win = utile.get_who_win([player,teki])
        print(who_win)
        if who_win !=None:
            text_winner = font.render(f"{who_win} win",True,(0,0,0))
            pygame.display.flip()
            pygame.time.wait(2006)
            running = False
        pygame.display.flip()
        ckock.tick(40)
init()
main()
