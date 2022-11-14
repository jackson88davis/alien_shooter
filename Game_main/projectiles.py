import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen.get_rect().bottomright

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.alien_speed
        self.rect.x = self.x


class Alien1(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()

        self.rect.bottomright = self.screen.get_rect().bottomleft

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien1_speed
        self.rect.x = self.x


class Blue_Planet_Move_Left(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blue_planet_left.png')
        self.rect = self.image.get_rect()

        self.rect.topright = self.screen_rect.topleft

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.blue_planet_move_left_speed
        self.rect.x = self.x


class Blue_Planet_Move_Right(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blue_planet_right.png')
        self.rect = self.image.get_rect()

        self.rect.topleft = self.screen.get_rect().topright

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.blue_planet_move_right_speed
        self.rect.x = self.x


class Meteor(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/meteor.png')
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect()

        self.rect.bottom = self.screen.get_rect().top
        meteor_left_max = self.settings.screen_height - self.rect.height
        self.rect.left = randint(0, meteor_left_max)

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.meteor_speed
        self.rect.y = self.y
