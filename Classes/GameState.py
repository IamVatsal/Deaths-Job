from enum import Enum

class GameState(Enum):
    SPLASH = 'splash'
    PLAYING = 'playing'
    PAUSED = 'paused'
    GAME_OVER = 'game_over'
    EXIT = 'exit'