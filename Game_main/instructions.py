import pygame.font


class Instructions_alien:

    def __init__(self, ai_game, msg):  # Parameters and initializing
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50  # Sets width and height
        self.instructions_alien_color = (241, 109, 63)  # Sets box color
        self.text_color = (255, 235, 205)  # Sets text color
        self.font = pygame.font.SysFont(None, 24, bold=True)  # Sets font size and bolds

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  # Sets position midtop
        self.rect.move_ip(0, -100)  # Sets 100 above center

        self._prep_msg(msg)  # Initializes _prep_msg

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_alien_color)  # Makes edges smoother and sets the text
        # and background color
        self.msg_image_rect = self.msg_image.get_rect()  # Creates rect from the image
        self.msg_image_rect.center = self.rect.center  # Puts text in the center of the box

    def draw_instructions_alien(self):
        self.screen.fill(self.instructions_alien_color, self.rect)  # Draws rectangular portion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Draws the text image to the screen


class Instructions_meteor:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_meteor_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(0, -50)  # Sets 50 above center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_meteor_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_meteor(self):
        self.screen.fill(self.instructions_meteor_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_lives:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_lives_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_lives_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_lives(self):
        self.screen.fill(self.instructions_lives_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_friend:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_friend_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(0, 50)  # Sets 50 below center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_friend_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_friend(self):
        self.screen.fill(self.instructions_friend_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_move:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_move_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-400, 20)  # Sets 400 left and 20 below center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_move_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_move(self):
        self.screen.fill(self.instructions_move_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_move1:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_move1_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(400, 20)  # Sets 400 right and 20 below center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_move1_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_move1(self):
        self.screen.fill(self.instructions_move1_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_shoot:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_shoot_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(-400, 70)  # Sets 400 left and 70 below center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_shoot_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_shoot(self):
        self.screen.fill(self.instructions_shoot_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_shoot1:  # Same as Instructions_alien

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_shoot1_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(400, 70)  # Sets 400 right and 70 below center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_shoot1_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_shoot1(self):
        self.screen.fill(self.instructions_shoot1_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
