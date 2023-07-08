from typing import Any
from pygame.locals import*
import sys
import pygame
import random
from .utils import puizuBOX, render_text
import time

class World():
    def __init__(self, quiz_filepath: str, num_quiz: int, interval: int = 5,) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)
        self.bg_color = (64,64,64)
        self.font_color = (211,211,211)
        self.quiz_filepath = quiz_filepath
        self.puizues=puizuBOX(quiz_filepath)
        if num_quiz < 0 or num_quiz >= len(self.puizues):
            self._num_quiz = len(self.puizues)
        else:
            self._num_quiz = int(num_quiz)
        
        self.puizues = random.sample(self.puizues, self._num_quiz)
        self.puizuID = random.randint(0,len(self.puizues)-1)
        self.puizu= self.puizues[self.puizuID]
        self.puizues.pop(self.puizuID)
        self.now_scene="start"
        self.font=pygame.font.SysFont("MS UI Gothic", 16)
        self.running=True
        self.screen_size = (900, 600)
        self.screen=pygame.display.set_mode(self.screen_size)
        self.cotae=self.puizu.answer
        self.seikai=0
        self.an_seikai=0
        self.tou_answer=0
        self.mondaisu=0
        self._interval = interval
        self.a = self.puizu.choices[0]
        self.b = self.puizu.choices[1]
        self.c = self.puizu.choices[2]
        self.d = self.puizu.choices[3]
        self._bgm = pygame.mixer.Sound("asset/sound/maou_bgm_fantasy08.mp3")
        self.do_mixing()
    
    def start(self):
        self.screen.fill(self.bg_color)
        render_text(self.screen, "クイズゲーム！", 72, self.font_color, "MS UI Gothic", "center", padding_top=-40)
        render_text(self.screen, "エンターキーを押してゲームをスタート！", 24, self.font_color, "MS UI Gothic", "center", padding_top=40)
        render_text(self.screen, "Esc キーを押すとゲームを終了するよ", 18, self.font_color, pos="center", padding_top=100)

        for event in self.events:
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
                    self.screen.fill(self.bg_color)
                    
                            
    def sentaku (self):
        render_text(self.screen, f"A: {self.puizu.choices[0]}", 22, self.font_color, "MS UI Gothic", [80, 200])
        render_text(self.screen, f"B: {self.puizu.choices[1]}", 22, self.font_color, "MS UI Gothic", [80, 260])
        render_text(self.screen, f"C: {self.puizu.choices[2]}", 22, self.font_color, "MS UI Gothic", [80, 320])
        render_text(self.screen, f"D: {self.puizu.choices[3]}", 22, self.font_color, "MS UI Gothic", [80, 380])

        
    def main(self):
        self.screen.fill(self.bg_color)
        self.font = pygame.font.SysFont("MS UI Gothic", 15, bold=True)
        for event in self.events:
            if event.type ==K_SPACE:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:  # キーを押したとき
                # ESCキーならスクリプトを終了
                if event.key ==K_ESCAPE :
                    self.now_scene = "start"
            
                if event.key == K_a:
                    self.tou_answer = "1"
                if event.key == K_b:
                    self.tou_answer = "2"
                if event.key == K_c:
                    self.tou_answer = "3"
                if event.key == K_d:
                    self.tou_answer = "4"
                if event.key in (K_a, K_b,K_c,K_d):
                    self.now_scene="jazzi"
                    
        render_text(self.screen, "問題:", 32, self.font_color, "MS UI Gothic", [60,30])
        render_text(self.screen, self.puizu.question, 20, self.font_color, "MS UI Gothic", [60,80])
        render_text(self.screen, "Esc キーを押してタイトルに戻る", size = 18, color=self.font_color, pos=[616, 572])
        
        
        
    def update_display(self):
        pygame.display.flip()
        pygame.display.update()
        
    def _load_effect_sound(self, seikai: bool):
        if seikai:
            self._ef = pygame.mixer.Sound("asset/sound/maou_se_chime14.mp3")
        else:
            self._ef = pygame.mixer.Sound("asset/sound/maou_se_onepoint33.mp3")
        
    def _play_bgm(self):
        pygame.mixer.Channel(0).play(self._bgm, loops=-1, fade_ms = 1000)
        
    def _play_effect_sound(self):
        pygame.mixer.Channel(1).play(self._ef)
    
    def _pause_bgm(self):
        pygame.mixer.Channel(0).pause()

    def _fadeout_bgm(self):
        pygame.mixer.Channel(0).fadeout(1)
        
    def _rewind_bgm(self):
        pygame.mixer.Channel(0).unpause()
        
    def _unpause_bgm(self):
        pygame.mixer.Channel(0).unpause()
        
    def _set_bgm_volume(self, volume: float = 1.0):
        pygame.mixer.Channel(0).set_volume(volume)
    
    def do_mixing(self):
        self._play_bgm()
        # pygame.mixer.music.play()
    
    def get_events(self):
        self.events = pygame.event.get()
        
    def handan(self):
        self.now_scene = "game"
        self.screen.fill(self.bg_color)
        font = pygame.font.SysFont("MS UI Gothic", 48, bold=True)
        self.mondaisu += 1
        for event in self.events:
            if event.type ==K_SPACE:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # if event.type == KEYDOWN:
            #     if event.key ==K_0:
            #         self.now_scene="game"
            
        if self.tou_answer == self.puizu.answer:
            self.seikai += 1
            self.yesno = font.render("正解",True, self.font_color)
            self.is_seikai = True
        else:
            self.an_seikai += 1
            self.yesno = font.render("不正解",True, self.font_color)
            self.is_seikai = False
            
        self._load_effect_sound(self.is_seikai)
        self._set_bgm_volume(0.3)
        self._play_effect_sound()
            
        text_size = self.yesno.get_rect()
        self.screen.blit(self.yesno, (self.screen_size[0]//2 - text_size.w//2, self.screen_size[1]//2 - text_size.h//2 - 80))
        render_text(self.screen, f"問題: {self.puizu.question}", size = 20, color = self.font_color, pos = [60, 400])
        render_text(self.screen, "答え:", size = 20, color =self.font_color, pos = [60, 448])
        render_text(self.screen, f"{self.puizu.choices[int(self.puizu.answer)-1]}", size = 30, color = self.font_color, pos = [140, 440])
        
        self.update_display()
        pygame.time.wait(2000)
        self._set_bgm_volume(1.0)

        print("-"*30)
        print(self.mondaisu, self.mondaisu%self._interval==0)

        if len(self.puizues) > 0:      # 今出題したクイズを含むクイズ数が1以上だったら、クイズを削る処理をする。
            self.puizuID=random.randint(0,len(self.puizues)-1)
            self.puizu = self.puizues[self.puizuID]
            # self.Q=self.font.render(self.puizu.question,True, self.font_color)
            self.puizues.pop(self.puizuID)
            self.now_scene="game"
            self.screen.fill(self.bg_color)
            
        if self.mondaisu%self._interval == 0:
            self.now_scene="pause"
        
        if self.mondaisu >= self._num_quiz:
            self.now_scene="kekka"
        
    def result(self):
        self.screen.fill(self.bg_color)
                
        render_text(self.screen, f"正答数: {self.seikai}", size=20, color=self.font_color, pos=[280, 360])
        render_text(self.screen, f"誤答数: {self.an_seikai}", size=20, color=self.font_color, pos=[510, 360])
        render_text(self.screen, f"全{self._num_quiz}問中、{self.seikai}問正解しました！", size = 28, color=self.font_color, padding_top= -50)
        render_text(self.screen, f"正答率: {self.seikai / self._num_quiz * 100 //1} %", size = 28, color= self.font_color, padding_top= -10)
        render_text(self.screen, "エンターキーを押してタイトルに戻る", size = 18, color=self.font_color, pos=[576, 572])
        
        for event in self.events:
            if event.type ==KEYDOWN:
                if event.key ==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key ==K_RETURN:
                    self.now_scene = "start"
                    self.__init__(self.quiz_filepath, self._num_quiz, self._interval)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def kyuukei(self):
        
        for event in self.events:
            if event.type ==KEYDOWN:
                if event.key ==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key ==K_RETURN:
                    self.now_scene="game"
                    self.screen.fill(self.bg_color)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        self.screen.fill(self.bg_color)
        render_text(self.screen, "休憩タイム", size=24, color=self.font_color)
        render_text(self.screen, f"回答状況: {self.mondaisu}/ {self._num_quiz}", size = 20, color=self.font_color, padding_top=30)
        render_text(self.screen, "エンターキーを押して続ける", size = 20, color=self.font_color, padding_top=60)
        print("break time!")
        
    def process(self):
        if self.now_scene=="start":
            """
            スタート画面用の関数を実行する
            """
            self.get_events()
            self.start()
            self.update_display()
            
        elif self.now_scene=="game":
            """""
            クイズゲームをプレイする用の関数を実行する
            """
            self.get_events()
            self.main()
            self.sentaku()
            self.update_display()
            
        elif self.now_scene=="jazzi":
            self.get_events()
            self.handan()
            self.update_display()
            
        elif self.now_scene=="kekka":
            self.get_events()
            self.result()
            self.update_display()
            
        elif self.now_scene=="pause":
            self.get_events()
            self.kyuukei()
            self.update_display()
            
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.do_mixing()
            
if __name__ == "__main__":
    world = World("../asset/qa_v2.csv", 5, 5)