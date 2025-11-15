import time
import pygame as pg
from Classes.Entity import Entity
from Classes.Env import PLAYER_GRAVITY, PLAYER_HORIZONTAL_DAMPING, PLAYER_JUMP_COOLDOWN, PLAYER_JUMP_STRENGTH_FORWARD, PLAYER_JUMP_STRENGTH_UP, PLAYER_MIN_HORIZONTAL_VELOCITY, PLAYER_MOVE_SPEED_HORIZONTAL, PLAYER_MOVE_SPEED_VERTICAL, PLAYER_SPRITE_PATH, SCREEN_HEIGHT, SCREEN_WIDTH

class Player(Entity):
    def __init__(self, x = SCREEN_WIDTH // 2 - 100, y = SCREEN_HEIGHT // 2):
        super().__init__(x, y)
        
        # Physics constants
        self.gravity = PLAYER_GRAVITY
        self.jump_strength_up = PLAYER_JUMP_STRENGTH_UP
        self.jump_strength_forward = PLAYER_JUMP_STRENGTH_FORWARD
        self.horizontal_damping = PLAYER_HORIZONTAL_DAMPING
        self.min_horizontal_velocity = PLAYER_MIN_HORIZONTAL_VELOCITY
        self.move_speed_vertical = PLAYER_MOVE_SPEED_VERTICAL
        self.move_speed_horizontal = PLAYER_MOVE_SPEED_HORIZONTAL
        self.facing_right = True
        
        # Jump cooldown
        self.last_jump_time = 0
        self.jump_cooldown = PLAYER_JUMP_COOLDOWN
        
        # Velocity (inherited from Entity but reset initial value)
        self.velocity = pg.Vector2(-50, 0)
        
        # Load sprite AFTER Entity init
        self._load_sprite()
        
        # Create rect from position (SINGLE source of truth: self.position)
        self.rect = self.get_rect()

        self.mask = pg.mask.from_surface(self.image)
    
    def _load_sprite(self):
        """Load and prepare player sprites"""
        player_image = pg.image.load(PLAYER_SPRITE_PATH).convert_alpha()
        self.scaled_image = pg.transform.smoothscale(
            player_image, 
            (player_image.get_width() // 4, player_image.get_height() // 4)
        )
        self.right_ghost = self.scaled_image
        self.left_ghost = pg.transform.flip(self.right_ghost, True, False)
        if self.facing_right:
            self.current_ghost = self.right_ghost
        else:
            self.current_ghost = self.left_ghost
            self.facing_right = False

        self.width = self.scaled_image.get_width()
        self.height = self.scaled_image.get_height()
        self.image = self.current_ghost
    
    def jump(self):
        """Make the player jump with cooldown"""
        current_time = time.time()
        if current_time - self.last_jump_time > self.jump_cooldown:
            self.velocity.y = self.jump_strength_up
            if self.facing_right:
                self.velocity.x = abs(self.jump_strength_forward) + 20
            else:
                self.velocity.x = -abs(self.jump_strength_forward)
            self.last_jump_time = current_time
    
    def handle_input(self, dt):
        """Handle keyboard input for movement"""
        keys = pg.key.get_pressed()
        
        if keys[pg.K_a]:
            self.current_ghost = self.left_ghost
            self.image = self.current_ghost
            self.facing_right = False
        if keys[pg.K_d]:
            self.current_ghost = self.right_ghost
            self.image = self.current_ghost
            self.facing_right = True

    def apply_physics(self, dt):
        """Apply gravity and velocity"""
        # Apply gravity
        self.velocity.y += self.gravity * dt
        
        # Apply horizontal damping
        self.velocity.x = max(
            self.velocity.x - self.horizontal_damping * dt, 
            self.min_horizontal_velocity
        )
        
        # Update position based on velocity
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def clamp(self, value, min_value, max_value):
        if value < min_value:
            return min_value
        if value > max_value:
            return max_value
        return value

    def clamp_to_screen(self, screen_width, screen_height):
        """Keep player within screen bounds"""
        self.position.x = self.clamp(self.position.x, 0, screen_width - self.width)
        self.position.y = self.clamp(self.position.y, 0, screen_height - self.height)

    def sync_rect(self):
        """Sync rect with position (call AFTER all movement/collision)"""
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)
    
    def update(self, dt, screen_width, screen_height):
        """Update player state"""
        self.handle_input(dt)
        self.apply_physics(dt)
        self.clamp_to_screen(screen_width, screen_height)
        self.sync_rect()  # Sync rect at the END
    
    def reset(self):
        """Reset player to initial state"""
        self.position = pg.Vector2(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
        self.velocity = pg.Vector2(-50, 0)
        self.last_jump_time = 0
        self.current_ghost = self.right_ghost
        self.image = self.current_ghost
        self.facing_right = True
        self.rect = self.get_rect()
        
    def draw(self, screen):
        """Render the player"""
        # For debugging: draw rect
        pg.draw.rect(screen, (255, 0, 0), self.rect, 1)
        screen.blit(self.current_ghost, self.rect)
    
    def get_rect(self):
        """Return collision rectangle"""
        return pg.Rect(self.position.x, self.position.y, self.width, self.height)