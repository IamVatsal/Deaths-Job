import pygame

class Player:
    def __init__(self):
        self.position = pygame.Vector2(84, 92)
        self.velocity = pygame.Vector2(-35, 0)
        # self.acceleration = 0.1
        self.player_image = pygame.image.load('data/gfx/ghost.png').convert_alpha()
        self.scaled_image = pygame.transform.smoothscale(
            self.player_image, 
            (self.player_image.get_width() // 4, self.player_image.get_height() // 4)
        )
        self.rightGhost = self.scaled_image
        self.leftGhost = pygame.transform.flip(self.rightGhost, True, False)
        self.currentGhost = self.rightGhost
        self.height = self.scaled_image.get_height()
        self.width = self.scaled_image.get_width()


        self.last_jump_time = 0
        self.jump_cooldown = 0.05


        self.velocity.x = -50
        self.velocity.y = 0
        self.gravity = 800  # Increased gravity for a snappier feel
        self.jump_strength_up = -250
        self.jump_strength_forward = 50