import pygame.font


class Instructions_alien:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_alien_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(0, -100)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_alien_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_alien(self):
        self.screen.fill(self.instructions_alien_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_meteor:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_meteor_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(0, -50)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_meteor_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_meteor(self):
        self.screen.fill(self.instructions_meteor_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_lives:

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


class Instructions_move:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_move_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(0, 50)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_move_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_move(self):
        self.screen.fill(self.instructions_move_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Instructions_shoot:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 350, 50
        self.instructions_shoot_color = (241, 109, 63)
        self.text_color = (255, 235, 205)
        self.font = pygame.font.SysFont(None, 24, bold=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.move_ip(0, 100)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.instructions_shoot_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_instructions_shoot(self):
        self.screen.fill(self.instructions_shoot_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)