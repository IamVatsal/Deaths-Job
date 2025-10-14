import pygame as pg
import os
from Classes.Obstacle import Obstacle
from Classes.Player import Player
from Classes.Background import Background
from Classes.SplashScreen import SplashScreen
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
# Screen settings
SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH', 864))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT', 486))
FPS = int(os.getenv('FPS', 60))
WINDOW_TITLE = os.getenv('WINDOW_TITLE', "Death's Job")

# Asset paths
GHOST_SPRITE_PATH = os.getenv('GHOST_SPRITE_PATH', 'data/gfx/ghost.png')
BACKGROUND_PATH = os.getenv('BACKGROUND_PATH', 'data/gfx/Clouds_1.png')


class Game1:
    def __init__(self):
        pg.init()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption(WINDOW_TITLE)
        
        # Load window icon
        window_icon = pg.image.load(GHOST_SPRITE_PATH).convert_alpha()
        pg.display.set_icon(window_icon)
        
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 0
        
        # Game objects
        self.player = Player(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 100)
        self.background = Background(BACKGROUND_PATH, self.screen_width, self.screen_height)

        # Game Objects
        self.obstacle = Obstacle(500, 400)

        # Splash Screen
        self.SplashScreen = SplashScreen(self.screen_width, self.screen_height)

        self.current_screen = 'splash'

        
    def handle_events(self):
        # if self.current_screen == 'splash':
        #     for event in pg.event.get():
        #         if event.type == pg.QUIT:
        #             self.running = False
        #         elif event.type == pg.MOUSEBUTTONDOWN:
        #             if self.SplashScreen.collide(event.pos):
        #                 self.current_screen = 'game'
        #     return

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.current_screen == 'splash' and self.SplashScreen.collide(event.pos):
                    self.current_screen = 'game'
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_ESCAPE:
                    self.current_screen = 'splash'

        if self.player.rect.colliderect(self.obstacle.rect):
            self.obstacle.collides(True)
            self.current_screen = 'splash'
            self.player.reset()
            # print("Collision detected!")
            # self.running = False
        else:
            self.obstacle.collides(False)
            
    
    def update(self):
        if self.current_screen == 'splash':
                self.SplashScreen.collide(pg.mouse.get_pos())
        else:
            # Update player
            self.player.update(self.dt, self.screen_width, self.screen_height)
            
            # Update obstacle
            self.obstacle.update(self.dt)
            
            # Update background
            self.background.update(self.dt)
    
    def render(self):
        if self.current_screen == 'splash':
            self.SplashScreen.draw(self.screen)
        else:
            self.screen.fill('purple')
            self.background.draw(self.screen)
            pg.draw.rect(self.screen, (255, 0, 0), self.player.rect, 1)
            self.player.draw(self.screen)
            self.obstacle.draw(self.screen)
        pg.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.dt = self.clock.tick(FPS) / 1000
        
        pg.quit()