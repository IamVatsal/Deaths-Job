import pygame as pg
from Classes.Entity import Entity
from Classes.Env import OBSTACLE_IMAGE_PATH

class Obstacle(Entity):
    def __init__(self, x, y, speed = 35):
        super().__init__(x, y)
        self.speed = speed
        self.load_image(OBSTACLE_IMAGE_PATH)
        self.rect = pg.Rect(self.position.x, self.position.y, self.width, self.height)
        self.mask = pg.mask.from_surface(self.image)

    def load_image(self, path):
        """Load sprite image and scale it down"""
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.smoothscale(self.image, (self.image.get_width() // 3, self.image.get_height() // 3))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, dt):
        """Move the obstacle leftwards and update its rect"""
        self.position.x -= self.speed * dt
        self.rect.topleft = (int(self.position.x), int(self.position.y))

    def draw(self, screen):
        """Draw the obstacle"""
        # Draw image
        if self.image:
            screen.blit(self.image, self.rect)