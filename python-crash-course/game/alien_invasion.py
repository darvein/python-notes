import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.st = Settings()
        self.screen = pygame.display.set_mode((self.st.screen_width, self.st.screen_height))
        pygame.display.set_caption("Alienz Aqui!!")
        self.bg_color = (220, 220, 220)
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.scoreboard = ScoreBoard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Gogogo!")

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                self._check_keydown_events(e)
            elif e.type == pygame.KEYUP:
                self._check_keyup_events(e)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self._check_play_button(pos)
    
    def _check_play_button(self, pos):
        clicked = self.play_button.rect.collidepoint(pos)
        if clicked and not self.stats.game_active:
            self.st.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif e.key == pygame.K_q:
            sys.exit()
        elif e.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.st.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Remove bullets
        for b in self.bullets.copy():
            if b.rect.bottom <= 0:
                self.bullets.remove(b)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for a in collisions.values():
                self.stats.score += self.st.alien_points * len(a)
            #self.stats.score += self.st.alien_points
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.st.increase_speed()

            self.stats.level += 1
            self.scoreboard.prep_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_screen(self):
        self.screen.fill(self.st.bg_color)
        self.ship.blitme()

        for b in self.bullets.sprites():
            b.draw_bullet()

        self.aliens.draw(self.screen)
        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self)
        #self.aliens.add(alien)
        #alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size

        available_space_x = self.st.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.st.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for n in range(number_rows):
            for a in range(number_aliens_x):
                self._create_alien(a, n)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.st.alien_fleet_drop_speed
        self.st.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for a in self.aliens.sprites():
            if a.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
