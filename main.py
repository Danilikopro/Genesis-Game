"""Genesis - OS Evolution Game
Main entry point for the game
"""
import tkinter as tk
from tkinter import messagebox
from config import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE
from epochs.epoch_1984 import Epoch1984
from epochs.epoch_1995 import Epoch1995
from epochs.epoch_2005 import Epoch2005
from epochs.epoch_2015 import Epoch2015
from epochs.epoch_2025 import Epoch2025
from mechanics.resources import Resources
from mechanics.progression import Progression

class GenesisGame:
    """Main game class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(GAME_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        
        # Initialize game state
        self.current_epoch_index = 0
        self.epochs = [
            Epoch1984(),
            Epoch1995(),
            Epoch2005(),
            Epoch2015(),
            Epoch2025()
        ]
        self.current_epoch = self.epochs[0]
        self.progression = Progression()
        
        # Create main UI
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI"""
        # Title
        title_label = tk.Label(
            self.root,
            text=GAME_TITLE,
            font=('Arial', 24, 'bold'),
            fg='#00FFFF',
            bg='#000000'
        )
        title_label.pack(pady=20)
        
        # Epoch display
        self.epoch_label = tk.Label(
            self.root,
            text=f"Epoch: {self.current_epoch.year} - {self.current_epoch.name}",
            font=('Arial', 16),
            fg='#FFFFFF',
            bg='#000000'
        )
        self.epoch_label.pack(pady=10)
        
        # Resources display
        self.resources_label = tk.Label(
            self.root,
            text=f"CPU: {self.current_epoch.cpu_speed} MHz | Memory: {self.current_epoch.memory} MB",
            font=('Arial', 12),
            fg='#00FF00',
            bg='#000000'
        )
        self.resources_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#000000')
        button_frame.pack(pady=20)
        
        # Progress button
        progress_btn = tk.Button(
            button_frame,
            text="Progress to Next Epoch",
            command=self.next_epoch,
            bg='#008080',
            fg='#FFFFFF',
            padx=20,
            pady=10
        )
        progress_btn.pack(side=tk.LEFT, padx=10)
        
        # View current epoch info
        info_btn = tk.Button(
            button_frame,
            text="View Epoch Info",
            command=self.view_epoch_info,
            bg='#008080',
            fg='#FFFFFF',
            padx=20,
            pady=10
        )
        info_btn.pack(side=tk.LEFT, padx=10)
        
        # Exit button
        exit_btn = tk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            bg='#800000',
            fg='#FFFFFF',
            padx=20,
            pady=10
        )
        exit_btn.pack(side=tk.LEFT, padx=10)
        
    def next_epoch(self):
        """Progress to the next epoch"""
        if self.current_epoch_index < len(self.epochs) - 1:
            self.current_epoch_index += 1
            self.current_epoch = self.epochs[self.current_epoch_index]
            self.progression.complete_task()
            self.update_display()
        else:
            messagebox.showinfo("Victory!", "You have successfully designed all 5 OS generations!")
    
    def view_epoch_info(self):
        """Display current epoch information"""
        info = self.current_epoch.get_era_info()
        message = "\n".join([f"{k}: {v}" for k, v in info.items()])
        messagebox.showinfo("Epoch Information", message)
    
    def update_display(self):
        """Update the display with current epoch info"""
        self.epoch_label.config(
            text=f"Epoch: {self.current_epoch.year} - {self.current_epoch.name}"
        )
        self.resources_label.config(
            text=f"CPU: {self.current_epoch.cpu_speed} MHz | Memory: {self.current_epoch.memory} MB"
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = GenesisGame(root)
    root.mainloop()
