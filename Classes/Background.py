import os
import pygame
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
# Screen settings
SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH', 864))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT', 486))
BACKGROUND_SCROLL_SPEED = int(os.getenv('BACKGROUND_SCROLL_SPEED', 35))
# Asset paths
BACKGROUND_IMAGE_PATH = os.getenv('BACKGROUND_IMAGE_PATH', 'data/gfx/Clouds_1.png')

class Background:
    def __init__(self, image_path = BACKGROUND_IMAGE_PATH, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT, scroll_speed = BACKGROUND_SCROLL_SPEED):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (screen_width, screen_height))
        self.width = self.image.get_width()
        self.scroll_speed = scroll_speed
        
        # Two positions for seamless scrolling
        self.x1 = 0
        self.x2 = self.width
    
    def update(self, dt):
        # Move both background images
        self.x1 -= self.scroll_speed * dt
        self.x2 -= self.scroll_speed * dt
        
        # Reset positions for infinite scroll
        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width
    
    def draw(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))