import random
import pygame as pg
from Classes.Env import OBSTACLE_HORIZONTAL_GAP_MAX, OBSTACLE_HORIZONTAL_GAP_MIN, OBSTACLE_VERTICAL_GAP_MAX, OBSTACLE_VERTICAL_GAP_MIN, SCREEN_HEIGHT, SCREEN_WIDTH
from Classes.Obstacle import Obstacle

class Obstacles:
    def __init__(self, num_of_obstacles=5):
        self.num_of_obstacles = num_of_obstacles
        self.obstacles_bottom = []
        self.obstacles_top = []
        self.screen_width = SCREEN_WIDTH
        self.min_y = SCREEN_HEIGHT // 2
        self.max_y = SCREEN_HEIGHT
        self.spawn_x_min = SCREEN_WIDTH // 2 + 100
        self.gap_size_x_min = OBSTACLE_HORIZONTAL_GAP_MIN
        self.gap_size_x_max = OBSTACLE_HORIZONTAL_GAP_MAX
        self.gap_size_y_min = OBSTACLE_VERTICAL_GAP_MIN
        self.gap_size_y_max = OBSTACLE_VERTICAL_GAP_MAX
        self.Obstacle_group = pg.sprite.Group()
        # Initial spawn 
        self._spawn_initial_obstacles()

    def _spawn_initial_obstacles(self):
        """Create initial obstacles with random gaps and positions"""
        current_x = self.spawn_x_min
        
        for i in range(self.num_of_obstacles):
            # Use current_x instead of calculating from i
            y_bottom = random.randrange(self.min_y, self.max_y)

            # Create bottom obstacle
            bottom_obstacle = Obstacle(current_x, y_bottom)
            self.Obstacle_group.add(bottom_obstacle)
            self.obstacles_bottom.append(bottom_obstacle)

            # Create top obstacle (above the bottom one with a gap)
            gap_size_y = random.randrange(self.gap_size_y_min, self.gap_size_y_max)
            y_top = y_bottom - gap_size_y - bottom_obstacle.height
            top_obstacle = Obstacle(current_x, y_top)
            self.Obstacle_group.add(top_obstacle)
            self.obstacles_top.append(top_obstacle)
            
            # Calculate next X position (add obstacle width + gap)
            gap_x = random.randrange(self.gap_size_x_min, self.gap_size_x_max)
            current_x += bottom_obstacle.width + gap_x

    def update(self, dt):
        """Update all obstacles and recycle if off-screen"""
        # Update both top and bottom obstacles together
        for i, (obstacle_bottom, obstacle_top) in enumerate(zip(self.obstacles_bottom, self.obstacles_top)):
            obstacle_bottom.update(dt)
            obstacle_top.update(dt)
            
        # THEN check if first obstacle is off-screen (don't modify during iteration)    
        if self.obstacles_bottom and self.obstacles_bottom[0].rect.right < 0:
            self.circulate_obstacles()

    def circulate_obstacles(self):
        """Move the first obstacle to the end of the list to create a continuous loop"""
        if self.obstacles_bottom and self.obstacles_top:

            # Remove first obstacles from both lists
            first_bottom = self.obstacles_bottom.pop(0)
            first_top = self.obstacles_top.pop(0)
            
            # Get the last obstacle's RIGHT edge
            last_obstacle_right = self.obstacles_bottom[-1].rect.right

            # Calculate new X position (SAME for both top and bottom)
            gap_x = random.randrange(self.gap_size_x_min, self.gap_size_x_max)
            new_x = last_obstacle_right + gap_x  # Add gap to RIGHT edge
            
            # Calculate new Y positions with vertical gap
            new_y_bottom = random.randrange(self.min_y, self.max_y)
            gap_y = random.randrange(self.gap_size_y_min, self.gap_size_y_max)
            new_y_top = new_y_bottom - gap_y - first_bottom.height
            
            # Update bottom obstacle
            first_bottom.position.x = new_x
            first_bottom.position.y = new_y_bottom
            first_bottom.rect.topleft = (int(first_bottom.position.x), int(first_bottom.position.y))
            
            # Update top obstacle
            first_top.position.x = new_x
            first_top.position.y = new_y_top
            first_top.rect.topleft = (int(first_top.position.x), int(first_top.position.y))
            
            # Add them back to the end
            self.obstacles_bottom.append(first_bottom)
            self.obstacles_top.append(first_top)

    def draw(self, screen):
        """Draw all obstacles"""
        for obstacle_bottom, obstacle_top in zip(self.obstacles_bottom, self.obstacles_top):
            obstacle_bottom.draw(screen)
            obstacle_top.draw(screen)

    def check_collisions(self, player):
        """Check collisions with all obstacles and return if any collision occurred"""
        collision_detected = False
        
        for obstacle_top, obstacle_bottom in zip(self.obstacles_top, self.obstacles_bottom):
            
            # Genral collision detection loop For Ractangles
            if player.rect.colliderect(obstacle_top.rect) or player.rect.colliderect(obstacle_bottom.rect):

                # Precise pixel-perfect collision detection
                if pg.sprite.spritecollide(player, self.Obstacle_group, False, pg.sprite.collide_mask):
                    collision_detected = True
                # Following lines are for debugging collision colors
                obstacle_top.collides(True)
                obstacle_bottom.collides(True)
            else:
                # Reset colors if no collision (for debugging)
                obstacle_top.collides(False)
                obstacle_bottom.collides(False)      

        return collision_detected
    
    def reset(self):
        """Reset all obstacles to initial positions"""
        self.obstacles_bottom.clear()
        self.obstacles_top.clear()
        self._spawn_initial_obstacles()  # Reuse the spawn logic