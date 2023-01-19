from pygame.locals import*
import sys
import pygame
import random
from utils import puizuBOX

goke=0
running = True
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("keyboard event")
font=pygame.font.SysFont("MS UI Gothic", 16)
puizues=puizuBOX("bun.csv")


# ESCキーならスクリプトを終了

puizuID = random.randint(0,len(puizues)-1)
puizu = puizues[puizuID]

print(puizues.pop(puizuID))



while True:
    for event in pygame.event.get():
            if event.type ==K_SPACE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:  
                if event.key ==K_ESCAPE :
                        while running:
                            screen.fill((0,0,0))
                            print(f"{puizuID}/{len(puizues)}")
                            
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
                                        puizuID=random.randint(0,len(puizues)-1)
                                        puizu = puizues[puizuID]
                                        print(puizues.pop(puizuID))
                                        goke += 1
                                    
                            if goke == 2:
                                running=False
                                            
                            Q=font.render(puizu.question,True, (255,255,255))
                            screen.blit(Q,(10,10))
                                        

                        #"押されたキー = " + pygame.key.name(event.key),
                            pygame.display.flip()
                            pygame.display.update() 
                                        
                                    
                        else:
                            pass
                                    #Home=font.render("please",True,(100,100,100))
                                    #screen.bilt(Home,(10,10))
                                    
                                
