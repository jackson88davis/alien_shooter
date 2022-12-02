import sys
from time import sleep
from random import random
import pygame
from pygame import mixer

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from text import Title
from text import Quit
from text import Button
from text import Button1
from text import Creator
from text import Name
from text import Hs
from text import Click
from text import Logo
from instructions import Instructions_alien
from instructions import Instructions_meteor
from instructions import Instructions_lives
from instructions import Instructions_friend
from instructions import Instructions_move
from instructions import Instructions_move1
from instructions import Instructions_shoot
from instructions import Instructions_shoot1
from background import Background
from background import Background1
from background import Blackhole
from background import Blackhole1
from background import Blackhole2
from background import Blackhole3
from background import King
from background import Text
from background import Message
from background import Message1
from background import Message2
from background import Press1
from background import Press2
from background import Press3
from background import Press4
from background import Vastness
from character import Character
from character1 import Character1
from bullet import Bullet
from bullet import Bullet1
from bullet import Shield
from bullet import Shield1
from bullet import Beam
from civilians import Civilian_orange
from civilians import Civilian_purple
from civilians import Civilian_turquoise
from civilians import Civilian_pink
from civilians import Civilian_red
from civilians import Civilian_yellow
from projectiles import Evil_alien
from projectiles import Alien
from projectiles import Alien1
from projectiles import Blue_Planet_Move_Left
from projectiles import Blue_Planet_Move_Right
from projectiles import Meteor


