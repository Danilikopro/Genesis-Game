"""Epoch 2005 - Modern Era
Modular design with silver/blue theme
"""
from base_os import BaseOS
from ui.theme_2005 import Theme2005

class Epoch2005(BaseOS):
    """Represents the 2005 Modern era epoch"""
    
    def __init__(self):
        super().__init__("Modern OS", 2005)
        self.theme = Theme2005()
        self.cpu_speed = 2000.0  # MHz
        self.memory = 1024  # MB
        
    def update_display(self):
        """Update the display for 2005 era"""
        pass
    
    def handle_input(self, action):
        """Handle user input in 2005 style"""
        pass
    
    def get_era_info(self):
        """Return information about this era"""
        return {
            'year': self.year,
            'name': self.name,
            'theme': 'Silver/Blue Modern',
            'cpu_speed': f'{self.cpu_speed} MHz',
            'memory': f'{self.memory} MB'
        }
