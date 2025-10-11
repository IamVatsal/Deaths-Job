import pygame

class Entity:
    """Base class for game entities"""
    def __init__(self, x, y, image_path=None):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.image = None
        self.width = 0
        self.height = 0
        
        if image_path:
            self.load_image(image_path)
    
    def load_image(self, path):
        """Load sprite image"""
        self.image = pygame.image.load(path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def update(self, dt):
        """Override in subclasses"""
        pass
    
    def draw(self, screen):
        """Render the entity"""
        if self.image:
            screen.blit(self.image, self.position)
    
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.position.x, self.position.y, self.width, self.height)