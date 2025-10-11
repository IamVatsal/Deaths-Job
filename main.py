import time
import pygame
from player import Player

def clamp(value, min, max):
    if value < min:
        return min
    if value > max:
        return max
    return value


def main():
    pygame.init()

    # Window
    screen_width, screen_height = 864, 486
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Bird")
    window_icon = pygame.image.load('data/gfx/ghost.png').convert_alpha()
    pygame.display.set_icon(window_icon)

    # Backgraound Image
    bg_image = pygame.image.load('data/gfx/Clouds_1.png').convert_alpha()
    bg_image = pygame.transform.smoothscale(bg_image, (screen_width, screen_height))
    bg_width = bg_image.get_width()
    bg_x1 = 0
    bg_x2 = bg_width

    clock = pygame.time.Clock()
    running = True
    dt = 0

    player = Player()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_time = time.time()
                if (current_time - player.last_jump_time > player.jump_cooldown):
                    # player.position.y -= clamp(150 * dt, 0, screen.get_height() - player.height)  # Flap
                    player.velocity.y = player.jump_strength_up
                    player.velocity.x = player.jump_strength_forward
                    player.last_jump_time = current_time

        

        # Update Player Position with Gravity
        player.velocity.y += player.gravity * dt
        player.position.y += player.velocity.y * dt
        player.position.x += player.velocity.x * dt
        player.velocity.x = max(player.velocity.x - 200 * dt, -50)

        # Background Movement
        bg_x1 -= (35 * dt)
        bg_x2 -= (35 * dt)
        
        if bg_x1 <= -bg_width:
            bg_x1 = bg_x2 + bg_width
        if bg_x2 <= -bg_width:
            bg_x2 = bg_x1 + bg_width
        
        # Gravity Effect
        player.position.y = clamp(player.position.y, 0, screen_height - player.height)
        player.position.x = clamp(player.position.x, 0, screen_width - player.width)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.position.y = clamp(player.position.y - 400 * dt, 0, screen_height - player.height)
        if keys[pygame.K_s]:
            player.position.y = clamp(player.position.y + 400 * dt, 0, screen_height - player.height)
        if keys[pygame.K_a]:
            player.position.x = clamp(player.position.x - 300 * dt, 0, screen_width - player.width)
        if keys[pygame.K_d]:
            player.position.x = clamp(player.position.x + 300 * dt, 0, screen_width - player.width)
        
        screen.fill('purple')
        screen.blit(bg_image, (bg_x1, 0))
        screen.blit(bg_image, (bg_x2, 0))

        screen.blit(player.currentGhost, player.position)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()