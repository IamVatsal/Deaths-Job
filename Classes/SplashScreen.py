import os
import pygame as pg
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
SPLASH_SCREEN_BG = os.getenv('SPLASH_SCREEN_BG', 'data/gfx/castle.png')

class SplashScreen():
    def __init__(self, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT):
        self.bg = pg.image.load(SPLASH_SCREEN_BG).convert_alpha()
        self.st_button = pg.Rect((SCREEN_WIDTH / 2) - 50, (SCREEN_HEIGHT / 2) - 25, 100, 50)
        self.bg_scaled = pg.transform.smoothscale(self.bg, (screen_width, screen_height))
        self.st_button_color = (0, 255, 0)  # Green color for the button
        self.mouse_pos = pg.Rect(0, 0, 1, 1)
        self.x = 0
        self.y = 0

    def collide(self, mouse_pos):
        self.mouse_pos.topleft = mouse_pos
        if self.mouse_pos.colliderect(self.st_button):
            self.st_button_color = (255, 0, 0)  # Change button color to red on hover
            return True
        self.st_button_color = (0, 255, 0)  # Reset button color to green
        return False

    def draw(self, screen):
        screen.blit(self.bg_scaled, (self.x, self.y))
        pg.draw.rect(screen, self.st_button_color, self.st_button)