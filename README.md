# Genesis - OS Evolution Game

A Python/Tkinter evolution game where you design your own operating system across 5 epochs from 1984 to 2025.

## Features

- **5 Evolutionary Epochs**: Journey from 1984 (Retro) through 2025 (Quantum)
- **OS Design Mechanics**: Build and customize your unique operating system
- **Progression System**: Advance through each era with new technologies
- **Resource Management**: Manage CPU power, memory, and innovation
- **Audio Effects**: Immersive sound for each era
- **Epoch-Specific Styling**: Each period has authentic visual design

## Project Structure

```
Genesis-Game/
├── main.py                 # Main entry point
├── config.py              # Configuration constants
├── base_os.py             # BaseOS class (foundation)
├── epochs/
│   ├── epoch_1984.py      # Retro era (1984)
│   ├── epoch_1995.py      # DOS/Win95 era (1995)
│   ├── epoch_2005.py      # Modern era (2005)
│   ├── epoch_2015.py      # Contemporary era (2015)
│   └── epoch_2025.py      # Quantum era (2025)
├── mechanics/
│   ├── progression.py     # Progression system
│   ├── resources.py       # Resource management
│   ├── puzzles.py         # Game mechanics & puzzles
│   └── audio.py           # Audio effects
├── ui/
│   ├── theme_1984.py      # Visual theme for 1984
│   ├── theme_1995.py      # Visual theme for 1995
│   ├── theme_2005.py      # Visual theme for 2005
│   ├── theme_2015.py      # Visual theme for 2015
│   └── theme_2025.py      # Visual theme for 2025
├── assets/
│   ├── sounds/            # Audio files
│   └── images/            # Image assets
└── README.md              # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- tkinter (usually comes with Python)
- Windows 10+ recommended (for best audio support)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Danilikopro/Genesis-Game.git
cd Genesis-Game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## Game Mechanics

### Epochs Overview

| Epoch | Year | Theme | Colors | Focus |
|-------|------|-------|--------|-------|
| Epoch 1 | 1984 | Retro | Amber/Black | CLI-style interface |
| Epoch 2 | 1995 | DOS/Win95 | Beige/Blue | Window management |
| Epoch 3 | 2005 | Modern | Silver/Blue | Modular design |
| Epoch 4 | 2015 | Contemporary | Dark/Neon | Advanced features |
| Epoch 5 | 2025 | Quantum | Cyan/Purple | AI integration |

### Core Systems

**Progression**: Complete tasks in each epoch to unlock the next
**Resources**: Balance CPU power, memory, and storage
**Mechanics**: Solve puzzles specific to each era's technology
**Win Condition**: Successfully design and implement all 5 OS generations

## Controls

- **Mouse**: Click to interact with UI elements
- **Keyboard**: Type commands (varies by epoch)
- **Buttons**: Progress through epochs and access menus

## Sound Effects

Each epoch includes period-appropriate audio:
- 1984: Beep/boop retro sounds
- 1995: Classic Windows chimes
- 2005: Modern UI sounds
- 2015: Subtle modern effects
- 2025: Electronic/futuristic sounds

## Development

### Base Classes

All epochs inherit from `BaseOS`:

```python
class BaseOS:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.resources = Resources()
        self.progression = Progression()
    
    def update_display(self):
        pass
    
    def handle_input(self, action):
        pass
```

### Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Credits

Developed as a passion project celebrating the evolution of operating systems.

## Status

🚀 **In Active Development**
- Core mechanics: ✅ Implemented
- All 5 epochs: ✅ Designed
- Audio system: ⏳ In progress
- UI styling: ⏳ In progress
- Testing: ⏳ Pending

## Roadmap

- [ ] Complete epoch implementations
- [ ] Add audio for each epoch
- [ ] Implement themed UI for all epochs
- [ ] Add achievement system
- [ ] Create high score tracking
- [ ] Release v1.0 on Steam

## Support

For bugs, feature requests, or questions, please open an Issue on GitHub.

---

**Made with ❤️ for retro computing enthusiasts**
