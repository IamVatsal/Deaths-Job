import os
import time
import pygame
from Classes.Entity import Entity
from utils import clamp
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
# Player physics
PLAYER_SPRITE_PATH = os.getenv('PLAYER_SPRITE_PATH', 'data/gfx/ghost.png')
PLAYER_GRAVITY = int(os.getenv('PLAYER_GRAVITY', 800))
PLAYER_JUMP_STRENGTH_UP = int(os.getenv('PLAYER_JUMP_STRENGTH_UP', -250))
PLAYER_JUMP_STRENGTH_FORWARD = int(os.getenv('PLAYER_JUMP_STRENGTH_FORWARD', 50))
PLAYER_JUMP_COOLDOWN = float(os.getenv('PLAYER_JUMP_COOLDOWN', 0.05))
PLAYER_HORIZONTAL_DAMPING = int(os.getenv('PLAYER_HORIZONTAL_DAMPING', 200))
PLAYER_MIN_HORIZONTAL_VELOCITY = int(os.getenv('PLAYER_MIN_HORIZONTAL_VELOCITY', -50))

# Player movement
PLAYER_MOVE_SPEED_VERTICAL = int(os.getenv('PLAYER_MOVE_SPEED_VERTICAL', 400))
PLAYER_MOVE_SPEED_HORIZONTAL = int(os.getenv('PLAYER_MOVE_SPEED_HORIZONTAL', 300))

class Player(Entity):
    def __init__(self, x=84, y=92):
        # Initialize base Entity (no image path yet, we'll handle sprite loading custom)
        super().__init__(x, y)
        
        # Physics constants
        self.gravity = PLAYER_GRAVITY
        self.jump_strength_up = PLAYER_JUMP_STRENGTH_UP
        self.jump_strength_forward = PLAYER_JUMP_STRENGTH_FORWARD
        self.horizontal_damping = PLAYER_HORIZONTAL_DAMPING
        self.min_horizontal_velocity = PLAYER_MIN_HORIZONTAL_VELOCITY

        # Movement speeds
        self.move_speed_vertical = PLAYER_MOVE_SPEED_VERTICAL
        self.move_speed_horizontal = PLAYER_MOVE_SPEED_HORIZONTAL

        # Jump cooldown
        self.last_jump_time = 0
        self.jump_cooldown = PLAYER_JUMP_COOLDOWN

        # Initialize velocity
        self.velocity = pygame.Vector2(-50, 0)
        
        # Load and scale sprite
        self._load_sprite()
    
    def _load_sprite(self):
        """Load and prepare player sprites"""
        player_image = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.scaled_image = pygame.transform.smoothscale(
            player_image, 
            (player_image.get_width() // 4, player_image.get_height() // 4)
        )
        self.right_ghost = self.scaled_image
        self.left_ghost = pygame.transform.flip(self.right_ghost, True, False)
        self.current_ghost = self.right_ghost
        
        # Set dimensions (inherited from Entity)
        self.width = self.scaled_image.get_width()
        self.height = self.scaled_image.get_height()
        
        # Set the main image for Entity base class
        self.image = self.current_ghost
    
    def jump(self):
        """Make the player jump with cooldown"""
        current_time = time.time()
        if current_time - self.last_jump_time > self.jump_cooldown:
            self.velocity.y = self.jump_strength_up
            self.velocity.x = self.jump_strength_forward
            self.last_jump_time = current_time
    
    def handle_input(self, dt):
        """Handle keyboard input for movement"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.position.y -= self.move_speed_vertical * dt
        if keys[pygame.K_s]:
            self.position.y += self.move_speed_vertical * dt
        if keys[pygame.K_a]:
            self.position.x -= self.move_speed_horizontal * dt
            self.current_ghost = self.left_ghost
        if keys[pygame.K_d]:
            self.position.x += self.move_speed_horizontal * dt
            self.current_ghost = self.right_ghost
    
    def apply_physics(self, dt):
        """Apply gravity and velocity"""
        # Apply gravity
        self.velocity.y += self.gravity * dt
        
        # Update position
        self.position.y += self.velocity.y * dt
        self.position.x += self.velocity.x * dt
        
        # Apply horizontal damping
        self.velocity.x = max(
            self.velocity.x - self.horizontal_damping * dt, 
            self.min_horizontal_velocity
        )
    
    def clamp_to_screen(self, screen_width, screen_height):
        """Keep player within screen bounds"""
        self.position.x = clamp(self.position.x, 0, screen_width - self.width)
        self.position.y = clamp(self.position.y, 0, screen_height - self.height)
    
    def update(self, dt, screen_width, screen_height):
        """Update player state (overrides Entity.update)"""
        self.handle_input(dt)
        self.apply_physics(dt)
        self.clamp_to_screen(screen_width, screen_height)
    
    def draw(self, screen):
        """Render the player (overrides Entity.draw)"""
        screen.blit(self.current_ghost, self.position)
    
    # get_rect() is inherited from Entity, no need to redefine