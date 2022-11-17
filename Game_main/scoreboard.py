import pygame.font
from pygame.sprite import Group

from character import Character
from character1 import Character1


class Scoreboard:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (241, 109, 63)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self.prep_score()
        self.prep_high_score()
        self.prep_characters()
        self.prep_character1s()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.characters.draw(self.screen)
        self.character1s.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_characters(self):
        self.characters = Group()
        for character_number in range(self.stats.characters_left):
            character = Character(self.ai_game)
            character.rect.x = 10 + character_number * character.rect.width
            character.rect.y = 10
            self.characters.add(character)

    def prep_character1s(self):
        self.character1s = Group()
        for character1_number in range(self.stats.character1s_left):
            character1 = Character1(self.ai_game)
            character1.rect.x = 10 + character1_number * character1.rect.width
            character1.rect.y = 10
            self.character1s.add(character1)