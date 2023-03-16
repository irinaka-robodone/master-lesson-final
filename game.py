import wold
import pygame


SCREEN_SIZE = (960, 640)        # 全部大文字のやつ: 定数
def main():
    world =wold.World()
    player_image= pygame.image.load('asset/player.png', 'player-santa')
    world.add_player(player_image, [100,100])
    while world.running:
        world.process()


if __name__ == "__main__":
    main()
