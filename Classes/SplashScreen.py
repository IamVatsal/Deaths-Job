import pygame as pg
from Classes.Env import SCREEN_WIDTH, SCREEN_HEIGHT, SPLASH_SCREEN_BG, START_BUTTON_IMAGE, EXIT_BUTTON_IMAGE, START_BUTTON_HOVER_IMAGE, EXIT_BUTTON_HOVER_IMAGE
from Classes.Button import Button
from Classes.GameState import GameState

class SplashScreen():
    def __init__(self, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT):
        self.bg = pg.image.load(SPLASH_SCREEN_BG).convert_alpha()
        self.bg_scaled = pg.transform.smoothscale(self.bg, (screen_width, screen_height))
        self.start_button = Button((SCREEN_WIDTH / 2) - 60, (SCREEN_HEIGHT / 2) - 200, START_BUTTON_IMAGE, START_BUTTON_HOVER_IMAGE)
        self.exit_button = Button((SCREEN_WIDTH / 2) - 60, (SCREEN_HEIGHT / 2) - 100, EXIT_BUTTON_IMAGE, EXIT_BUTTON_HOVER_IMAGE)
        self.start_button.scale(100, 50)
        self.exit_button.scale(100, 50)
        self.mouse_pos = pg.Rect(0, 0, 1, 1)
        self.x = 0
        self.y = 0

    def collide(self, mouse_pos):
        self.mouse_pos.topleft = mouse_pos
        if self.start_button.is_clicked(mouse_pos):
            return GameState.PLAYING
        if self.exit_button.is_clicked(mouse_pos):
            return GameState.EXIT
        return False

    def draw(self, screen):
        screen.blit(self.bg_scaled, (self.x, self.y))
        self.start_button.draw(screen)
        self.exit_button.draw(screen)