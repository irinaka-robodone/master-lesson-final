
from pygame.locals import *
import pygame

class Object():
    def __init__(self, rect: pygame.Rect, pos: list[float, float]) -> None:
        self.player_rect = rect
        self.pos = pos
        self.size = self.player_rect.get_size()
        self.dx = 0
        self.dy = 0
        
class Bullet():
    def __init__(self, rect: pygame.Rect, pos: list[float, float], dx, dy) -> None:
        self.rect = rect
        self.pos = pos
        self.size = self.rect.get_size()
        self.dx = dx
        self.dy = dy
    
    def remove(self):
        """
        remove
        """
        # del self
        # return True

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

        for i, bullet in enumerate(self.bullets):
            print(f"{i+1}/{len(self.bullets)}, {bullet}")
            self.screen.blit(bullet.rect, (bullet.pos[0], bullet.pos[1], bullet.size[0], bullet.size[1]))
        
    def process_event(self):
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.running = False
                
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
    
    def add_bullet(self, bullet: Bullet):
        
        self.bullets.append(bullet)

    def update_pos(self):
        direction_key_any_down = False
        does_stop = False
        
        distance = ((self.mouse_pos[0] - self.player.pos[0])**2 + (self.mouse_pos[1] - self.player.pos[1])**2 )**(1/2)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

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
                elif event.key == K_ESCAPE:
                    self.running = False
                    
                if event.key == K_SPACE:
                    self.mouse_pos = pygame.mouse.get_pos()
                    bullet_direction = [(self.mouse_pos[0] - self.player.pos[0])/distance, (self.mouse_pos[1] - self.player.pos[1])/distance]
                    # rect = pygame.Surface((20,20))
                    # bullet = Bullet(rect, self.player.pos, bullet_dx, bullet_dy)
                    self.add_bullet(Bullet(pygame.Surface((5,5), masks=(255,0,0)), self.player.pos, bullet_direction[0], bullet_direction[1]))
                    print(len(self.bullets), bullet_direction)
                    
            elif event.type == KEYUP:
                self.player.dy = 0
                self.player.dx = 0

        # print(self.mouse_pos)
            # elif event.type == KEYUP:
            #     self.player.dx = 0
            #     self.player.dy = 0
                    
        # if not direction_key_any_down:
        #     self.player.dx = 0
        #     self.player.dy = 0
        
        self.player.pos[0] += self.player.dx
        self.player.pos[1] += self.player.dy

        if len(self.bullets) > 0:
            for bullet in self.bullets:
                bullet.pos[0] += bullet.dx
                bullet.pos[1] += bullet.dy
        # print(self.bullet_direction)
        
    # def render_bullet(self):
    #     bullet = pygame.Surface((20,20), masks=(255,0,0))
    #     self.screen.blit(bullet, (200,200,20,20))
    #     print(bullet)
    
    def process(self):
        self.clock.tick(self.FPS)
        
        if self.current_scene == "start":
            self.show_start_screen()
            self.update_display()
        elif self.current_scene == "main":
            self.render_map()
            self.update_pos()
            self.render_object()
            # self.render_bullet()
            self.update_display()
            self.process_event()