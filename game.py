import object 
import pygame
import utils

SCREEN_SIZE = (960, 640)        # 全部大文字のやつ: 定数

def init():
    """
    ゲーム画面を初期化する
    """
    pygame.init()
    pygame.display.set_caption("猫をなでなでしよう（激しく）")
    window = pygame.display.set_mode(SCREEN_SIZE)
    window.fill((255,255,255))
    """
    プレイヤーと敵を定義する
    """
    player = object.Player(100, 10, 10)
    enemy = object.Enemy(100, 0.5)
    
    player_image = pygame.image.load("material/player.png")
    enemy_image = pygame.image.load("material/enemy.png")
    
    return window, player, enemy, player_image, enemy_image

def main():
    clock = pygame.time.Clock()
    window, player, enemy, player_image, enemy_image = init()
    
    font = pygame.font.SysFont(None, 36)
    
    title_player = font.render("Player", True, (0,0,0))
    title_enemy = font.render("Enemy", True, (0,0,0))
    
    
    """
    ゲームを動かす処理をここに書く
    """
    running = True
    while running:
        
        """
        描画の処理はここに書く
        """
        window.blit(player_image, (50, 50))
        window.blit(enemy_image, (500, 50))
        window.blit(title_player, (50, 20))
        window.blit(title_enemy, (500, 20))
        
        for event in pygame.event.get():            # 
                if event.type == pygame.QUIT:       # イベントQUIT: 出る、アプリを止める
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player.attack(enemy)
                        print("player attacked!")
                    elif event.key == pygame.K_SPACE:
                        enemy.random_attack((player))
        
        who_win = utils.get_who_win([player, enemy])
        print(who_win)
        if who_win != None:
            text_winner = font.render(f"{who_win} lose!", True, (0,0,0))
            window.blit(text_winner, (200, 50))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
            
        pygame.display.flip()
        clock.tick(30)
        
    
init()
main()
