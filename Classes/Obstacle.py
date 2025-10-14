import os
import pygame as pg
from Classes.Entity import Entity
from dotenv import load_dotenv

load_dotenv()

OBSTACLE_IMAGE_PATH = os.getenv("OBSTACLE_IMAGE_PATH", "data/gfx/fence.png")

class Obstacle(Entity):
    def __init__(self, x, y, speed = 35):
        super().__init__(x, y, image_path=OBSTACLE_IMAGE_PATH)
        self.speed = speed
        self.load_image(OBSTACLE_IMAGE_PATH)
        self.rect = pg.Rect(self.position.x, self.position.y, self.width, self.height)

        # temp variables for testing
        self.color = (255, 0, 0)  # Red color for the rectangle

    def load_image(self, path):
        """Load sprite image and scale it down"""
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.smoothscale(self.image, (self.image.get_width() // 2, self.image.get_height() // 1))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, dt):
        """Move the obstacle leftwards and update its rect"""
        self.position.x -= self.speed * dt
        self.rect.topleft = (int(self.position.x), int(self.position.y))
    
    def collides(self, is_colliding):
        if is_colliding:
            self.color = (0, 255, 0)  # Change color to green on collision
        else:
            self.color = (255, 0, 0)  # Change color back to red after collision

    def draw(self, screen):
        """Draw the obstacle as a colored rectangle"""
        pg.draw.rect(screen, self.color, self.rect)
        if self.image:
            screen.blit(self.image, self.rect)