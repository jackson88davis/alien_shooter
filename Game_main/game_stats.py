class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        self.characters_left = self.settings.character_limit
        self.deads_left = self.settings.character1_limit
        self.score = 0
