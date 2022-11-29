import pygame
from pygame.sprite import Sprite


class Civilian_orange(Sprite):

    def __init__(self, ai_game):  # Parameters and Initializing
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/friend_orange_alien.png')  # Loads orange_alien image
        self.image = pygame.transform.scale(self.image, (75, 75))  # Smooths out the image and changes the size
        self.rect = self.image.get_rect()  # Creates rect from the image

        self.rect.bottomright = self.screen.get_rect().bottomleft  # Moves right to left

        self.x = float(self.rect.x)  # Store decimal value for x-coordinate

    def update(self):
        self.x += self.settings.civilian_speed  # Add increasing x-coordinate to evil_alien_speed
        self.rect.x = self.x  # Use value self.x to set value of self.rect.x


class Civilian_purple(Sprite):  # Same as Civilian_orange

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


class Civilian_turquoise(Sprite):  # Same as Civilian_orange

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


class Civilian_pink(Sprite):  # Same as Civilian_orange

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
        self.x -= self.settings.civilian_speed  # Add decreasing x-coordinate to evil_alien_speed
        self.rect.x = self.x


class Civilian_red(Sprite):  # Same as Civilian_orange

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
        self.x -= self.settings.civilian_speed  # Add decreasing x-coordinate to evil_alien_speed
        self.rect.x = self.x


class Civilian_yellow(Sprite):  # Same as Civilian_orange

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
        self.x -= self.settings.civilian_speed  # Add decreasing x-coordinate to evil_alien_speed
        self.rect.x = self.x
