import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Suppress pygame welcome message

# Screen settings
SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH', '1296'))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT', '729'))
FPS = int(os.getenv('FPS', '60'))
WINDOW_TITLE = os.getenv('WINDOW_TITLE', "Death's Job")

# Background environment variables
BACKGROUND_SCROLL_SPEED = int(os.getenv('BACKGROUND_SCROLL_SPEED', '35'))

# Asset paths
# Graphics paths
GHOST_SPRITE_PATH = os.getenv('GHOST_SPRITE_PATH', 'data/gfx/ghost.png')
BACKGROUND_PATH = os.getenv('BACKGROUND_PATH', 'data/gfx/background.png')
OBSTACLE_IMAGE_PATH = os.getenv("OBSTACLE_IMAGE_PATH", "data/gfx/poll_new.png")
SPLASH_SCREEN_BG = os.getenv('SPLASH_SCREEN_BG', 'data/gfx/back.png')
START_BUTTON_IMAGE = os.getenv('START_BUTTON_IMAGE', 'data/gfx/start_button_normal.png')
EXIT_BUTTON_IMAGE = os.getenv('EXIT_BUTTON_IMAGE', 'data/gfx/exit_button_normal.png')
START_BUTTON_HOVER_IMAGE = os.getenv('START_BUTTON_HOVER_IMAGE', 'data/gfx/start_button_hover.png')
EXIT_BUTTON_HOVER_IMAGE = os.getenv('EXIT_BUTTON_HOVER_IMAGE', 'data/gfx/exit_button_hover.png')

# Sound paths
JUMP_SOUND_PATH = os.getenv('JUMP_SOUND_PATH', 'data/sfx/flap.wav')
BUTTON_CLICK_SOUND_PATH = os.getenv('BUTTON_CLICK_SOUND_PATH', 'data/sfx/button_click.wav')
COLLISION_SOUND_PATH = os.getenv('COLLISION_SOUND_PATH', 'data/sfx/collision_sound.wav')
BACKGROUND_MUSIC_PATH = os.getenv('BACKGROUND_MUSIC_PATH', 'data/sfx/bgm-blues-guitar-loop-192099.mp3')

# Player environment variables
PLAYER_SPRITE_PATH = os.getenv('PLAYER_SPRITE_PATH', 'data/gfx/ghost.png')
PLAYER_GRAVITY = int(os.getenv('PLAYER_GRAVITY', '800'))
PLAYER_JUMP_STRENGTH_UP = int(os.getenv('PLAYER_JUMP_STRENGTH_UP', '-200'))
PLAYER_JUMP_STRENGTH_FORWARD = int(os.getenv('PLAYER_JUMP_STRENGTH_FORWARD', '50'))
PLAYER_JUMP_COOLDOWN = float(os.getenv('PLAYER_JUMP_COOLDOWN', '0.05'))
PLAYER_HORIZONTAL_DAMPING = int(os.getenv('PLAYER_HORIZONTAL_DAMPING', '200'))
PLAYER_MIN_HORIZONTAL_VELOCITY = int(os.getenv('PLAYER_MIN_HORIZONTAL_VELOCITY', '-50'))
PLAYER_MOVE_SPEED_VERTICAL = int(os.getenv('PLAYER_MOVE_SPEED_VERTICAL', '400'))
PLAYER_MOVE_SPEED_HORIZONTAL = int(os.getenv('PLAYER_MOVE_SPEED_HORIZONTAL', '300'))

# Obstacle environment variables
OBSTACLE_HORIZONTAL_GAP_MIN = int(os.getenv('OBSTACLE_HORIZONTAL_GAP_MIN', '150'))
OBSTACLE_HORIZONTAL_GAP_MAX = int(os.getenv('OBSTACLE_HORIZONTAL_GAP_MAX', '250'))
OBSTACLE_VERTICAL_GAP_MIN = int(os.getenv('OBSTACLE_VERTICAL_GAP_MIN', '250'))
OBSTACLE_VERTICAL_GAP_MAX = int(os.getenv('OBSTACLE_VERTICAL_GAP_MAX', '350'))