import pygame
import os
from Classes.Obstacle import Obstacle
from Classes.Player import Player
from Classes.Background import Background
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


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(WINDOW_TITLE)
        
        # Load window icon
        window_icon = pygame.image.load(GHOST_SPRITE_PATH).convert_alpha()
        pygame.display.set_icon(window_icon)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        
        # Game objects
        self.player = Player(84, 92)
        self.background = Background(BACKGROUND_PATH, self.screen_width, self.screen_height)

        # Game Objects
        self.obstacle = Obstacle(500, 400)

        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

        if self.player.rect.colliderect(self.obstacle.rect):
            self.obstacle.collides(True)
            # print("Collision detected!")
            # self.running = False
        else:
            self.obstacle.collides(False)
            
    
    def update(self):
        # Update player
        self.player.update(self.dt, self.screen_width, self.screen_height)
        
        # Update obstacle
        self.obstacle.update(self.dt)
        
        # Update background
        self.background.update(self.dt)
    
    def render(self):
        self.screen.fill('purple')
        self.background.draw(self.screen)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.rect, 1)
        self.player.draw(self.screen)
        self.obstacle.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.dt = self.clock.tick(FPS) / 1000
        
        pygame.quit()