import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = ai_game.character.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


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


class Shield(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.shield_color

        self.rect = pygame.Rect(0, 0, self.settings.shield_width,
                                self.settings.shield_height)
        self.rect.midtop = ai_game.character.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.shield_speed
        self.rect.y = self.y

    def draw_shield(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
