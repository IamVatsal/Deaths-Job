import pygame as pg
from Classes.Obstacles import Obstacles
from Classes.Player import Player
from Classes.Background import Background
from Classes.SplashScreen import SplashScreen
from Classes.Env import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WINDOW_TITLE, GHOST_SPRITE_PATH, BACKGROUND_PATH, BACKGROUND_MUSIC_PATH, BUTTON_CLICK_SOUND_PATH
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
        self.obstacles = Obstacles(num_of_obstacles=10)

        # Splash Screen
        self.SplashScreen = SplashScreen(self.screen_width, self.screen_height)
        self.current_state = GameState.SPLASH

        # Game Restart Timer
        self.restart_timer = 0

        # Sound
        pg.mixer.init()
        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.mixer.music.load(BACKGROUND_MUSIC_PATH)
        pg.mixer.music.play(-1)
        self.button_click_sound = pg.mixer.Sound(BUTTON_CLICK_SOUND_PATH)
        
    def handle_events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.current_state == GameState.SPLASH and self.SplashScreen.collide(event.pos) == GameState.PLAYING:
                    self.button_click_sound.play()
                    self.current_state = GameState.PLAYING
                elif self.current_state == GameState.SPLASH and self.SplashScreen.collide(event.pos) == GameState.EXIT:
                    self.button_click_sound.play()
                    self.running = False
                elif self.current_state == GameState.PLAYING:
                    self.player.jump()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE: 
                    if self.current_state == GameState.PLAYING:
                        self.player.jump()
                    if self.current_state == GameState.SPLASH and self.restart_timer <= 0:
                        self.current_state = GameState.PLAYING
                        self.button_click_sound.play()
                if event.key == pg.K_ESCAPE:
                    if self.current_state == GameState.PLAYING:
                        self.current_state = GameState.SPLASH
                    elif self.current_state == GameState.SPLASH:
                        self.running = False

    def update(self):
        if self.current_state == GameState.SPLASH:
            self.SplashScreen.collide(pg.mouse.get_pos())
            self.restart_timer = max(0, self.restart_timer - 1)
        else:
            # Update player
            self.player.update(self.dt, self.screen_width, self.screen_height)
            
            # Update obstacle
            self.obstacles.update(self.dt)
            
            # Update background
            self.background.update(self.dt)

            if self.obstacles.check_collisions(self.player):
                self.current_state = GameState.SPLASH
                self.player.reset()
                self.obstacles.reset()
                self.restart_timer = 20 # Small delay before restarting
    
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