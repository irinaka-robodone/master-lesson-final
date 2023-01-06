import pygame
import sys
from pygame.locals import *
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
        new_text = pygame.font.SysFont("Noto Sans JP", 20).render(text, True, (10,10,10))
        new_text_rect = new_text.get_rect(center=(SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
        window.blit(new_text, new_text_rect)
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
    manager = pygame_gui.UIManager(
        SCREEN_SIZE,
        theme_path="theme.json"
    )
    input_box = pygame_gui.elements.UITextEntryLine(
        pygame.Rect(SCREEN_SIZE[0]//2 - 500//2, SCREEN_SIZE[1]//2 - 30//2, 500, 40),
        manager,
        object_id="#main_text_entry"
    )

    running = True 
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == 96:
                    print("Pressed!")
                    
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                show_text(window, event.text)
            manager.process_events(event)
        
        time_delta = clock.tick(FPS)/ 1000.0
        manager.update(time_delta)
        manager.draw_ui(window)
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


main()