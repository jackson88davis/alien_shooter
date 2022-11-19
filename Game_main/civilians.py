import pygame
from pygame.sprite import Sprite


class Civilian_orange(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_orange_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen.get_rect().bottomleft

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.civilian_speed
        self.rect.x = self.x


class Civilian_purple(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_purple_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen.get_rect().bottomleft

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.civilian_speed
        self.rect.x = self.x


class Civilian_turquoise(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_turquoise_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen.get_rect().bottomleft

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.civilian_speed
        self.rect.x = self.x


class Civilian_pink(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_pink_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen.get_rect().bottomright

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.civilian_speed
        self.rect.x = self.x


class Civilian_red(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_red_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen.get_rect().bottomright

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.civilian_speed
        self.rect.x = self.x


class Civilian_yellow(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_yellow_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen.get_rect().bottomright

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.civilian_speed
        self.rect.x = self.x