import pygame.font


class Title:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 700, 80
        self.title_color = (224, 89, 57)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 96, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.title_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_title(self):
        self.screen.fill(self.title_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Quit:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.quit_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midleft = self.screen_rect.midleft

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.quit_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_quit(self):
        self.screen.fill(self.quit_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Creator:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 1300, 80
        self.creator_color = (224, 89, 57)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 108, bold=True, italic=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.creator_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_creator(self):
        self.screen.fill(self.creator_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Hs:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 700, 80
        self.hs_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 96, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.hs_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_hs(self):
        self.screen.fill(self.hs_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Click:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/aliens.png')
        self.image = pygame.transform.smoothscale(self.image, (230, 85))
        self.rect = self.image.get_rect()

        self.rect.topleft = self.screen_rect.topleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)
