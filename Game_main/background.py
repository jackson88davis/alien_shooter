import pygame


class Background:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/mars.png')
        self.image = pygame.transform.scale(self.image, (1300, 550))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Background1:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/mars1.png')
        self.image = pygame.transform.scale(self.image, (1300, 550))
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blackhole.png')
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole1:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blackhole.png')
        self.image = pygame.transform.scale(self.image, (1000, 1000))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole2:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blackhole.png')
        self.image = pygame.transform.scale(self.image, (3000, 3000))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole3:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/black.png')
        self.image = pygame.transform.scale(self.image, (1300, 800))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class King:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/king_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-150, -60)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Text:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/text.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-90, -125)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Message:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 20, 20
        self.message_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 18, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-90, -140)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.message_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_message(self):
        self.screen.fill(self.message_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Message1:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 140, 20
        self.message1_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 17, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-90, -140)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.message1_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_message1(self):
        self.screen.fill(self.message1_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Message2:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 140, 20
        self.message2_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 17, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-90, -140)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.message2_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_message2(self):
        self.screen.fill(self.message2_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Press1:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.press1_color = (96, 0, 141)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.move_ip(0, -115)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.press1_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_press1(self):
        self.screen.fill(self.press1_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Press2:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.press2_color = (96, 0, 141)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.move_ip(0, -115)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.press2_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_press2(self):
        self.screen.fill(self.press2_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Press3:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.press3_color = (96, 0, 141)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.move_ip(0, -115)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.press3_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_press3(self):
        self.screen.fill(self.press3_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Press4:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.press4_color = (96, 0, 141)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.move_ip(0, -115)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.press4_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_press4(self):
        self.screen.fill(self.press4_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Vastness:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 480, 50
        self.vastness_color = (96, 0, 141)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.vastness_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_vastness(self):
        self.screen.fill(self.vastness_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)