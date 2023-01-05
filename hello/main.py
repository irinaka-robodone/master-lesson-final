import pygame
import pygame_gui
from pygame.locals import *
from text import Text


# def draw_text(text: str) -> None:


SCREEN_SIZE=(1200,860)

def init():
    pygame.init()
    pygame.display.set_caption("しりとりゲーム")
    Window = pygame.display.set_mode(SCREEN_SIZE)
    Window.fill((255,255,255))
def main():

    init()
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager(SCREEN_SIZE,"tema.json")
    input_text = pygame_gui.elements.UITextEntryLine(
        pygame.Rect(20,43,362,32),
        manager
    )

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
            # elif event.type == pygame.KEYDOWN and not text.is_editing:
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
        kankaku = clock.tick(60)/1000.0
        manager.update(kankaku)

main()
