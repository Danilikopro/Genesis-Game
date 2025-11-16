"""Epoch 2015 - Contemporary Era
Advanced features with dark/neon theme
"""
from base_os import BaseOS
from ui.theme_2015 import Theme2015

class Epoch2015(BaseOS):
    """Represents the 2015 Contemporary era epoch"""
    
    def __init__(self):
        super().__init__("Contemporary OS", 2015)
        self.theme = Theme2015()
        self.cpu_speed = 3000.0  # MHz
        self.memory = 8192  # MB (8GB)
        
    def update_display(self):
        """Update the display for 2015 era"""
        pass
    
    def handle_input(self, action):
        """Handle user input in 2015 style"""
        pass
    
    def get_era_info(self):
        """Return information about this era"""
        return {
            'year': self.year,
            'name': self.name,
            'theme': 'Dark/Neon Contemporary',
            'cpu_speed': f'{self.cpu_speed} MHz',
            'memory': f'{self.memory} MB'
        }
