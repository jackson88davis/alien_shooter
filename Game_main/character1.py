import pygame
from pygame.sprite import Sprite


class Character1(Sprite):  # Same as Character

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Variables for if statements for player 2 game
        self.number = 0
        self.numbers = 0
        self.numbers1 = 0
        self.numbers2 = 0
        self.numbers3 = 0
        self.numbers4 = 0

        self.image_regular = pygame.transform.scale(pygame.image.load('images/character1.png'), (180, 130))
        self.image_hurt1 = pygame.transform.scale(pygame.image.load('images/character1_hurt1.png'), (180, 130))
        self.image_hurt2 = pygame.transform.scale(pygame.image.load('images/character1_hurt2.png'), (180, 130))
        self.image_hurt3 = pygame.transform.scale(pygame.image.load('images/character1_hurt3.png'), (180, 130))

        self.image = pygame.image.load('images/character1.png')
        self.image = pygame.transform.scale(self.image, (180, 130))
        self.rect = self.image.get_rect()

        self.midbottom_character1()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.character1_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.character1_speed

        self.rect.x = self.x

    def midbottom_character1(self):
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Dead(Sprite):  # Same as Character

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Variable for if statements for player 2 game
        self.number = 0

        self.image_regular = pygame.transform.scale(pygame.image.load('images/dead.png'), (75, 75))

        self.image = pygame.image.load('images/dead.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.midbottom_dead()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def midbottom_dead(self):
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
