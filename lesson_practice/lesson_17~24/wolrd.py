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
        self.puizues.pop(self.puizuID)
        self.now_scene="start"
        self.now_puizu_nom=0
        self.goke=0
        self.font=pygame.font.SysFont("MS UI Gothic", 16)
        self.running=True
        self.Xmon=len(self.puizues)
        self.screen=pygame.display.set_mode((400,300))
        self.cotae=self.puizu.answer
        self.tou=0
        self.a = self.puizu.choices[0]
        self.b = self.puizu.choices[1]
        self.c = self.puizu.choices[2]
        self.d = self.puizu.choices[3]
        self.final_answer=0
        
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
        
    def sentaku (self):
        self.sentacu_1=self.font.render(f"A: {self.puizu.choices[0]}",True, (255,255,255))
        self.screen.blit(self.sentacu_1,(50,100))
        self.sentacu_2=self.font.render(f"B:{self.puizu.choices[1]}",True, (255,255,255))
        self.screen.blit(self.sentacu_2,(50,150))
        self.sentacu_3=self.font.render(f"C:{self.puizu.choices[2]}",True, (255,255,255))
        self.screen.blit(self.sentacu_3,(50,200))
        self.sentacu_4=self.font.render(f"D:{self.puizu.choices[3]}",True, (255,255,255))
        self.screen.blit(self.sentacu_4,(50,250))
            
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
            
                if event.key == K_a:
                    self.tou = "1"
                if event.key == K_b:
                    self.tou = "2"
                if event.key == K_c:
                    self.tou = "3"
                if event.key == K_d:
                    self.tou = "4"
                # if event.key ==K_RETURN:
                #     self.reply()
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
        
    def update_display(self):
        pygame.display.flip()
        pygame.display.update()
    
    
    
    
    def reply(self):
        if self.tou == self.puizu.answer:
            print("yes")
            self.Yes=self.font.render("正解",True, (255,255,115))
            self.screen.blit(self.Yes,(300,200))
            
        else:
            self.No=self.font.render("不正解",True, (215,255,255))
            self.screen.blit(self.No,(300,100))
            
            print(self.tou)
        
            
            
    def process(self):
        if self.now_scene=="start":
            self.start()
            self.update_display()
            """
            スタート画面用の関数を実行する
            """
        elif self.now_scene=="game":
            self.main()
            self.sentaku()
            self.reply()
            self.update_display()
            """""
            クイズゲームをプレイする用の関数を実行する
            """