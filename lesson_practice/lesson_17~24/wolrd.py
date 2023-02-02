from pygame.locals import*
import sys
import pygame
import random
from utils import puizuBOX


pygame.init()

# screen=pygame.display.set_mode((400,300))
# pygame.display.set_caption("keyboard event")
# font=pygame.font.SysFont("MS UI Gothic", 16)
running = True

# print(f"{puizuID}/{len(puizues)}")


class Wold():
    def __init__(self) -> None:
        
        self.puizues=puizuBOX("bun.csv")
        self.puizuID = random.randint(0,len(self.puizues)-1)  
        self.puizu= self.puizues[self.puizuID]
        self.now_scene="start"
        self.now_puizu_nom=0
        self.goke=0
        self.font=pygame.font.SysFont("MS UI Gothic", 16)
        self.running=True
        self.Xmon=len(self.puizues)
        
        self.screen=pygame.display.set_mode((400,300))
        
        self.Q=self.font.render(self.puizu.question,True, (255,255,255))
    def start(self):
        self.screen.fill((255,255,255))
        self.taitoru=self.font.render("クイズゲーム エンターキーを押してね",True, (215,115,215))
        self.screen.blit(self.taitoru,(10,10))
        for event in pygame.event.get():
            if event.type ==KEYDOWN:
                if event.key ==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:  
                if event.key ==K_RETURN:
                    self.now_scene="game"
        
        pygame.display.flip()
        pygame.display.update() 
                        
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
                
        if self.goke == self.Xmon:
            self.running=False
                        
        self.screen.blit(self.Q,(10,10))
                

    #"押されたキー = " + pygame.key.name(event.key),
        pygame.display.flip()
        pygame.display.update() 
        
        
    def process(self):
        if self.now_scene=="start":
            self.start()
            
            """
            スタート画面用の関数を実行する
            """
        elif self.now_scene=="game":
            self.main()
            
            """""
            クイズゲームをプレイする用の関数を実行する
            """