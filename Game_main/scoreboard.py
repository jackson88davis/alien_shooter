import pygame.font
from pygame.sprite import Group

from character import Character
from character1 import Dead


class Scoreboard:

    def __init__(self, ai_game):  # Parameters and initializing
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (241, 109, 63)  # Sets the text color
        self.font = pygame.font.SysFont(None, 48, bold=True)  # Sets font size and bolds

        self.prep_score()  # Initializes prep_score
        self.prep_high_score()  # Initializes prep_high_score
        self.prep_characters()  # Initializes prep_characters
        self.prep_character1s()  # Initializes prep_character1s

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)  # Rounds to the nearest 10
        score_str = "{:,}".format(rounded_score)  # Turns into a string and adds commas
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)  # Generates image from score

        self.score_rect = self.score_image.get_rect()  # Creates rect
        self.score_rect.right = self.screen_rect.right - 20  # Sets right edge 20 pixels from right
        self.score_rect.top = 20  # Sets top edge 20 pixels from top

    def prep_high_score(self):  # Same as prep_score
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # Centers the high score horizontally
        self.high_score_rect.top = self.score_rect.top  # Sets top to match top of score image

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)  # Draws the score image to the screen
        self.screen.blit(self.high_score_image, self.high_score_rect)  # Draws the high score image to the screen
        self.characters.draw(self.screen)

    def show_score1(self):  # Same as show_score
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.deads.draw(self.screen)

    def check_high_score(self):  # If score higher than high score replace high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_characters(self):
        self.characters = Group()  # Creates empty group
        for character_number in range(self.stats.characters_left):
            character = Character(self.ai_game)  # Loop runs once for every life the player has left
            character.rect.x = 10 + character_number * character.rect.width  # Creates new lives and makes them
            # appear next to each other with 10 pixels on the left side
            character.rect.y = 10  # Sets 10 pixels from the top
            self.characters.add(character)  # Adds new lives to group

    def prep_character1s(self):  # Same as prep_characters
        self.deads = Group()
        for dead_number in range(self.stats.deads_left):
            dead = Dead(self.ai_game)
            dead.rect.x = 10 + dead_number * dead.rect.width
            dead.rect.y = 10
            self.deads.add(dead)
