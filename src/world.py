import sys
import random
sys.path.append("../")
import pygame
import pygame_gui
from pygame_textinput.textinput import TextInput

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

        self.screen.blit("bg.jpg")


        self.curent_scene = "menyu"
        self.mae_word = "りんご"

        pygame.init()
        pygame.display.set_caption("しりとりゲーム")
        self.window = pygame.display.set_mode(SCREEN_SIZE)
        self.window.fill((255,255,255))

        self.text_box = TextInput(pygame.font.SysFont("yumincho", 30), (255, 0, 0))

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

        self.otetuki_kaunto =  0


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

        textbox_x = (SCREEN_SIZE[0] - 100) // 2
        textbox_y = (SCREEN_SIZE[1]- 30) // 2

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    # text = textbox.get(())
                    self.curent_scene = "nyuryoku"

                    # if self.mae_word[-1] == text[0]:
                    #     self.mae_word = text
                    #     self.siritori_rekisi.append(text)
                    # else:
                    #     pass
                    # show_text(self.window, event.text)
                    pass

            if event.type == pygame.USEREVENT:
                # 入力確定したテキスト
                print(event.Text)
                if len(self.mae_word) < 1 or len(event.Text) < 1:
                    continue
                elif event.Text[-1] == "ん":
                    otetsuki = self.taitoru_font.render("お手つき！", True, (0,0,0))
                    otetsuki_rect = otetsuki.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
                    self.window.blit(otetsuki, otetsuki_rect)
                    self.update_display()
                    pygame.time.wait(1000)

                elif self.mae_word[-1]== event.Text[0] and event.Text not in self.siritori_rekisi:
                    self.mae_word = event.Text
                    self.siritori_rekisi.append(event.Text)
                #elif self.otetuki_kaunto = [+1]

                else:
                    print("otetuki")
                    otetsuki = self.taitoru_font.render("お手つき！", True, (0,0,0))
                    otetsuki_rect = otetsuki.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
                    self.window.blit(otetsuki, otetsuki_rect)
                    self.update_display()
                    pygame.time.wait(1000)
                    # self.running = False

            # elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                # show_text(self.window, event.text)

            self.manager.process_events(event)

        # self.window.fill((100, 225, 255))
        self.text_box.update(events)
        text_box_rect = self.text_box.get_surface().get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
        self.window.blit(self.text_box.get_surface(), text_box_rect)


        time_delta = clock.tick(FPS)/ 1000.0
        moji = self.mae_word

        # self.manager.update(time_delta)
        # self.manager.draw_ui(self.window)
        bun_text = self.bun_font.render(self.mae_word, True, (10,10,10))
        bun_text_rect = bun_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2-100))
        #show_text(self.window, )
        self.window.blit(bun_text, bun_text_rect)
        # show_text(self.window, self.mae_word)


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

        # root.mainloop()
    def update_display(self):
        pygame.display.flip()
        pygame.display.update()

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
