from pygame.locals import*
import sys
import pygame
import random
from utils import puizuBOX


pygame.init()

# screen=pygame.display.set_mode((400,300))
# pygame.display.set_caption("keyboard event")
# font=pygame.font.SysFont("MS UI Gothic", 16)


# print(f"{puizuID}/{len(puizues)}")


class Wold():
    def __init__(self) -> None:
        
        self.puizues=puizuBOX("bun.csv")
        self.puizuID = random.randint(0,len(self.puizues)-1)  
        self.puizu= self.puizues[self.puizuID]
        self.now_scene="start"
        self.now_puizu_nom=0
        self.goke=2
        self.font=pygame.font.SysFont("MS UI Gothic", 16)
        self.running=True
        
        self.screen=pygame.display.set_mode((400,300))
        
        self.Q=self.font.render(self.puizu.question,True, (255,255,255))
    def start(self):
        for event in pygame.event.get():
            if event.type ==K_SPACE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:  
                if event.key ==K_ESCAPE:
                    self.now_scene
                        
    def main(self):
        self.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type ==K_SPACE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key ==K_ESCAPE :
                    pygame.quit()
                    sys.exit()

                else:
                    puizuID=random.randint(0,len(self.puizues)-1)
                    self.puizu = self.puizues[puizuID]
                    self.Q=self.font.render(self.puizu.question,True, (255,255,255))
                    print(self.puizues.pop(puizuID))
                    self.goke += 1
                
        if self.goke == 2:
            self.running=False
                        
        
        self.screen.blit(self.Q,(10,10))
                    

    #"押されたキー = " + pygame.key.name(event.key),
        pygame.display.flip()
        pygame.display.update() 
        
        
    def process(self):
        if self.now_scene=="start":
            self.main()
            
            
        
            """
            スタート画面用の関数を実行する
            """
        elif self.game_scence=="game":
            self.main()
            
            """""
            クイズゲームをプレイする用の関数を実行する
            """