import sys
import random
import pygame
from pygame_textinput.textinput import TextInput

from utils import render_text

SCREEN_SIZE=(900,600)
FPS = 60

class World():
    def __init__(self) -> None:
        self.running= True
        # self.font = pygame.font.SysFont("Noto Sans JP", 20)
        self.taitoru_font = pygame.font.Font("font/NotoSansJP-Black.otf", 60)
        self.enta_font = pygame.font.Font("font/NotoSansJP-Black.otf",30)
        self.bun_font = pygame.font.Font("font/NotoSansJP-Black.otf",40)

        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("しりとりゲーム")
        self.window = pygame.display.set_mode(SCREEN_SIZE)
        self.window.fill((255,255,255))
        
        self.bg_img = pygame.image.load("../asset/bg.jpg")
        
        self.current_scene = "start"
        
        self.text_box = TextInput(pygame.font.SysFont("yumincho", 30), (255, 0, 0))
        # self.siritori_history = ["りんご", "ごりら", "らっぱ", "ぱんつ", "つみき", "きつつき", "きんぱ", "ぱりぴ", "ぴっと", "とーます", "するめ", "めんこ", "こあら", "らじお", "おがわ", "わに", "にんにく", "くりすます", "すいか", "からす"]
        self.siritori_history = ["しりとり"]
        self.mae_word = self.siritori_history[-1]
        self.otetuki_kaunto =  0
        
        self.prev_answer_input = False


    def show_start_screen(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                if event.key == pygame.K_RETURN:
                    self.current_scene = "play"
                    
                elif event.key == pygame.K_SPACE:
                    self.current_scene = "history"
        
        render_text(self.window, "しりとりゲーム!", 70, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos="center", padding_top=-120)
        render_text(self.window, "Enterキーを押してスタート", 28, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos="center", padding_top=40)
        render_text(self.window, "Escキーを押して終了", 28, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos="center", padding_top=100)
        render_text(self.window, "Spaceキー(半角)を押して、しりとりの履歴を表示", 28, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos="center", padding_top=160)


    def play_siritori(self):
        answer = ""
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.prev_answer_input == True:
                    
                    if self.answer[-1] != "ん" and self.mae_word[-1]== self.answer[0] and self.answer not in self.siritori_history:
                        self.mae_word = self.answer
                        self.siritori_history.append(self.answer)
                        
                    else:
                        print("Mistake!")
                        self.otetuki_kaunto += 1
                        self.current_scene = "mistake"
                        self.prev_answer_input = False
                        self.text_box.text = "|"
                        
            
            if event.type == pygame.TEXTINPUT:
                # print(event.text)
                if len(self.mae_word) < 1 or len(event.text) < 1:
                    continue

                else:
                    self.answer = event.text
                    self.prev_answer_input = True
            
            # if event.type == pygame.USEREVENT:
            #     # 入力確定したテキスト
            #     print(event)
            #     if len(self.mae_word) < 1 or len(event.Text) < 1:
            #         continue
            #     elif event.Text[-1] == "ん":
            #         otetsuki = self.taitoru_font.render("お手つき！", True, (0,0,0))
            #         otetsuki_rect = otetsuki.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
            #         self.window.blit(otetsuki, otetsuki_rect)
            #         self.update_display()
            #         pygame.time.wait(1000)

            #     elif self.mae_word[-1]== event.Text[0] and event.Text not in self.siritori_history:
            #         self.mae_word = event.Text
            #         self.siritori_history.append(event.Text)
            #     #elif self.otetuki_kaunto = [+1]

            #     else:
            #         print("otetuki")
            #         otetsuki = self.taitoru_font.render("お手つき！", True, (0,0,0))
            #         otetsuki_rect = otetsuki.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
            #         self.window.blit(otetsuki, otetsuki_rect)
            #         self.update_display()
            #         pygame.time.wait(1000)
            #         # self.running = False
                
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.current_scene = "start"
        
        self.text_box.update(events)
        text_box_rect = self.text_box.get_surface().get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
        self.window.blit(self.text_box.get_surface(), text_box_rect)
        bun_text = self.bun_font.render(self.mae_word, True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-100))
        self.window.blit(bun_text, bun_text_rect)

        bun_text = self.bun_font.render("▼", True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-150))
        self.window.blit(bun_text, bun_text_rect)

        if len(self.siritori_history) >= 2:
            bun_text = self.bun_font.render(self.siritori_history[-2], True, (10,10,10))
            bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-200))
            self.window.blit(bun_text, bun_text_rect)

        bun_text = self.bun_font.render("▼", True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-50))
        self.window.blit(bun_text, bun_text_rect)
        
        render_text(self.window, "Escキーを押してスタート画面に戻る", 20, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos = (550,550))
        
    def show_help(self):
        render_text(self.window, "お手つき!", 50, font_pass = "font/NotoSansJP-Black.otf", color = (10,10,10), pos = "center", padding_top= -40)
        render_text(self.window, "続けるにはEnterキーを押してね", 28, font_pass = "font/NotoSansJP-Black.otf", color = (10,10,10), pos = "center", padding_top= 30)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.current_scene = "play"
            
    def show_history(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.current_scene = "start"
        
        render_text(self.window, "ここまでのしりとり履歴", 24, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos = (40,20))
        j = 0
        for i, noun in enumerate(self.siritori_history):
            
            col = i//10
            index = i%10
            render_text(self.window, f"{i+1}: {noun}", 16, (10,10,10), font_pass = "font/NotoSansJP-Black.otf", pos=(60 + 200*col, 80 + 45*index))
            render_text(self.window, "▼", 16, (10,10,10), font_pass= "font/NotoSansJP-Black.otf", pos=(90 + 200*col, 100+45*index))
        
        render_text(self.window, "Escキーを押してスタート画面に戻る", 20, (10,10,10), font_pass="font/NotoSansJP-Black.otf", pos = (550,550))
        
    def draw_bg(self):
        self.window.fill((255,255,255))
        self.bg_img = pygame.transform.scale(self.bg_img, (900, 600)) 
        self.window.blit(self.bg_img, (0,0), )

    def update_display(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(FPS)

    def init(self):
        pygame.init()
        pygame.display.set_caption("しりとりゲーム")
        window = pygame.display.set_mode(SCREEN_SIZE)
        window.fill((255,255,255))

        return window
    

    def pro(self):
        if self.current_scene == "start":
            self.draw_bg()
            self.show_start_screen()
            self.update_display()

        elif self.current_scene == "play":
            self.draw_bg()
            self.play_siritori()
            self.update_display()
            
        elif self.current_scene == "mistake":
            self.draw_bg()
            self.show_help()
            self.update_display()
            
        elif self.current_scene == "history":
            self.draw_bg()
            self.show_history()
            self.update_display()