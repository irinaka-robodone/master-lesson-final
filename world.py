import pygame
from pygame.locals import *

pygame.init()
class Object():
    def __init__(self,image: pygame.Rect,pos:list[float,float]) -> None:
        self.image=image
        self.pos=pos
        
        self.dx=0
        self.dy=0
        self.picture_pos = [0,0]
        self.rect = self.image.subsurface(0,0,32,32)
        self.size=self.rect.get_size()
                    
        
        
class Bullet(Object):
    def __init__(self, rect: pygame.Rect, pos: list[float, float]) -> None:
        super().__init__(rect, pos)
    def remove(self):
        """
        remove
        """
        
class World():
    def __init__(self) -> None:
        self.SCREENSIZE = (960,480)
        self.TITLE ="シューティングゲーム"
        self.running=True
        self.current_scene="start"
        self.EPS=60
        self.anime_step = 0
        self.clock=pygame.time.Clock()
        pygame.init()
        
        self.screen =pygame.display.set_mode(self.SCREENSIZE)
        pygame.display.set_caption(self.TITLE)
        
        self.mouse_pos=(0,0)
        self.display=[]
    def render_text(self,text, pos: tuple[int,int], size, color: tuple[int,int,int],bold =True, italic=False):
        font = pygame.font.SysFont("MS UI Gothic",size, bold, italic)
        text = font.render(text, True, color)
        rect = text.get_rect()
        self.screen.blit(text, (pos[0]-rect.w//2, pos[1]- rect.h//2))
        
    def update_display(self):
        pygame.display.flip()
        pygame.display.update()
        
    def render_object(self):
        self.screen.fill((255,255,255))
            
        """
        render object
        """
        self.player.rect = self.player.image.subsurface(self.player.picture_pos[0], self.player.picture_pos[1], 32 , 32)
        self.screen.fill((0,0,0), (100, 100, 20, 20))
        self.screen.blit(self.player.rect,((self.player.pos[0],self.player.pos[1],self.player.size[0],self.player.size[1])))
    
    
    def add_player(self, player_rect: pygame.Rect, pos: list[float, float]):
        self.player = Object(player_rect, pos)
    def start_screen(self):
        self.screen.fill((255,255,255))
        
        # self.render_text("シューティングゲーム", (self.SCREENSIZE[0]//2,self.SCREENSIZE[1]//2-40), 32, (0,0,0))
        # self.render_text("エンターキーを押してゲームスタート",(self.SCREENSIZE[0]//2,self.SCREENSIZE[1]//2+60), 16, (0,0,0))
        
        self.render_text("shooting game", (self.SCREENSIZE[0]//2,self.SCREENSIZE[1]//2-40), 32, (0,0,0))
        self.render_text("Press Enter to start!",(self.SCREENSIZE[0]//2,self.SCREENSIZE[1]//2+60), 16, (0,0,0))
        #
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.running =False
                
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                
                elif event.key == K_RETURN:
                    self.current_scene= "main"
                    

    def update_pos(self):
        self.screen.fill((255,255,255))
        
        direction_key_any_down = False
        does_stop = False
    
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.running =False
            
            # elif event.type ==MOUSEBUTTONDOWN:
            #     self.mouse_pos =pygame.mouse.get_pos()
            
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                    direction_key_any_down = True
                if event.key == K_a:
                    self.player.dx = -2
                    self.player.picture_pos = [0,32]
                if event.key == K_d:
                    self.player.dx = 2
                    self.player.picture_pos = [0,64]
                if event.key == K_w:
                    self.player.dy = -2
                    self.player.picture_pos = [0,96]
                if event.key == K_s:
                    self.player.dy = 2
                    self.player.picture_pos =[0,0]
            
            elif event.type ==KEYUP:
                self.player.dx =0
                self.player.dy =0
        # print(self.player.dx, self.player.dy)
        
        self.player.pos[0] += self.player.dx
        self.player.pos[1] += self.player.dy

        distance = ((self.mouse_pos[0] - self.player.pos[0])**2 +(self.mouse_pos[1] - self.player.pos[1])**2)**(1/2)
        self.bullet_direction = [(self.mouse_pos[0] - self.player.pos[0])/distance, (self.mouse_pos[1] - self.player.pos[1])/distance]
        print(self.bullet_direction)
                
    def add_bullet(self, init_pos, size=(5,5)):

        self.append()
        self.bullets.append(pygame.Surface((5,5), masks=(255,0,0)))
        
    def animation(self):
        self.anime_step +=0.1
        if self.anime_step > 2:
            self.anime_step =0
        print(30*int(self.anime_step))
        self.player.picture_pos = (30 * int(self.anime_step), self.player.picture_pos[1]) 
        
    def render_bullet(self):
        bullet= pygame.Surface((20,20), masks=(255,0,0))
        self.screen.blit(bullet, (200,200,20,20))
        print(bullet)
    
    def render_map(self):
        """
        """
    
    def process_event(self):
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.running = False
            
            
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
        

    def process(self):
        self.clock.tick(60)
        if self.current_scene=="start":
            self.start_screen()
            self.update_display()
        elif self.current_scene == "main":
            # self.render_map()
            self.update_pos()
            self.render_object()
            self.update_display()
            self.animation()
            # self.render_bullet()
            # self.process_event()