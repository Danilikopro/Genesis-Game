"""Epoch 1995 - DOS/Windows 95 Era
Window-based interface with beige/blue theme
"""
from base_os import BaseOS
from ui.theme_1995 import Theme1995

class Epoch1995(BaseOS):
    """Represents the 1995 DOS/Win95 era epoch"""
    
    def __init__(self):
        super().__init__("Windows 95", 1995)
        self.theme = Theme1995()
        self.cpu_speed = 100.0  # MHz
        self.memory = 8  # MB
        
    def update_display(self):
        """Update the display for 1995 era"""
        pass
    
    def handle_input(self, action):
        """Handle user input in 1995 style"""
        pass
    
    def get_era_info(self):
        """Return information about this era"""
        return {
            'year': self.year,
            'name': self.name,
            'theme': 'Beige/Blue Windows',
            'cpu_speed': f'{self.cpu_speed} MHz',
            'memory': f'{self.memory} MB'
        }
