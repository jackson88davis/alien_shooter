class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600

        self.character_speed = 4
        self.character_limit = 3

        self.character1_speed = 4
        self.character1_limit = 3

        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (194, 23, 232)
        self.bullets_allowed = 2

        self.bullet1_speed = 2
        self.bullet1_width = 15
        self.bullet1_height = 5
        self.bullet1_color = (194, 23, 232)
        self.bullet1s_allowed = 2

        self.shield_speed = 4
        self.shield_width = 95
        self.shield_height = 5
        self.shield_color = (194, 23, 232)
        self.shields_allowed = 1

        self.shield1_speed = 4
        self.shield1_width = 95
        self.shield1_height = 5
        self.shield1_color = (194, 23, 232)
        self.shield1s_allowed = 1

        self.beam_speed = 2
        self.beam_width = 120
        self.beam_height = 200
        self.beam_color = (255, 255, 51)
        self.beams_allowed = 1

        self.civilian_frequency = .0001
        self.civilian_speed = 1

        self.evil_alien_frequency = .0001
        self.evil_alien_speed = .3

        self.alien_frequency = .0015
        self.alien_speed = .5

        self.alien1_frequency = .0015
        self.alien1_speed = .5

        self.meteor_frequency = .0005
        self.meteor_speed = 1

        self.blue_planet_move_left_frequency = .0002
        self.blue_planet_move_left_speed = 3

        self.blue_planet_move_right_frequency = .0002
        self.blue_planet_move_right_speed = 4

        self.bg_color = (254, 179, 114)

        self.speedup_scale = 1.02
        self.score_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed = 2
        self.bullet1_speed = 2
        self.alien_speed = .5
        self.alien1_speed = .5

        self.evil_alien_points = 2000
        self.alien_points = 50
        self.alien1_points = 50
        self.meteor_points = 1000

    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.bullet1_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien1_speed *= self.speedup_scale

        self.evil_alien_points = int(self.evil_alien_points * self.score_scale)
        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien1_points = int(self.alien1_points * self.score_scale)
        self.meteor_points = int(self.meteor_points * self.score_scale)
