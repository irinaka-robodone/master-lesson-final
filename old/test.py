from pygame.locals import *
import pygame

class Object():
    def __init__(self, rect: pygame.Rect, pos: list[float, float]) -> None:
        self.player_rect = rect
        self.pos = pos
        self.size = self.player_rect.get_size()
        self.dx = 0
        self.dy = 0

class Bullet(Object):
    def __init__(self, rect: pygame.Rect, pos: list[float, float]) -> None:
        super().__init__(rect, pos)

    def remove(self):
        """
        remove
        """

class World():
    def __init__(self) -> None:
        self.SCREENSIZE = (960, 480)
        self.TITLE = "見下ろし型シューティングゲーム"
        self.running = True
        self.current_scene = "start"
        self.FPS = 60
        self.clock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREENSIZE)       # 画面の初期化
        pygame.display.set_caption(self.TITLE)                  # ゲームタイトルとアイコンの初期化
        self.mouse_pos = (0,0)
        self.bullets = []

    def show_start_screen(self):
        self.screen.fill((255,255,255))

        self.render_text("シューティングゲーム", (self.SCREENSIZE[0]//2, self.SCREENSIZE[1]//2-40), 32, (0,0,0), bold=True)
        self.render_text("エンターキーを押してゲームスタート", (self.SCREENSIZE[0]//2, self.SCREENSIZE[1]//2+60), 16, (0,0,0))
        for event in pygame.event.get():

            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

                elif event.key == K_RETURN:
                    self.current_scene = "main"

    def add_player(self, player_rect: pygame.Rect, pos: list[float, float]):
        self.player = Object(player_rect, pos)

    def update_display(self):
        pygame.display.flip()
        pygame.display.update()

    def render_text(self, text, pos: tuple[int, int], size, color: tuple[int, int, int], font_name: str = "MS UI Gothic", bold = True, italic = False):
        font = pygame.font.SysFont(font_name, size, bold, italic)
        text = font.render(text, True, color)
        rect = text.get_rect()
        self.screen.blit(text, (pos[0]-rect.w//2, pos[1]-rect.h//2))

    def render_map(self):
        """
        render map
        """

    def render_object(self):
        self.screen.fill((255,255,255))
        """
        render object
        """
        self.screen.fill((0,0,0), (100, 100, 20, 20))
        self.screen.blit(self.player.player_rect, (self.player.pos[0],self.player.pos[1],self.player.size[0],self.player.size[1]))

    def process_event(self):

        for event in pygame.event.get():

            if event.type == QUIT:
                self.running = False

            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()

    def add_bullet(self, init_pos, size=(5,5)):

        self.append()
        self.bullets.append(pygame.Surface((5,5), masks=(255,0,0)))

    def update_pos(self):
        direction_key_any_down = False
        does_stop = False
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            if event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()

            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                    direction_key_any_down = True
                if event.key == K_LEFT:
                    self.player.dx = -2
                elif event.key == K_RIGHT:
                    self.player.dx = 2
                if event.key == K_UP:
                    self.player.dy = -2
                elif event.key == K_DOWN:
                    self.player.dy = 2

            elif event.type == KEYUP:
                self.player.dx = 0
                self.player.dy = 0

        # if not direction_key_any_down:
        #     self.player.dx = 0
        #     self.player.dy = 0

        self.player.pos[0] += self.player.dx
        self.player.pos[1] += self.player.dy

        distance = ((self.mouse_pos[0] - self.player.pos[0])**2 + (self.mouse_pos[1] - self.player.pos[1])**2 )**(1/2)
        self.bullet_direction = [(self.mouse_pos[0] - self.player.pos[0])/distance, (self.mouse_pos[1] - self.player.pos[1])/distance]
        print(self.bullet_direction)

    def render_bullet(self):
        bullet = pygame.Surface((20,20), masks=(255,0,0))
        self.screen.blit(bullet, (200,200,20,20))
        print(bullet)

    def process(self):
        self.clock.tick(self.FPS)

        if self.current_scene == "start":
            self.show_start_screen()
            self.update_display()
        elif self.current_scene == "main":
            self.render_map()
            self.update_pos()
            self.render_object()
            self.render_bullet()
            self.update_display()
            self.process_event()

def main():
    world = World()
    player_rect = pygame.image.load('asset/player_santa.png', 'player-santa')
    world.add_player(player_rect, [100,100])
    while world.running:
        world.process()

if __name__ == "__main__":
    main()