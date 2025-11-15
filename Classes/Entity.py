import pygame as pg

class Entity(pg.sprite.Sprite):
    """Base class for game entities"""
    def __init__(self, x, y, image_path=None):
        super().__init__()
        # Use Vector2 for precise float position
        self.position = pg.Vector2(float(x), float(y))
        self.velocity = pg.Vector2(0, 0)
        self.image = None
        self.width = 0
        self.height = 0
        
        if image_path:
            self.load_image(image_path)
    
    def load_image(self, path):
        """Load sprite image"""
        self.image = pg.image.load(path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def update(self, dt):
        """Override in subclasses"""
        pass
    
    def draw(self, screen):
        """Render the entity"""
        if self.image:
            screen.blit(self.image, (int(self.position.x), int(self.position.y)))
    
    def get_rect(self):
        """Get collision rectangle"""
        return pg.Rect(int(self.position.x), int(self.position.y), self.width, self.height)