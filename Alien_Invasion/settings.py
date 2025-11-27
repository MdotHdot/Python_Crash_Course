#settings class for the project
class Settings:
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        #ship settings
        
        self.ship_limit = 3
        
        
        #bullet settings
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (200, 180, 0)
        self.bullets_allowed = 20
        
       
        #How quickly the game speeds up 
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
        self.fleet_drop_speed = 10
        
        
        #menu button settings
        self.button_speed = 2
        
    def initialize_dynamic_settings(self):
        """Initialize thhe settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase Speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale