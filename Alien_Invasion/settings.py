#settings class for the project
class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 50, 230)
        
        #ship settings
        self.ship_speed = 3.5
        
        #bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (200, 180, 0)
        self.bullets_allowed = 20
        
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        


    
    
    