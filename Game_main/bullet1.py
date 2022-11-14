import pygame
from pygame.sprite import Sprite


class Bullet1(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet1_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet1_width,
                                self.settings.bullet1_height)
        self.rect.midleft = ai_game.character.rect.midleft

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.bullet1_speed
        self.rect.x = self.x

    def draw_bullet1(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
