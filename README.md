# Death's Job

A 2D arcade-style game built with Pygame where you control a ghost navigating through the skies. Inspired by Flappy Bird mechanics with additional movement controls.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/pygame--ce-latest-green.svg)

## 🎮 About

In Death's Job, you play as a ghost with the challenging task of staying airborne while navigating through obstacles. The game features smooth gravity physics, a scrolling cloud background, and responsive controls.

## ✨ Features

- **Flappy-style mechanics**: Jump/flap with cooldown system
- **Full directional control**: Move in all four directions
- **Physics simulation**: Realistic gravity and velocity
- **Scrolling background**: Infinite cloud parallax effect
- **Smooth animations**: 60 FPS gameplay

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/deaths-job.git
   cd deaths-job
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the game:
   ```sh
   python main.py
   ```

## 🎮 Controls

| Key | Action |
|-----|--------|
| **Space** | Flap/Jump (upward thrust with forward momentum) |
| **W** | Move up |
| **S** | Move down |
| **A** | Move left |
| **D** | Move right |

## 🛠️ Project Structure

```
Death's Job/
├── main.py              # Game loop and rendering
├── player.py            # Player class with physics
├── requirements.txt     # Python dependencies
├── LICENSE             # MIT License
├── README.md           # This file
└── data/
    └── gfx/
        ├── ghost.png       # Player sprite
        └── Clouds_1.png    # Background image
```

## 🔧 Technical Details

- **Game Engine**: Pygame Community Edition (pygame-ce)
- **Resolution**: 864x486 pixels
- **Frame Rate**: 60 FPS
- **Physics**:
  - Gravity: 800 units/s²
  - Jump strength: -250 (upward), 50 (forward)
  - Jump cooldown: 0.05 seconds

### Key Components

- **[`main.py`](main.py)**: Contains the main game loop in [`main`](main.py) function and a helper [`clamp`](main.py) function for boundary checking
- **[`player.py`](player.py)**: Implements the [`Player`](player.py) class with physics, sprite loading, and movement parameters
- **[`requirements.txt`](requirements.txt)**: Lists pygame-ce as the only dependency

## 🎨 Customization

You can tweak gameplay by modifying values in [`player.py`](player.py):

```python
self.gravity = 800              # Fall speed
self.jump_strength_up = -250    # Jump height
self.jump_strength_forward = 50 # Horizontal boost on jump
self.jump_cooldown = 0.05       # Seconds between jumps
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vatsal Patel**

## 🙏 Acknowledgments

- Inspired by the classic Flappy Bird game
- Built with Pygame Community Edition

---

Made with ❤️ using Python and Pygame