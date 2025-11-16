"""Genesis Game Configuration
Central configuration file for all game settings
"""

# Window Settings
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
WINDOW_TITLE = "Genesis - OS Evolution Game"

# Game Settings
GAME_VERSION = "0.1.0"
DEBUG_MODE = True

# Epoch Definitions
EPOCH_CONFIG = {
    "1984": {
        "name": "Retro Era",
        "year": 1984,
        "background_color": "#000000",
        "text_color": "#FFBF00",
        "theme": "amber_black",
        "description": "CLI-style retro interface"
    },
    "1995": {
        "name": "DOS/Win95 Era",
        "year": 1995,
        "background_color": "#C0C0C0",
        "text_color": "#000000",
        "theme": "win95",
        "description": "Classic Windows 95 look"
    },
    "2005": {
        "name": "Modern Era",
        "year": 2005,
        "background_color": "#D3D3D3",
        "text_color": "#1E90FF",
        "theme": "modern",
        "description": "Contemporary design"
    },
    "2015": {
        "name": "Contemporary Era",
        "year": 2015,
        "background_color": "#1a1a1a",
        "text_color": "#00FF00",
        "theme": "dark_neon",
        "description": "Dark modern interface"
    },
    "2025": {
        "name": "Quantum Era",
        "year": 2025,
        "background_color": "#0a0a1a",
        "text_color": "#00FFFF",
        "theme": "quantum",
        "description": "Futuristic quantum design"
    }
}

# Resource Limits
RESOURCES = {
    "cpu_max": 100,
    "memory_max": 1000,
    "storage_max": 10000,
    "innovation_max": 500
}

# Audio Settings
AUDIO_ENABLED = True
AUDIO_VOLUME = 0.7
SFX_ENABLED = True

# Game Mechanics
TURNS_PER_EPOCH = 20
TASKS_PER_EPOCH = 5
PUZZLES_PER_EPOCH = 3

# File Paths
ASSETS_PATH = "assets/"
SOUNDS_PATH = "assets/sounds/"
IMAGES_PATH = "assets/images/"
