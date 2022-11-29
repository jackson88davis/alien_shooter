class GameStats:

    def __init__(self, ai_game):  # Parameters and initializing
        self.settings = ai_game.settings
        self.reset_stats()  # Initializes reset_stats

        self.game_active = False  # Sets game to inactive state

        self.high_score = 0  # Initializes high_score

    def reset_stats(self):
        self.characters_left = self.settings.character_limit  # Resets lives
        self.deads_left = self.settings.character1_limit  # Resets player 2 lives
        self.score = 0  # Resets score to 0
