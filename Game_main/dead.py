import pygame
from pygame.sprite import Sprite


class Dead(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

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