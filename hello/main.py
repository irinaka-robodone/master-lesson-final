import pygame
import pygame_gui
import sys
from pygame.locals import *
from text import Text


# def draw_text(text: str) -> None:


SCREEN_SIZE=(1200,600)
FPS = 60
clock = pygame.time.Clock()

def show_text(window,text):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.fill((255,255,255))
        new_text = pygame.font.SysFont("Noto sans JP",20).rander(text,True,(10,10,10))
        new_text_rect = new_text.get_rect(center=(SCREEN_SIZE[0]//2,SCREEN_SIZE[1]//2))
        window.blit(new_text,new_text_rect)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


def init():
    pygame.init()
    pygame.display.set_caption("しりとりゲーム")
    window = pygame.display.set_mode(SCREEN_SIZE)
    window.fill((255,255,255))

    return window
def main():

    window = init()
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager(SCREEN_SIZE,"tema.json")
    input_text = pygame_gui.elements.UITextEntryLine(
        pygame.Rect(20,43,362,32),
        manager
    )
    imput_box = pygame_gui.elements.UITextEntryLine(
        pygame.Rect(SCREEN_SIZE[0]//2 - 500//2,SCREEN_SIZE[1]//2 - 30//2,500,40
    ),manager,object_id="#main_text_entry")

    running = True
    while running:
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == 96:
                    print("osareta!")


            elif event.type == pygame_gui.UI_TEXT_EFFECT_FINISHED and event.ui_object_id == "#main_text_entry":
                show_text(window,event.text)
            manager.process_events(event)

        time_delta = clock.tick(FPS)/ 100.0
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)
            #     if event.key in event_trigger.keys():
            #         input_text = pygame.event_trigger[event.key]()
            #     # 入力の確定
            #     if event.unicode in ("\r", "") and event.key == pygame.K_RETURN:
            #         print(input_text)  # 確定した文字列を表示
            #         draw_text(format(text))  # テキストボックスに"|"を表示
            #         input_text = format(text)  # "|"に戻す
            #         break
            # elif event.type == pygame. TEXTEDITING:  # 全角入力
            #     input_text =  pygame. pygame.text.edit(event.text, event.start)
            # elif event.type == pygame.TEXTINPUT:  # 半角入力、もしくは全角入力時にenterを押したとき
            #     input_text =  pygame.text.input(event.text)
            # # 描画しなおす必要があるとき
            # if event.type in [KEYDOWN, TEXTEDITING, TEXTINPUT]:
            #     draw_text(input_text)
        kankaku = clock.tick(60)/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000.00000000000000000000000000000000000000000000000000001
        manager.update(kankaku)

main()
