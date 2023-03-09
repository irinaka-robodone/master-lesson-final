import pygame
from pygame.locals import *
import tkinter as tk

pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('日本語入力テスト')

# テキストボックスのサイズ
TEXTBOX_WIDTH = 200
TEXTBOX_HEIGHT = 30

# テキストボックスのフォント
font = pygame.font.SysFont('Arial', 24)

# テキストボックスの背景色
bg_color = (255, 255, 255)

# テキストボックスの表示位置
textbox_x = (WINDOW_WIDTH - TEXTBOX_WIDTH) // 2
textbox_y = (WINDOW_HEIGHT - TEXTBOX_HEIGHT) // 2

# テキストボックスの作成
textbox = tk.Entry(window, font=('Arial', 24), bg='white')
textbox.place(x=textbox_x, y=textbox_y, width=TEXTBOX_WIDTH, height=TEXTBOX_HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # テキストボックスの値を取得
    text = textbox.get()

    # テキストを描画
    text_surface = font.render(text, True, (0, 0, 0))
    window.fill(bg_color)
    window.blit(text_surface, (textbox_x, textbox_y))

    pygame.display.update()
