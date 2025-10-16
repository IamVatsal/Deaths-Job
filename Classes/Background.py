import pygame as pg
from Classes.Env import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE_PATH, BACKGROUND_SCROLL_SPEED

class Background:
    def __init__(self, image_path = BACKGROUND_IMAGE_PATH, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT, scroll_speed = BACKGROUND_SCROLL_SPEED):
        self.image = pg.image.load(image_path).convert_alpha()
        self.image = pg.transform.smoothscale(self.image, (screen_width, screen_height))
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