import pygame as pg
from Classes.Obstacles import Obstacles
from Classes.Player import Player
from Classes.Background import Background
from Classes.SplashScreen import SplashScreen
from Classes.Env import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WINDOW_TITLE, GHOST_SPRITE_PATH, BACKGROUND_PATH
from Classes.GameState import GameState

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
        # self.obstacle = Obstacle(500, 400)
        self.obstacles = Obstacles(num_of_obstacles=10)

        # Splash Screen
        self.SplashScreen = SplashScreen(self.screen_width, self.screen_height)

        self.current_state = GameState.SPLASH
        self.current_screen = 'splash'

        
    def handle_events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.current_state == GameState.SPLASH and self.SplashScreen.collide(event.pos):
                    self.current_state = GameState.PLAYING
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE: 
                    if self.current_state == GameState.PLAYING:
                        self.player.jump()
                    if self.current_state == GameState.SPLASH:
                        self.current_state = GameState.PLAYING
                if event.key == pg.K_ESCAPE:
                    if self.current_state == GameState.PLAYING:
                        self.current_state = GameState.SPLASH
                    elif self.current_state == GameState.SPLASH:
                        self.running = False

    def update(self):
        if self.current_state == GameState.SPLASH:
            self.SplashScreen.collide(pg.mouse.get_pos())
        else:
            # Update player
            self.player.update(self.dt, self.screen_width, self.screen_height)
            
            # Update obstacle
            self.obstacles.update(self.dt)
            
            # Update background
            self.background.update(self.dt)

            if self.obstacles.check_collisions(self.player.rect):
                self.current_state = GameState.SPLASH
                self.player.reset()
                self.obstacles.reset()
                # print("Collision detected!")
                # self.running = False
    
    def render(self):
        if self.current_state == GameState.SPLASH:
            self.SplashScreen.draw(self.screen)
        else:
            self.screen.fill('purple')
            self.background.draw(self.screen)
            self.player.draw(self.screen)
            self.obstacles.draw(self.screen)
        pg.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.dt = self.clock.tick(FPS) / 1000
        
        pg.quit()