class Game:

    def __init__(self):  # Parameters and initializing
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Creates window size that will fit the screen
        self.settings.screen_width = self.screen.get_rect().width  # Uses the width screen's rect to update settings
        # object
        self.settings.screen_height = self.screen.get_rect().height  # Uses the width screen's rect to update settings
        # object
        pygame.display.set_caption("Planetary Panic")  # Sets the display caption

        # Assigns game instances to attributes
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.background = Background(self)
        self.background1 = Background1(self)
        self.blackhole = Blackhole(self)
        self.blackhole1 = Blackhole1(self)
        self.blackhole2 = Blackhole2(self)
        self.blackhole3 = Blackhole3(self)
        self.king = King(self)
        self.text = Text(self)
        self.click = Click(self)
        self.logo = Logo(self)
        self.character = Character(self)
        self.character1 = Character1(self)
        self.bullets = pygame.sprite.Group()
        self.bullet1s = pygame.sprite.Group()
        self.shields = pygame.sprite.Group()
        self.shield1s = pygame.sprite.Group()
        self.beams = pygame.sprite.Group()
        self.civilian_oranges = pygame.sprite.Group()
        self.civilian_purples = pygame.sprite.Group()
        self.civilian_turquoises = pygame.sprite.Group()
        self.civilian_pinks = pygame.sprite.Group()
        self.civilian_reds = pygame.sprite.Group()
        self.civilian_yellows = pygame.sprite.Group()
        self.evil_aliens = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien1s = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.blue_planet_move_lefts = pygame.sprite.Group()
        self.blue_planet_move_rights = pygame.sprite.Group()

        # Assigns sound files to sound attributes
        self.mixer = mixer
        self.alien_sound = pygame.mixer.Sound('sounds/alien_sound.wav')
        self.blackhole_sound = pygame.mixer.Sound('sounds/blackhole_sound.mp3')
        self.click_sound = pygame.mixer.Sound('sounds/click_sound.ogg')
        self.confirmation_sound = pygame.mixer.Sound('sounds/confirmation_sound.ogg')
        self.crash_sound = pygame.mixer.Sound('sounds/crash_sound.wav')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion_sound.mp3')
        self.giant_sound = pygame.mixer.Sound('sounds/giant_sound.wav')
        self.giant_hurt_sound = pygame.mixer.Sound('sounds/giant_hurt_sound.wav')
        self.hey_sound = pygame.mixer.Sound('sounds/hey_sound.mp3')
        self.hi_sound = pygame.mixer.Sound('sounds/hi_sound.mp3')
        self.hurt_sound = pygame.mixer.Sound('sounds/hurt_sound.wav')
        self.instructions_sound = pygame.mixer.Sound('sounds/instructions_sound.wav')
        self.lalala_sound = pygame.mixer.Sound('sounds/lalala_sound.wav')
        self.laser_sound = pygame.mixer.Sound('sounds/laser_sound.ogg')
        self.loss_sound = pygame.mixer.Sound('sounds/loss_sound.wav')
        self.meteor_explosion_sound = pygame.mixer.Sound('sounds/meteor_explosion_sound.ogg')
        self.meteor_strike_sound = pygame.mixer.Sound('sounds/meteor_strike_sound.wav')
        self.ouch_sound = pygame.mixer.Sound('sounds/ouch_sound.mp3')
        self.quit_sound = pygame.mixer.Sound('sounds/quit_sound.mp3')
        self.shield_sound = pygame.mixer.Sound('sounds/shield_sound.mp3')
        self.space_sound = pygame.mixer.Sound('sounds/space_sound.aiff')
        self.stop_sound = pygame.mixer.Sound('sounds/stop_sound.mp3')
        self.what_sound = pygame.mixer.Sound('sounds/what_sound.mp3')

        # Assigns music file to music attribute
        pygame.mixer.music.load('sounds/music.mp3')
        pygame.mixer.music.set_volume(0.2)

        # Assigns text instances to text attributes
        self.play_button = Button(self, "1 Player")
        self.play_button1 = Button1(self, "2 Player")
        self.play_quit = Quit(self, "Quit")
        self.play_title = Title(self, "Planetary Panic")
        self.play_instructions_alien = Instructions_alien(self, "-Aliens attack from the left and right-")
        self.play_instructions_meteor = Instructions_meteor(self, "-Meteors fall from the sky-")
        self.play_instructions_lives = Instructions_lives(self, "-You only have three lives-")
        self.play_instructions_friend = Instructions_friend(self, "-Watch out for your alien friends-")
        self.play_instructions_move = Instructions_move(self, "-Use the arrow keys to move-")
        self.play_instructions_move1 = Instructions_move1(self, "-Player 1 use arrow keys-")
        self.play_instructions_shoot = Instructions_shoot(self, "-Use the 'a', 'w', and 'd' keys to shoot-")
        self.play_instructions_shoot1 = Instructions_shoot1(self, "-Player 2 use 'a', 'w', 's', and 'd'-")
        self.play_creator = Creator(self, "E-X-T-I-N-C-T-I-O-N       G-A-M-E-S")
        self.play_name = Name(self, "Jackson Davis")
        self.play_hs = Hs(self, "HIGH SCORE!")
        self.play_message = Message(self, "HOW DARE YOU!")
        self.play_message1 = Message1(self, "YOU ARE A TRAITOR!")
        self.play_message2 = Message2(self, "DIE!")
        self.play_press1 = Press1(self, "PRESS 1")
        self.play_press2 = Press2(self, "PRESS 2")
        self.play_press3 = Press3(self, "PRESS 3")
        self.play_press4 = Press4(self, "PRESS 4")
        self.play_vastness = Vastness(self, "You are floating through the empty vastness of space")
        self.play_click = Click(self)
        self.play_logo = Logo(self)

    def run_game(self):
        while True:  # runs continually
            self._check_events()  # calls _check_events method

            if self.stats.game_active:  # if game is in an active state run these methods
                self.character.update()
                self.character1.update()
                self._update_bullets()
                self._update_bullet1s()
                self._update_shields()
                self._update_shield1s()
                self._update_beams()
                self._create_civilian_orange()
                self._update_civilian_oranges()
                self._create_civilian_purple()
                self._update_civilian_purples()
                self._create_civilian_turquoise()
                self._update_civilian_turquoises()
                self._create_civilian_pink()
                self._update_civilian_pinks()
                self._create_civilian_red()
                self._update_civilian_reds()
                self._create_civilian_yellow()
                self._update_civilian_yellows()
                self._create_evil_alien()
                self._update_evil_aliens()
                self._create_alien()
                self._update_aliens()
                self._create_alien1()
                self._update_alien1s()
                self._create_meteor()
                self._update_meteors()
                self._create_blue_planet_move_left()
                self._update_blue_planet_move_lefts()
                self._create_blue_planet_move_right()
                self._update_blue_planet_move_rights()

            self._update_screen()  # Calls _update_screen method

    def _check_events(self):
        for event in pygame.event.get():  # For loop
            if event.type == pygame.KEYDOWN:  # If key pressed down run _check_keydown_events method
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:  # If key pressed up run _check_keyup_events method
                self._check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:  # If mouse pressed down run these methods
                mouse_pos = pygame.mouse.get_pos()  # Returns mouses x and y coordinates
                self._check_play_button(mouse_pos)
                self._check_play_button1(mouse_pos)
                self._check_quit(mouse_pos)
                self._check_click(mouse_pos)
                self._check_logo(mouse_pos)
                self._check_instructions_alien(mouse_pos)
                self._check_instructions_meteor(mouse_pos)
                self._check_instructions_lives(mouse_pos)
                self._check_instructions_friend(mouse_pos)
                self._check_instructions_move(mouse_pos)
                self._check_instructions_move1(mouse_pos)
                self._check_instructions_shoot(mouse_pos)
                self._check_instructions_shoot1(mouse_pos)

    def _check_play_button(self, mouse_pos):
        pygame.mixer.Sound.play(self.click_sound)  # Plays sound if mouse clicked
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)  # Check if mouse click overlaps with button
        if button_clicked and not self.stats.game_active:  # If button clicked and game not active
            pygame.mixer.Sound.play(self.confirmation_sound)  # Plays sound if button clicked
            pygame.mixer.music.play(-1)  # Plays continuous music if button clicked
            # Runs the methods
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True  # Sets game to an active state
            self.sb.prep_score()
            self.sb.prep_characters()

            self.civilian_oranges.empty()
            self.civilian_purples.empty()
            self.civilian_turquoises.empty()
            self.civilian_pinks.empty()
            self.civilian_reds.empty()
            self.civilian_yellows.empty()
            self.evil_aliens.empty()
            self.aliens.empty()
            self.alien1s.empty()
            self.meteors.empty()
            self.blue_planet_move_lefts.empty()
            self.blue_planet_move_rights.empty()

            self._create_civilian_orange()
            self._create_civilian_purple()
            self._create_civilian_turquoise()
            self._create_civilian_pink()
            self._create_civilian_red()
            self._create_civilian_yellow()
            self._create_evil_alien()
            self._create_alien()
            self._create_alien1()
            self._create_meteor()
            self._create_blue_planet_move_left()
            self._create_blue_planet_move_right()
            self.character.midbottom_character()
            self.character1.number = 0  # Sets variable to 0 for player 2 game

            pygame.mouse.set_visible(False)  # Sets mouse invisible

    def _check_play_button1(self, mouse_pos):  # Same as _check_play_button
        pygame.mixer.Sound.play(self.click_sound)
        button1_clicked = self.play_button1.rect.collidepoint(mouse_pos)
        if button1_clicked and not self.stats.game_active:
            pygame.mixer.Sound.play(self.confirmation_sound)
            pygame.mixer.music.play(-1)
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_characters()
            self.sb.prep_character1s()

            self.civilian_oranges.empty()
            self.civilian_purples.empty()
            self.civilian_turquoises.empty()
            self.civilian_pinks.empty()
            self.civilian_reds.empty()
            self.civilian_yellows.empty()
            self.evil_aliens.empty()
            self.aliens.empty()
            self.alien1s.empty()
            self.meteors.empty()
            self.blue_planet_move_lefts.empty()
            self.blue_planet_move_rights.empty()

            self._create_civilian_orange()
            self._create_civilian_purple()
            self._create_civilian_turquoise()
            self._create_civilian_pink()
            self._create_civilian_red()
            self._create_civilian_yellow()
            self._create_evil_alien()
            self._create_alien()
            self._create_alien1()
            self._create_meteor()
            self._create_blue_planet_move_left()
            self._create_blue_planet_move_right()
            self.character.midbottom_character()
            self.character1.midbottom_character1()
            self.character1.number = 1  # Sets variable to 1 for player 2 game

            pygame.mouse.set_visible(False)

    def _check_quit(self, mouse_pos):
        quit_clicked = self.play_quit.rect.collidepoint(mouse_pos)  # Check if mouse click overlaps with button
        if quit_clicked:  # If button clicked
            pygame.mixer.Sound.play(self.quit_sound)  # Stops continuous music if button clicked
            sleep(1)  # Pauses the game for a second
            sys.exit()  # Exits the game

    def _check_click(self, mouse_pos):
        click_clicked = self.play_click.rect.collidepoint(mouse_pos)  # Check if mouse click overlaps with button
        if click_clicked:  # If button clicked
            pygame.mixer.Sound.play(self.stop_sound)  # Plays sound if button clicked

    def _check_logo(self, mouse_pos):
        logo_clicked = self.play_logo.rect.collidepoint(mouse_pos)  # Check if mouse click overlaps with button
        if logo_clicked:  # If button clicked
            pygame.mixer.Sound.play(self.space_sound)  # Plays sound if button clicked

    def _check_instructions_alien(self, mouse_pos):
        instructions_alien_clicked = self.play_instructions_alien.rect.collidepoint(mouse_pos)  # Check if mouse
        # click overlaps with button
        if instructions_alien_clicked:  # If button clicked
            pygame.mixer.Sound.play(self.instructions_sound)  # Plays sound if button clicked

    def _check_instructions_meteor(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_meteor_clicked = self.play_instructions_meteor.rect.collidepoint(mouse_pos)
        if instructions_meteor_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_instructions_lives(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_lives_clicked = self.play_instructions_lives.rect.collidepoint(mouse_pos)
        if instructions_lives_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_instructions_friend(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_friend_clicked = self.play_instructions_friend.rect.collidepoint(mouse_pos)
        if instructions_friend_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_instructions_move(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_move_clicked = self.play_instructions_move.rect.collidepoint(mouse_pos)
        if instructions_move_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_instructions_move1(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_move1_clicked = self.play_instructions_move1.rect.collidepoint(mouse_pos)
        if instructions_move1_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_instructions_shoot(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_shoot_clicked = self.play_instructions_shoot.rect.collidepoint(mouse_pos)
        if instructions_shoot_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_instructions_shoot1(self, mouse_pos):  # Same as _check_instructions_alien
        instructions_shoot1_clicked = self.play_instructions_shoot1.rect.collidepoint(mouse_pos)
        if instructions_shoot1_clicked:
            pygame.mixer.Sound.play(self.instructions_sound)

    def _check_keydown_events(self, event):
        if self.character1.number == 0:  # Sets variable to 0 for player 2 game
            if event.key == pygame.K_RIGHT:  # If right arrow clicked
                self.character.moving_right = True  # Sets method True
            if event.key == pygame.K_LEFT:  # If left arrow clicked
                self.character.moving_left = True  # Sets method True
            if event.key == pygame.K_d:  # If d clicked
                self._fire_bullet()  # Runs method
            if event.key == pygame.K_a:  # If a clicked
                self._fire_bullet1()  # Runs method
            if event.key == pygame.K_w:  # If w clicked
                self._fire_shield()  # Runs method
        if self.character1.number == 1:  # Sets variable to 1 for player 2 game
            if event.key == pygame.K_RIGHT:  # If right arrow clicked
                self.character.moving_right = True  # Sets method True
            if event.key == pygame.K_LEFT:  # If left arrow clicked
                self.character.moving_left = True  # Sets method True
            if event.key == pygame.K_UP:  # If up arrow clicked
                self._fire_bullet()  # Runs method
                self._fire_bullet1()  # Runs method
            if event.key == pygame.K_d:  # If d clicked
                self.character1.moving_right = True  # Sets method True
            if event.key == pygame.K_a:  # If a clicked
                self.character1.moving_left = True  # Sets method True
            if event.key == pygame.K_w:  # If w clicked
                self._fire_shield1()  # Runs method
            if event.key == pygame.K_s:  # If s clicked
                self._fire_beam()  # Runs method
        if self.character1.numbers == 1:  # Sets variable to 1 for player 2 game
            if event.key == pygame.K_1:  # If 1 clicked
                self.character1.numbers1 = 1  # Sets variable to 1 for player 2 game
        if self.character1.numbers1 == 1:  # Sets variable to 1 for player 2 game
            if event.key == pygame.K_2:  # If 2 clicked
                self.character1.numbers2 = 1  # Sets variable to 1 for player 2 game
        if self.character1.numbers2 == 1:  # Sets variable to 1 for player 2 game
            if event.key == pygame.K_3:  # If 3 clicked
                self.character1.numbers3 = 1  # Sets variable to 1 for player 2 game
        if self.character1.numbers3 == 1:  # Sets variable to 1 for player 2 game
            if event.key == pygame.K_4:  # If 4 clicked
                self.character1.numbers4 = 1  # Sets variable to 1 for player 2 game
        if self.stats.game_active == True and event.key == pygame.K_TAB:  # If game is in an active state and tab
            # clicked
            pygame.mixer.music.stop()  # Stops continuous music if button clicked
            self.stats.game_active = False  # Sets game to an inactive state
            pygame.mouse.set_visible(True)  # Sets mouse visible
        if event.key == pygame.K_ESCAPE:  # If escape clicked
            pygame.mixer.Sound.play(self.quit_sound)  # Stops continuous music if button clicked
            sleep(1)  # Pauses the game for a second
            sys.exit()  # Exits the game

    def _check_keyup_events(self, event):  # Same as _check_keydown_events
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False  # Sets method False
        if event.key == pygame.K_LEFT:
            self.character.moving_left = False  # Sets method False
        if event.key == pygame.K_d:
            self.character1.moving_right = False  # Sets method False
        if event.key == pygame.K_a:
            self.character1.moving_left = False  # Sets method False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:  # If less than 1 create new bullet
            new_bullet = Bullet(self)  # Instance of bullet
            self.bullets.add(new_bullet)  # Adds new_bullet to group of bullets
            pygame.mixer.Sound.play(self.laser_sound)  # Plays sound

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():  # For loop with copy of bullets
            if bullet.rect.left >= self.screen.get_rect().right:  # Checks if disappeared off the screen
                self.bullets.remove(bullet)  # Remove from bullets

        # Runs methods checking for collisions
        self._check_bullet_civilian_orange_collisions()
        self._check_bullet_civilian_purple_collisions()
        self._check_bullet_civilian_turquoise_collisions()
        self._check_bullet_civilian_pink_collisions()
        self._check_bullet_civilian_red_collisions()
        self._check_bullet_civilian_yellow_collisions()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)  # Checks for collisions by checking bullets and aliens positions
        if collisions:  # If there is a collision
            self.bullets.empty()  # Removes bullets
            self._create_alien()  # Creates new aliens
            self.settings.increase_speed()  # Increases the speed
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)  # Increases the score
            self.sb.prep_score()  # Sets score to 0
            self.sb.check_high_score()  # Checks if high score has been beaten

    def _check_bullet_civilian_orange_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.civilian_oranges, True, True)
        if collisions:
            self.bullets.empty()
            self._create_civilian_orange()
            self.character1.numbers = 1  # Sets variable to 1 for player 2 game

    def _check_bullet_civilian_purple_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.civilian_purples, True, True)
        if collisions:
            self.bullets.empty()
            self._create_civilian_purple()
            self.character1.numbers = 1

    def _check_bullet_civilian_turquoise_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.civilian_turquoises, True, True)
        if collisions:
            self.bullets.empty()
            self._create_civilian_turquoise()
            self.character1.numbers = 1

    def _check_bullet_civilian_pink_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.civilian_pinks, True, True)
        if collisions:
            self.bullets.empty()
            self._create_civilian_pink()
            self.character1.numbers = 1

    def _check_bullet_civilian_red_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.civilian_reds, True, True)
        if collisions:
            self.bullets.empty()
            self._create_civilian_red()
            self.character1.numbers = 1

    def _check_bullet_civilian_yellow_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.civilian_yellows, True, True)
        if collisions:
            self.bullets.empty()
            self._create_civilian_yellow()
            self.character1.numbers = 1

    def _fire_bullet1(self):  # Same as _fire_bullet
        if len(self.bullet1s) < self.settings.bullet1s_allowed:
            new_bullet1 = Bullet1(self)
            self.bullet1s.add(new_bullet1)
            pygame.mixer.Sound.play(self.laser_sound)

    def _update_bullet1s(self):  # Same as _update_bullets
        self.bullet1s.update()

        for bullet1 in self.bullet1s.copy():
            if bullet1.rect.left <= 0:
                self.bullet1s.remove(bullet1)

        self._check_bullet1_civilian_orange_collisions()
        self._check_bullet1_civilian_purple_collisions()
        self._check_bullet1_civilian_turquoise_collisions()
        self._check_bullet1_civilian_pink_collisions()
        self._check_bullet1_civilian_red_collisions()
        self._check_bullet1_civilian_yellow_collisions()
        self._check_bullet1_evil_alien_collisions()
        self._check_bullet1_alien1_collisions()

    def _check_bullet1_civilian_orange_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.civilian_oranges, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_civilian_orange()
            self.character1.numbers = 1

    def _check_bullet1_civilian_purple_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.civilian_purples, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_civilian_purple()
            self.character1.numbers = 1

    def _check_bullet1_civilian_turquoise_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.civilian_turquoises, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_civilian_turquoise()
            self.character1.numbers = 1

    def _check_bullet1_civilian_pink_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.civilian_pinks, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_civilian_pink()
            self.character1.numbers = 1

    def _check_bullet1_civilian_red_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.civilian_reds, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_civilian_red()
            self.character1.numbers = 1

    def _check_bullet1_civilian_yellow_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.civilian_yellows, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_civilian_yellow()
            self.character1.numbers = 1

    def _check_bullet1_evil_alien_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.evil_aliens, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_evil_alien()
            self.settings.increase_speed()
            for evil_aliens in collisions.values():
                self.stats.score += self.settings.evil_alien_points * len(evil_aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _check_bullet1_alien1_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.bullet1s, self.alien1s, True, True)
        if collisions:
            self.bullet1s.empty()
            self._create_alien1()
            self.settings.increase_speed()
            for alien1s in collisions.values():
                self.stats.score += self.settings.alien1_points * len(alien1s)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _fire_shield(self):  # Same as _fire_bullet
        if len(self.shields) < self.settings.shields_allowed:
            new_shield = Shield(self)
            self.shields.add(new_shield)
            pygame.mixer.Sound.play(self.shield_sound)

    def _update_shields(self):  # Same as _update_bullets
        self.shields.update()

        for shield in self.shields.copy():
            if shield.rect.left <= 0:
                self.shields.remove(shield)

        self._check_shields_top()
        self._check_shield_meteor_collisions()
        self._check_beam_civilian_orange_collisions()
        self._check_beam_civilian_purple_collisions()
        self._check_beam_civilian_turquoise_collisions()
        self._check_beam_civilian_pink_collisions()
        self._check_beam_civilian_red_collisions()
        self._check_beam_civilian_yellow_collisions()

    def _check_shields_top(self):
        for shield in self.shields.sprites():  # For loop
            if shield.rect.top < 0:  # If shield
                self.shields.empty()  # Removes bullets

    def _check_beam_civilian_orange_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.civilian_oranges, True, True)
        if collisions:
            self.beams.empty()
            self._create_civilian_orange()
            self.character1.numbers = 1

    def _check_beam_civilian_purple_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.civilian_purples, True, True)
        if collisions:
            self.beams.empty()
            self._create_civilian_purple()
            self.character1.numbers = 1

    def _check_beam_civilian_turquoise_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.civilian_turquoises, True, True)
        if collisions:
            self.beams.empty()
            self._create_civilian_turquoise()
            self.character1.numbers = 1

    def _check_beam_civilian_pink_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.civilian_pinks, True, True)
        if collisions:
            self.beams.empty()
            self._create_civilian_pink()
            self.character1.numbers = 1

    def _check_beam_civilian_red_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.civilian_reds, True, True)
        if collisions:
            self.beams.empty()
            self._create_civilian_red()
            self.character1.numbers = 1

    def _check_beam_civilian_yellow_collisions(self):  # Same as _check_bullet_civilian_orange_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.civilian_yellows, True, True)
        if collisions:
            self.beams.empty()
            self._create_civilian_yellow()
            self.character1.numbers = 1

    def _check_shield_meteor_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.shields, self.meteors, True, True)
        if collisions:
            self.shields.empty()
            self._create_meteor()
            for meteors in collisions.values():
                self.stats.score += self.settings.meteor_points * len(meteors)
            self.sb.prep_score()
            self.sb.check_high_score()
            pygame.mixer.Sound.play(self.meteor_explosion_sound)

    def _fire_shield1(self):  # Same as _fire_shield
        if len(self.shield1s) < self.settings.shield1s_allowed:
            new_shield1 = Shield1(self)
            self.shield1s.add(new_shield1)
            pygame.mixer.Sound.play(self.shield_sound)

    def _update_shield1s(self):  # Same as _update_shields
        self.shield1s.update()

        for shield1 in self.shield1s.copy():
            if shield1.rect.left <= 0:
                self.shield1s.remove(shield1)

        self._check_shield1s_top()
        self._check_shield1_meteor_collisions()

    def _check_shield1s_top(self):  # Same as _check_shields_top
        for shield1 in self.shield1s.sprites():
            if shield1.rect.top < 0:
                self.shield1s.empty()

    def _check_shield1_meteor_collisions(self):  # Same as _check_shield_meteor_collisions
        collisions = pygame.sprite.groupcollide(
            self.shield1s, self.meteors, True, True)
        if collisions:
            self.shield1s.empty()
            self._create_meteor()
            for meteors in collisions.values():
                self.stats.score += self.settings.meteor_points * len(meteors)
            self.sb.prep_score()
            self.sb.check_high_score()
            pygame.mixer.Sound.play(self.meteor_explosion_sound)

    def _fire_beam(self):  # Same as _fire_shield
        if len(self.beams) < self.settings.beams_allowed:
            new_beam = Beam(self)
            self.beams.add(new_beam)
            pygame.mixer.Sound.play(self.shield_sound)

    def _update_beams(self):  # Same as _update_shields
        self.beams.update()

        for beam in self.beams.copy():
            if beam.rect.top >= self.screen.get_rect().bottom:
                self.beams.remove(beam)

        self._check_beams_bottom()
        self._check_beam_evil_alien_collisions()
        self._check_beam_alien_collisions()
        self._check_beam_alien1_collisions()

    def _check_beams_bottom(self):  # Same as _check_shields_top
        for beam in self.beams.sprites():
            if beam.rect.bottom < 0:
                self.beams.empty()

    def _check_beam_alien_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.aliens, True, True)
        if collisions:
            self.beams.empty()
            self._create_alien()
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _check_beam_alien1_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.alien1s, True, True)
        if collisions:
            self.beams.empty()
            self._create_alien1()
            for alien1s in collisions.values():
                self.stats.score += self.settings.alien1_points * len(alien1s)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _check_beam_evil_alien_collisions(self):  # Same as _check_bullet_alien_collisions
        collisions = pygame.sprite.groupcollide(
            self.beams, self.evil_aliens, True, True)
        if collisions:
            self.beams.empty()
            self._create_evil_alien()
            for evil_aliens in collisions.values():
                self.stats.score += self.settings.evil_alien_points * len(evil_aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _create_civilian_orange(self):
        if random() < self.settings.civilian_frequency:  # Sets random frequency
            civilian_orange = Civilian_orange(self)  # Instance of civilian
            self.civilian_oranges.add(civilian_orange)  # Adds civilian to group
            pygame.mixer.Sound.play(self.lalala_sound)  # Plays sound

    def _update_civilian_oranges(self):  # Updates civilians
        self.civilian_oranges.update()

    def _create_civilian_purple(self):  # Same as _create_civilian_orange
        if random() < self.settings.civilian_frequency:
            civilian_purple = Civilian_purple(self)
            self.civilian_purples.add(civilian_purple)
            pygame.mixer.Sound.play(self.lalala_sound)

    def _update_civilian_purples(self):  # Same as _update_civilian_oranges
        self.civilian_purples.update()

    def _create_civilian_turquoise(self):  # Same as _create_civilian_orange
        if random() < self.settings.civilian_frequency:
            civilian_turquoise = Civilian_turquoise(self)
            self.civilian_turquoises.add(civilian_turquoise)
            pygame.mixer.Sound.play(self.lalala_sound)

    def _update_civilian_turquoises(self):  # Same as _update_civilian_oranges
        self.civilian_turquoises.update()

    def _create_civilian_pink(self):  # Same as _create_civilian_orange
        if random() < self.settings.civilian_frequency:
            civilian_pink = Civilian_pink(self)
            self.civilian_pinks.add(civilian_pink)
            pygame.mixer.Sound.play(self.lalala_sound)

    def _update_civilian_pinks(self):  # Same as _update_civilian_oranges
        self.civilian_pinks.update()

    def _create_civilian_red(self):  # Same as _create_civilian_orange
        if random() < self.settings.civilian_frequency:
            civilian_red = Civilian_red(self)
            self.civilian_reds.add(civilian_red)
            pygame.mixer.Sound.play(self.lalala_sound)

    def _update_civilian_reds(self):  # Same as _update_civilian_oranges
        self.civilian_reds.update()

    def _create_civilian_yellow(self):  # Same as _create_civilian_orange
        if random() < self.settings.civilian_frequency:
            civilian_yellow = Civilian_yellow(self)
            self.civilian_yellows.add(civilian_yellow)
            pygame.mixer.Sound.play(self.lalala_sound)

    def _update_civilian_yellows(self):  # Same as _update_civilian_oranges
        self.civilian_yellows.update()

    def _create_evil_alien(self):  # Same as _create_civilian_orange
        if random() < self.settings.evil_alien_frequency:
            evil_alien = Evil_alien(self)
            self.evil_aliens.add(evil_alien)
            pygame.mixer.Sound.play(self.giant_sound)

    def _update_evil_aliens(self):  # Same as _update_civilian_oranges
        self.evil_aliens.update()
        if pygame.sprite.spritecollideany(self.character, self.evil_aliens):
            pygame.mixer.Sound.play(self.giant_hurt_sound)
            sleep(.2)
            pygame.mixer.Sound.play(self.hurt_sound)
            sleep(.6)
            self._character_hit()
            self._character1_hit()

    def _create_alien(self):  # Same as _create_civilian_orange
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
            pygame.mixer.Sound.play(self.alien_sound)

    def _update_aliens(self):  # Same as _update_civilian_oranges
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.character, self.aliens):
            pygame.mixer.Sound.play(self.crash_sound)
            sleep(.2)
            pygame.mixer.Sound.play(self.hurt_sound)
            pygame.mixer.Sound.play(self.ouch_sound)
            sleep(.6)
            self._character_hit()
            self._character1_hit()

    def _create_alien1(self):  # Same as _create_civilian_orange
        if random() < self.settings.alien1_frequency:
            alien1 = Alien1(self)
            self.alien1s.add(alien1)
            pygame.mixer.Sound.play(self.alien_sound)

    def _update_alien1s(self):  # Same as _update_civilian_oranges
        self.alien1s.update()
        if pygame.sprite.spritecollideany(self.character, self.alien1s):
            pygame.mixer.Sound.play(self.crash_sound)
            sleep(.2)
            pygame.mixer.Sound.play(self.hurt_sound)
            pygame.mixer.Sound.play(self.ouch_sound)
            sleep(.6)
            self._character_hit()
            self._character1_hit()

    def _create_meteor(self):  # Same as _create_civilian_orange
        if random() < self.settings.meteor_frequency:
            meteor = Meteor(self)
            self.meteors.add(meteor)
            pygame.mixer.Sound.play(self.meteor_strike_sound)

    def _update_meteors(self):  # Same as _update_civilian_oranges
        self.meteors.update()
        if pygame.sprite.spritecollideany(self.character, self.meteors):
            pygame.mixer.Sound.play(self.hurt_sound)
            sleep(.2)
            pygame.mixer.Sound.play(self.explosion_sound)
            sleep(.6)
            self._character_hit()
            self._character1_hit()

    def _create_blue_planet_move_left(self):  # Same as _create_civilian_orange
        if random() < self.settings.blue_planet_move_left_frequency:
            pygame.mixer.Sound.play(self.hey_sound)
            blue_planet_move_left = Blue_Planet_Move_Left(self)
            self.blue_planet_move_lefts.add(blue_planet_move_left)

    def _update_blue_planet_move_lefts(self):  # Same as _update_civilian_oranges
        self.blue_planet_move_lefts.update()

    def _create_blue_planet_move_right(self):  # Same as _create_civilian_orange
        if random() < self.settings.blue_planet_move_right_frequency:
            pygame.mixer.Sound.play(self.hi_sound)
            blue_planet_move_right = Blue_Planet_Move_Right(self)
            self.blue_planet_move_rights.add(blue_planet_move_right)

    def _update_blue_planet_move_rights(self):  # Same as _update_civilian_oranges
        self.blue_planet_move_rights.update()

    def _character_hit(self):
        if self.stats.characters_left > 0:  # Sets lives to 0
            self.stats.characters_left -= 1  # Takes one life away from lives
            self.sb.prep_characters()  # Updates the display of lives

            # Resets sprites
            self.bullets.empty()
            self.bullet1s.empty()
            self.shields.empty()
            self.shield1s.empty()
            self.beams.empty()
            self.civilian_oranges.empty()
            self.civilian_purples.empty()
            self.civilian_turquoises.empty()
            self.civilian_pinks.empty()
            self.civilian_reds.empty()
            self.civilian_yellows.empty()
            self.evil_aliens.empty()
            self.aliens.empty()
            self.alien1s.empty()
            self.meteors.empty()
            self.blue_planet_move_lefts.empty()
            self.blue_planet_move_rights.empty()

            self.character.midbottom_character()
        else:
            pygame.mixer.music.stop()  # Stops continuous music
            pygame.mixer.Sound.play(self.loss_sound)  # Plays sound
            pygame.mixer.Sound.play(self.what_sound)  # Plays sound
            self.stats.game_active = False  # Sets game to an inactive state
            pygame.mouse.set_visible(True)  # Sets mouse visible
        if self.stats.characters_left == 2:  # If 2 lives left
            self.character.image = self.character.image_hurt1  # Change image
        if self.stats.characters_left == 1:  # If 1 lives left
            self.character.image = self.character.image_hurt2  # Change image
        if self.stats.characters_left == 0:  # If 0 lives left
            self.character.image = self.character.image_hurt3  # Change image

    def _character1_hit(self):  # Same as _character_hit
        if self.stats.deads_left > 0:
            self.stats.deads_left -= 1
            self.sb.prep_character1s()

            self.bullets.empty()
            self.bullet1s.empty()
            self.shields.empty()
            self.shield1s.empty()
            self.beams.empty()
            self.civilian_oranges.empty()
            self.civilian_purples.empty()
            self.civilian_turquoises.empty()
            self.civilian_pinks.empty()
            self.civilian_reds.empty()
            self.civilian_yellows.empty()
            self.evil_aliens.empty()
            self.aliens.empty()
            self.alien1s.empty()
            self.meteors.empty()
            self.blue_planet_move_lefts.empty()
            self.blue_planet_move_rights.empty()

            self.character1.midbottom_character1()
        else:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(self.loss_sound)
            pygame.mixer.Sound.play(self.what_sound)
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        if self.stats.deads_left == 2:
            self.character1.image = self.character1.image_hurt1
        if self.stats.deads_left == 1:
            self.character1.image = self.character1.image_hurt2
        if self.stats.deads_left == 0:
            self.character1.image = self.character1.image_hurt3

    def _update_screen(self):
        # Puts background on screen
        self.background1.blitme()
        self.background.blitme()

        self.sb.show_score()  # Puts lives on screen
        if self.character1.number == 1:  # If variable is 1
            self.sb.show_score1()  # Puts lives on screen for player 2

        for bullet in self.bullets.sprites():  # For loop
            bullet.draw_bullet()  # Draws bullet on screen
        for bullet1 in self.bullet1s.sprites():  # For loop
            bullet1.draw_bullet1()  # Draws bullet on screen
        for shield in self.shields.sprites():  # For loop
            shield.draw_shield()  # Draws shield on screen
        for shield1 in self.shield1s.sprites():  # For loop
            shield1.draw_shield1()  # Draws shield on screen
        for beam in self.beams.sprites():  # For loop
            beam.draw_beam()  # Draws beam on screen

        # Draws sprites to screen
        self.civilian_oranges.draw(self.screen)
        self.civilian_purples.draw(self.screen)
        self.civilian_turquoises.draw(self.screen)
        self.civilian_pinks.draw(self.screen)
        self.civilian_reds.draw(self.screen)
        self.civilian_yellows.draw(self.screen)
        self.evil_aliens.draw(self.screen)
        self.aliens.draw(self.screen)
        self.alien1s.draw(self.screen)
        self.meteors.draw(self.screen)
        self.blue_planet_move_lefts.draw(self.screen)
        self.blue_planet_move_rights.draw(self.screen)

        # If civilian is hit
        if self.character1.numbers == 1:  # If variable is 1
            pygame.mixer.music.stop()  # Stops continuous music
            pygame.mixer.Sound.play(self.blackhole_sound)  # Plays sound
            # Resets sprites
            self.civilian_oranges.empty()
            self.civilian_purples.empty()
            self.civilian_turquoises.empty()
            self.civilian_pinks.empty()
            self.civilian_reds.empty()
            self.civilian_yellows.empty()
            self.evil_aliens.empty()
            self.aliens.empty()
            self.alien1s.empty()
            self.meteors.empty()
            self.blue_planet_move_lefts.empty()
            self.blue_planet_move_rights.empty()
        if self.character1.numbers2 == 1:  # If variable is 1
            self.blackhole2.blitme()  # Puts blackhole on screen
        if self.character1.numbers1 == 1:  # If variable is 1
            self.blackhole1.blitme()  # Puts blackhole on screen
        if self.character1.numbers == 1:  # If variable is 1
            self.blackhole.blitme()  # Puts blackhole on screen
            self.play_press1.draw_press1()  # Puts button on screen
            self.king.blitme()  # Puts king on screen
            self.text.blitme()  # Puts text on screen
            self.play_message.draw_message()  # Puts textbox on screen
        if self.character1.numbers1 == 1:  # If variable is 1
            self.play_message1.draw_message1()  # Puts textbox on screen
            self.play_press2.draw_press2()  # Puts button on screen
        if self.character1.numbers2 == 1:  # If variable is 1
            self.play_message2.draw_message2()  # Puts textbox on screen
            self.play_press3.draw_press3()  # Puts button on screen
        self.character.blitme()  # Puts player 1 on screen
        if self.character1.number == 1:  # If variable is 1
            self.character1.blitme()  # Puts player 2 on screen
        if self.character1.numbers3 == 1:  # If variable is 1
            self.blackhole3.blitme()  # Puts blackhole on screen
            self.play_press4.draw_press4()  # Puts button on screen
            self.play_vastness.draw_vastness()  # Puts text on screen
        if self.character1.numbers4 == 1:  # If variable is 1
            self.stats.game_active = False  # Sets game to an inactive state
            pygame.mouse.set_visible(True)  # Sets mouse invisible

        if not self.stats.game_active:
            self.character1.number = 0  # Sets variable to 1 for player 1 game
            self.character1.numbers = 0  # Sets variable to 1 for player 1 game
            self.character1.numbers1 = 0  # Sets variable to 1 for player 1 game
            self.character1.numbers2 = 0  # Sets variable to 1 for player 1 game
            self.character1.numbers3 = 0  # Sets variable to 1 for player 1 game
            self.character1.numbers4 = 0  # Sets variable to 1 for player 1 game
            pygame.mixer.Sound.stop(self.blackhole_sound)  # Plays sound
            # Draws sprites to screen
            self.character.image = self.character.image_regular
            self.character1.image = self.character1.image_regular
            self.click.blitme()
            self.play_button.draw_button()
            self.play_button1.draw_button1()
            self.play_quit.draw_quit()
            self.play_title.draw_title()
            self.play_creator.draw_creator()
            self.play_name.draw_name()
            self.logo.blitme()
            self.play_instructions_alien.draw_instructions_alien()
            self.play_instructions_meteor.draw_instructions_meteor()
            self.play_instructions_lives.draw_instructions_lives()
            self.play_instructions_friend.draw_instructions_friend()
            self.play_instructions_move.draw_instructions_move()
            self.play_instructions_move1.draw_instructions_move1()
            self.play_instructions_shoot.draw_instructions_shoot()
            self.play_instructions_shoot1.draw_instructions_shoot1()
            if self.sb.stats.score > 0 and self.sb.stats.score >= self.sb.stats.high_score:  # If score is greater
                # Then 0 and score is greater than or equal to high score
                self.play_hs.draw_hs()  # Draw high score on screen

        pygame.display.flip()  # Makes most recently drawn screen visible


if __name__ == '__main__':  # Runs the game
    ai = Game()
    ai.run_game()
