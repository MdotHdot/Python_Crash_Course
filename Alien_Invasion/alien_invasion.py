#this is the alien invasion Class for displaying the screen
# running and quitting the game
import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from scoreboard import Scoreboard
from menu_ship import MenuShip
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #Start ALien Invasion in an active state
        self.game_active = False
        #Create an instance to store settings.
        
        self.settings = Settings()       
        self.clock = pygame.time.Clock()        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
           
         # Create an instance to store game statistics, and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.button_hits = 0
        self.button_hits_to_start = 3 
        self.menu_ship = MenuShip(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        #self.pilot = Pilot(self)
        self.aliens = pygame.sprite.Group()
        
        
        self._create_fleet()
        
        # Set the background color
        self.bg_color = (0,0,0)
        #Start Alien Invasion in an inactive state
        # self.game_active = False
        # Make the Play button.
        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:            
                self.ship.update()               
                self._update_aliens()
                
            else:
                self.menu_ship.update()
                self.play_button.update()
                self.check_bullet_button_collisions()
                
            self._update_bullets()               
            self._update_screen()  
            self.clock.tick(60) # Limit to 60 frames per second
            
    def _check_events(self):
        '''Watch for keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                    
    def _check_play_button(self, mouse_pos):
        '''Start a new game when Player clicks Play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)      
        if button_clicked  and not self.game_active :
            #reset game settings.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
    
            

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()
        elif event.key == pygame.K_UP and not self.game_active:
            self.menu_ship.moving_up = True
        elif event.key == pygame.K_DOWN and not self.game_active:
            self.menu_ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.game_active:    
                self._fire_bullet()
            else:
                self._fire_menu_bullet()
        
    
    def _start_game(self):
                    #reset game statistics
            self.stats.reset_stats()
            self.game_active = True
            
            #get rid of remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            #reset screen for next game
            self._create_fleet()
            self.ship.center_ship()
            
            #Hide the mouse cursor
            pygame.mouse.set_visible(False)

            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False        
        elif event.key == pygame.K_UP and not self.game_active:
            self.menu_ship.moving_up = False
        elif event.key == pygame.K_DOWN and not self.game_active:
            self.menu_ship.moving_down = False
            
    def _fire_bullet(self):
        """Fire a bullet if limit not reached yet."""
        if len(self.bullets) < self.settings.bullets_allowed:       
            new_bullet = Bullet(self, self.ship)
            self.bullets.add(new_bullet)
            
    def _fire_menu_bullet(self, ):
        """Fire a bullet if limit not reached yet."""
        if len(self.bullets) < self.settings.bullets_allowed:       
            new_bullet = Bullet(self, self.menu_ship)
            self.bullets.add(new_bullet) 
                      
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        #checks for for remaining bullets and removes them
        if self.game_active and not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            #Level increment
            self.stats.level += 1
            self.sb.prep_level()
            
         # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()
        

        
    def  check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
    def check_bullet_button_collisions(self):
    
        "'Responds to bullet menu collision when game not active"
        
        # We iterate over a copy of the bullets in case we remove them
        for bullet in self.bullets.copy(): 
            
            # 1. Check if the bullet's rect hits the button's rect
            if bullet.rect.colliderect(self.play_button.rect):              
                # 2. A hit occurred: Increment the counter
                self.button_hits += 1        
                # 3. Remove the bullet so it doesn't hit the button twice 
                self.bullets.remove(bullet)
            # checks counter to start gsame 
            if self.button_hits >= self.button_hits_to_start:    
                sleep(1)
                self._start_game()
        
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left.
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1       
            #get rid of any remaining aliens and bullets.
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.settings.initialize_dynamic_settings()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(1)
        else:
            self.aliens.empty()
            self.aliens.empty()
            self.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break
            
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        #look for aline-shp collision 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
       # Check for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
        
        
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
   
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - (3 * alien_height)):
            while current_x < (self.settings.screen_width - (2 * alien_width)):
                self._create_alien(current_x, current_y)
                current_x += alien_width * 2
                
                #Finish a row and reset x value and increment y value
            current_x = alien_width
            current_y += alien_height * 2

    
    def _create_alien(self, x_position, y_position):
        if not self.game_active:
            False
        else:
            """Create an alien and place it in the row."""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)
            #Check fo collision with ship
        
    

    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
          
    def _update_screen(self):
                  # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            #self.pilot.blitme()
            self.aliens.draw(self.screen)
            #Draw the Scoreboard 
            self.sb.show_score()
            #Draw the play button if the game is inactive
            if not self.game_active:
                self.play_button.draw_button()            
                self.menu_ship.blitme()
                
                       
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            

                    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai= AlienInvasion()
    ai.run_game()            