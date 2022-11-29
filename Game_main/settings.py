class Settings:

    def __init__(self):
        self.screen_width = 1200  # Sets the screen width
        self.screen_height = 600  # Sets the screen height

        self.character_speed = 4  # Sets the character speed
        self.character_limit = 3  # Sets the character's amount of lives

        self.character1_speed = 4  # Sets the player 2 speed
        self.character1_limit = 3  # Sets the player 2's amount of lives

        self.bullet_speed = 2  # Sets right bullet speed
        self.bullet_width = 15  # Sets right bullet width
        self.bullet_height = 5  # Sets right bullet height
        self.bullet_color = (194, 23, 232)  # Sets right bullet color
        self.bullets_allowed = 1  # Sets right bullet amount

        self.bullet1_speed = 2  # Sets left bullet speed
        self.bullet1_width = 15  # Sets left bullet width
        self.bullet1_height = 5  # Sets left bullet height
        self.bullet1_color = (194, 23, 232)  # Sets left bullet color
        self.bullet1s_allowed = 1  # Sets left bullet amount

        self.shield_speed = 4  # Sets shield speed
        self.shield_width = 95  # Sets shield width
        self.shield_height = 5  # Sets shield height
        self.shield_color = (194, 23, 232)  # Sets shield color
        self.shields_allowed = 1  # Sets shield amount

        self.shield1_speed = 4  # Sets player 2 shield speed
        self.shield1_width = 95  # Sets player 2 shield width
        self.shield1_height = 5  # Sets player 2 shield height
        self.shield1_color = (194, 23, 232)  # Sets player 2 shield color
        self.shield1s_allowed = 1  # Sets player 2 shield amount

        self.beam_speed = 2  # Sets player 2 beam speed
        self.beam_width = 120  # Sets player 2 beam width
        self.beam_height = 200  # Sets player 2 beam height
        self.beam_color = (255, 255, 51)  # Sets player 2 beam color
        self.beams_allowed = 1  # Sets player 2 beam amount

        self.civilian_frequency = .0001  # Sets civilian frequency
        self.civilian_speed = 1  # Sets civilian speed

        self.evil_alien_frequency = .0001    # Sets evil alien frequency
        self.evil_alien_speed = .3    # Sets evil alien speed

        self.alien_frequency = .0015    # Sets left alien frequency
        self.alien_speed = 1      # Sets left alien speed

        self.alien1_frequency = .0015    # Sets right alien frequency
        self.alien1_speed = 1      # Sets right alien speed

        self.meteor_frequency = .0005    # Sets meteor frequency
        self.meteor_speed = 1      # Sets meteor speed

        self.blue_planet_move_left_frequency = .0002    # Sets left planet frequency
        self.blue_planet_move_left_speed = 3      # Sets left planet speed

        self.blue_planet_move_right_frequency = .0002    # Sets right planet frequency
        self.blue_planet_move_right_speed = 4      # Sets right planet speed

        self.bg_color = (254, 179, 114)  # Sets background color

        self.speedup_scale = 1.02  # Sets increasing speed scale
        self.score_scale = 1.1  # Sets increasing score scale

        self.initialize_dynamic_settings()  # Initializes increasing difficulty

    def initialize_dynamic_settings(self):
        self.bullet_speed = 2  # Sets right bullet speed
        self.bullet1_speed = 2  # Sets left bullet speed
        self.alien_speed = 1.5  # Sets left alien speed
        self.alien1_speed = 1.5  # Sets right alien speed

        self.evil_alien_points = 2000  # Sets evil alien points
        self.alien_points = 50  # Sets left alien points
        self.alien1_points = 50  # Sets right alien points
        self.meteor_points = 1000  # Sets meteor points

    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale  # Multiplies right bullet speed by speed scale
        self.bullet1_speed *= self.speedup_scale  # Multiplies left bullet speed by speed scale
        self.alien_speed *= self.speedup_scale  # Multiplies left alien speed by speed scale
        self.alien1_speed *= self.speedup_scale  # Multiplies right alien speed by speed scale

        self.evil_alien_points = int(self.evil_alien_points * self.score_scale)    # Multiplies evil alien points by
        # score scale
        self.alien_points = int(self.alien_points * self.score_scale)    # Multiplies left alien points by score scale
        self.alien1_points = int(self.alien1_points * self.score_scale)    # Multiplies right alien points by score
        # scale
        self.meteor_points = int(self.meteor_points * self.score_scale)    # Multiplies meteor points by score scale
