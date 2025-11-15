import pygame as pg

class Button:
    def __init__(self, x, y, image_path=None, hover_image_path=None):
        if image_path:
            self.load_image(image_path)
        if hover_image_path:
            self.hover_image = pg.image.load(hover_image_path).convert_alpha()
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.hover_flag = False

    def load_image(self, path):
        """Load Button image"""
        self.image = pg.image.load(path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def scale(self, width, height):
        """Scale button image"""
        self.image = pg.transform.smoothscale(self.image, (width, height))
        if self.hover_image:
            self.hover_image = pg.transform.smoothscale(self.hover_image, (width, height))
        self.width = width
        self.height = height
        self.rect.width = width
        self.rect.height = height

    def draw(self, screen):
        if self.hover_flag and self.hover_image:
            screen.blit(self.hover_image, self.rect)
        elif self.image:
            screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hover_flag = True
        else:
            self.hover_flag = False
        return self.rect.collidepoint(mouse_pos)