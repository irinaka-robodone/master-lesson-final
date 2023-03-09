def draw_text(text: str) -> None:
    """
    入力文字を描画するための関数
    """
    text_surface = font.render(text, True, (0, 0, 0))
    screen.fill((112, 225, 112))
    # テキストに応じて上下左右中央揃えにする
    center_w = (800 / 2) - (text_surface.get_width() / 2)
    center_h = (600 / 2) - (text_surface.get_height() / 2)
    screen.blit(text_surface, (center_w, center_h))
    pygame.display.update()