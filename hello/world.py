import sys
import random
sys.path.append("../")
import pygame
import pygame_gui



SCREEN_SIZE=(900,600)
FPS = 60
clock = pygame.time.Clock()
def show_text(window, text):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
        window.fill((255,255,255))
        new_text = pygame.font.SysFont("MS P ゴシック", 20).render(text, True, (10,10,10))
        new_text_rect = new_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
        window.blit(new_text, new_text_rect)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


class World():
    def __init__(self) -> None:
        self.running= True

        # self.font = pygame.font.SysFont("Noto Sans JP", 20)
        self.taitoru_font = pygame.font.Font("font/NotoSansJP-Black.otf", 60)
        self.enta_font = pygame.font.Font("font/NotoSansJP-Black.otf",30)
        self.bun_font = pygame.font.Font("font/NotoSansJP-Black.otf",40)


        self.curent_scene = "menyu"
        self.mae_word = "siritori"

        pygame.init()
        pygame.display.set_caption("しりとりゲーム")
        self.window = pygame.display.set_mode(SCREEN_SIZE)
        self.window.fill((255,255,255))

        self.manager = pygame_gui.UIManager(
            SCREEN_SIZE,
            theme_path="theme.json"
        )

        self.input_box = pygame_gui.elements.UITextEntryLine(
            pygame.Rect(SCREEN_SIZE[0]//2 - 500//2, SCREEN_SIZE[1]//2 - 30//2, 500, 40),
            self.manager,
            object_id="#main_text_entry"
        )

        self.siritori_rekisi = [self.mae_word]

        # テキストボックスのサイズ
self.TEXTBOX_WIDTH = 200
self.TEXTBOX_HEIGHT = 30

# テキストボックスのフォント
self.font = pygame.font.SysFont('Arial', 24)

# テキストボックスの背景色
self.bg_color = (255, 255, 255)

# テキストボックスの表示位置
self.textbox_x = (WINDOW_WIDTH - TEXTBOX_WIDTH) // 2
self.textbox_y = (WINDOW_HEIGHT - TEXTBOX_HEIGHT) // 2

# テキストボックスの作成
self.textbox = tk.Entry(window, font=('Arial', 24), bg='white')
self.textbox.place(x=textbox_x, y=textbox_y, width=TEXTBOX_WIDTH, height=TEXTBOX_HEIGHT)



def show_start_screen(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.curent_scene = "nyuryoku"
        self.window.fill((255,255,255))

        taitoru_text = self.taitoru_font.render("しりとりゲーム‼", True, (10,10,10))
        taitoru_text_rect = taitoru_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-50))
        self.window.blit(taitoru_text, taitoru_text_rect)

        enta_text = self.enta_font.render("Enterキーを押してスタート", True, (15,10,10))
        enta_text_rect = enta_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2+50))
        self.window.blit(enta_text, enta_text_rect)


        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)

    def nyuryoku(self):
        self.window.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.curent_scene = "nyuryoku"

            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                if self.mae_word[-1]== event.text[0]:
                    self.mae_word = event.text
                    self.siritori_rekisi.append(event.text)
                else:
                    pass
                # show_text(self.window, event.text)

            self.manager.process_events(event)

        time_delta = clock.tick(FPS)/ 1000.0
        moji = self.mae_word
        print(moji[-1])
        self.manager.update(time_delta)
        self.manager.draw_ui(self.window)
        bun_text = self.bun_font.render(self.mae_word, True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-100))
        #show_text(self.window, )
        self.window.blit(bun_text, bun_text_rect)


        bun_text = self.bun_font.render("▼", True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-150))
        self.window.blit(bun_text, bun_text_rect)

        if len(self.siritori_rekisi) >= 2:
            bun_text = self.bun_font.render(self.siritori_rekisi[-2], True, (10,10,10))
            bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-200))
            #show_text(self.window, )
            self.window.blit(bun_text, bun_text_rect)


        bun_text = self.bun_font.render("▼", True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-50))
        #show_text(self.window, )
        self.window.blit(bun_text, bun_text_rect)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


    def init(self):
        pygame.init()
        pygame.display.set_caption("しりとりゲーム")
        window = pygame.display.set_mode(SCREEN_SIZE)
        window.fill((255,255,255))

        return window
    def main():
        clock = pygame.time.Clock()

    def pro(self):
        if self.curent_scene == "menyu":
            self.show_start_screen()

        elif self.curent_scene == "nyuryoku":
            self.nyuryoku()
