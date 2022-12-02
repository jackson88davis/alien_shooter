import pygame.font


class Title:

    def __init__(self, ai_game, msg):  # Parameters and initializing
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 700, 80  # Sets width and height
        self.title_color = (224, 89, 57)  # Sets box color
        self.text_color = (255, 235, 205)  # Sets text color
        self.font = pygame.font.SysFont(None, 96, bold=True)  # Sets font size and bolds

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop  # Sets position midtop
        self.rect.move_ip(0, 80)  # Sets 80 below midtop

        self._prep_msg(msg)  # Initializes _prep_msg

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.title_color)  # Makes edges smoother and sets the text and background
        # color
        self.msg_image_rect = self.msg_image.get_rect()  # Creates rect from the image
        self.msg_image_rect.center = self.rect.center  # Puts text in the center of the box

    def draw_title(self):
        self.screen.fill(self.title_color, self.rect)  # Draws rectangular portion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Draws the text image to the screen


class Quit:  # Same as Title

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.quit_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  # Sets position center
        self.rect.move_ip(0, 120)  # Sets 70 below center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.quit_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_quit(self):
        self.screen.fill(self.quit_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button:  # Same as Title

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-400, -50)  # Sets 400 left and 50 above center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button1:  # Same as Title

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button1_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 48, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(400, -50)  # Sets 400 right and 50 above center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button1_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button1(self):
        self.screen.fill(self.button1_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Creator:  # Same as Title

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 1300, 130
        self.creator_color = (96, 0, 141)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font("edo.ttf", 75, bold=True, italic=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom  # Sets position midbottom

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.creator_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_creator(self):
        self.screen.fill(self.creator_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Hs:  # Same as Title

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 700, 80
        self.hs_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 96, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop
        self.rect.move_ip(0, 80)  # Sets 80 below midtop

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.hs_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_hs(self):
        self.screen.fill(self.hs_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Click:  # Same as Title

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/aliens.png')  # Loads aliens image
        self.image = pygame.transform.smoothscale(self.image, (230, 85))  # Smooths out the image and changes the size
        self.rect = self.image.get_rect()

        self.rect.topleft = self.screen_rect.topleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Logo:  # Same as Title

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ExtinctionGamesLogo.png')  # Loads logo image
        self.image = pygame.transform.smoothscale(self.image, (130, 130))  # Smooths out the image and changes the size
        self.rect = self.image.get_rect()
        self.rect.move_ip(745, 0)  # Sets 730 right of bottom

        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
