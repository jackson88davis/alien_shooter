import pygame
from pygame.sprite import Sprite


class Character(Sprite):

    def __init__(self, ai_game):  # Parameters and Initializing
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image_regular = pygame.transform.scale(pygame.image.load('images/character.png'), (75, 75))
        # Set character regular image
        self.image_hurt1 = pygame.transform.scale(pygame.image.load('images/character_hurt1.png'), (75, 75))
        # Set character hurt1 image
        self.image_hurt2 = pygame.transform.scale(pygame.image.load('images/character_hurt2.png'), (75, 75))
        # Set character hurt2 image
        self.image_hurt3 = pygame.transform.scale(pygame.image.load('images/character_hurt3.png'), (75, 75))
        # Set character hurt3 image

        self.image = pygame.image.load('images/character.png')  # Loads Character image
        self.image = pygame.transform.scale(self.image, (75, 75))  # Smooths out the image and changes the size
        self.rect = self.image.get_rect()  # Creates rect from the image

        self.midbottom_character()  # Initializes midbottom_character

        self.rect.midbottom = self.screen_rect.midbottom  # Sets position midbottom

        self.x = float(self.rect.x)  # Store decimal value for x-coordinate

        self.moving_right = False  # Initialize moving_right to False
        self.moving_left = False  # Initialize moving_left to False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:  # Detect if reached right of screen
            self.x += self.settings.character_speed  # Add increasing x-coordinate to character_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:  # Detect if reached left of screen
            self.x -= self.settings.character_speed  # Add decreasing x-coordinate to character_speed

        self.rect.x = self.x  # Use value self.x to set value of self.rect.x

    def midbottom_character(self):
        self.rect.midbottom = self.screen_rect.midbottom  # Sets position midbottom

        self.x = float(self.rect.x)  # Store decimal value for x-coordinate

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # Draws the image to the screen
