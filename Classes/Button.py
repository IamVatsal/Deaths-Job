import pygame as pg

class Button:
    def __init__(self, x, y, image_path=None):
        if image_path:
            self.load_image(image_path)
        self.rect = pg.Rect(x, y, self.width, self.height)

    def load_image(self, path):
        """Load Button image"""
        self.image = pg.image.load(path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def scale(self, width, height):
        """Scale button image"""
        self.image = pg.transform.smoothscale(self.image, (width, height))
        self.width = width
        self.height = height
        self.rect.width = width
        self.rect.height = height

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)