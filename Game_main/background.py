import pygame


class Background:

    def __init__(self, ai_game):  # Parameters and initializing
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/mars.png')  # Loads Mars background image
        self.image = pygame.transform.scale(self.image, (1300, 550))  # Smooths out the image and changes the size
        self.rect = self.image.get_rect()  # Creates rect from the image

        self.rect.midbottom = self.screen_rect.midbottom  # Sets position midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # Draws the image to the screen


class Background1:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/mars1.png')
        self.image = pygame.transform.scale(self.image, (1300, 550))
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blackhole.png')
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole1:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blackhole.png')
        self.image = pygame.transform.scale(self.image, (1000, 1000))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole2:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/blackhole.png')
        self.image = pygame.transform.scale(self.image, (3000, 3000))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blackhole3:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/black.png')
        self.image = pygame.transform.scale(self.image, (1300, 800))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class King:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/king_alien.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-150, -60)  # Sets 150 left and 60 above center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Text:  # Same as Background

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/text.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-90, -125)  # Sets 90 left and 125 above center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Message:

    def __init__(self, ai_game, msg):  # Parameters and initializing
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 20, 20  # Sets width and height
        self.message_color = (255, 255, 255)  # Sets box color
        self.text_color = (0, 0, 0)  # Sets text color
        self.font = pygame.font.SysFont(None, 18, bold=True)  # Sets font size and bolds

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  # Sets position center
        self.rect.move_ip(-90, -140)  # Sets 90 left and 140 above the center

        self._prep_msg(msg)  # Initializes _prep_msg

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.message_color)  # Makes edges smoother and sets the text
        # and background color
        self.msg_image_rect = self.msg_image.get_rect()  # Creates rect from the image
        self.msg_image_rect.center = self.rect.center  # Puts text in the center of the box

    def draw_message(self):
        self.screen.fill(self.message_color, self.rect)  # Draws rectangular portion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Draws the message image to the screen


class Message1:  # Same as Message

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


class Message2:  # Same as Message

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


class Press1:  # Same as Message

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


class Press2:  # Same as Message

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


class Press3:  # Same as Message

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


class Press4:  # Same as Message

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


class Vastness:  # Same as Message

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
