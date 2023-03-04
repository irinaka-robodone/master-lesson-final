import pygame

from world import World

def main():
    world = World()
    player_rect = pygame.image.load('asset/player_santa.png', 'player-santa')
    world.add_player(player_rect, [100,100])
    while world.running:
        world.process()
    
if __name__ == "__main__":
    main()