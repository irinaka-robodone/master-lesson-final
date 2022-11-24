import object 
import pygame

SCREEN_SIZE = (960, 640)        # 全部大文字のやつ: 定数

def init():
    """
    ゲーム画面を初期化する
    """
    pygame.init()
    pygame.display.set_caption("猫をなでなでしよう（激しく）")
    window = pygame.display.set_mode(SCREEN_SIZE)
    
    """
    プレイヤーと敵を定義する
    """
    player = object.Player(100, 10, 10)
    enemy = object.Enemy(100, 0.5)
    return player, enemy

def main():
    clock = pygame.time.Clock()
    player, enemy = init()
    
    """
    ゲームを動かす処理をここに書く
    """
    running = True
    while running:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player.attack(enemy)
                        print("player attacked!")
        
        clock.tick(30)
        
        
    
init()
main()