# Death's Job

A 2D arcade-style game built with Pygame where you control a ghost navigating through obstacles in the sky. Inspired by Flappy Bird mechanics with enhanced movement controls and a splash screen.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/pygame--ce-latest-green.svg)

## 🎮 About

In Death's Job, you play as a ghost navigating through pairs of obstacles (top and bottom) while managing gravity and momentum. The game features smooth physics, collision detection, a scrolling cloud background, and a castle-themed splash screen.

## ✨ Features

- **Splash Screen**: Interactive start screen with hover effects
- **Flappy-style mechanics**: Jump/flap with cooldown system and forward momentum
- **Horizontal movement**: Control left/right direction during flight
- **Physics simulation**: Realistic gravity, velocity, and horizontal damping
- **Dynamic obstacles**: Randomized top/bottom obstacle pairs with recycling system
- **Collision detection**: Real-time collision with visual debugging
- **Scrolling background**: Infinite parallax cloud effect
- **Game state management**: Smooth transitions between splash, playing, and game over states
- **Auto-reset**: Automatic restart on collision
- **60 FPS gameplay**: Smooth animations and responsive controls

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
| **Space** | Start game (from splash) / Flap/Jump (during gameplay) |
| **A** | Face and move left |
| **D** | Face and move right |
| **Escape** | Return to splash screen (during gameplay) / Quit (from splash) |
| **Mouse Click** | Start game (click start button on splash screen) |

## 🛠️ Project Structure

```
Death's Job/
├── main.py                    # Entry point
├── requirements.txt           # Python dependencies
├── .env                       # Game configuration
├── LICENSE                    # MIT License
├── README.md                  # This file
├── Classes/
│   ├── Game.py               # Main game loop and state management
│   ├── GameState.py          # Game state enum (SPLASH, PLAYING, PAUSED, GAME_OVER)
│   ├── Player.py             # Player physics and controls
│   ├── Entity.py             # Base class for game entities
│   ├── Obstacle.py           # Individual obstacle with collision
│   ├── Obstacles.py          # Obstacle manager (spawning, recycling)
│   ├── Background.py         # Scrolling background system
│   ├── SplashScreen.py       # Start screen with interactive button
│   └── Env.py                # Environment configuration loader
└── data/
    └── gfx/
        ├── ghost.png         # Player sprite
        ├── fence.png         # Obstacle sprite
        ├── Clouds_1.png      # Background image
        └── castle.png        # Splash screen background
```

## 🔧 Technical Details

- **Game Engine**: Pygame Community Edition (pygame-ce)
- **Resolution**: 1296x729 pixels (configurable via [.env](.env))
- **Frame Rate**: 60 FPS
- **Physics** (configurable in [.env](.env)):
  - Gravity: 800 units/s²
  - Jump strength: -200 (upward), 50 (forward)
  - Jump cooldown: 0.05 seconds
  - Horizontal damping: 200 units/s²
  - Minimum horizontal velocity: -50 units/s
- **Obstacles**:
  - Vertical gap: 250-350 pixels (randomized)
  - Horizontal gap: 150-250 pixels (randomized)
  - Speed: 35 units/s
  - Number: 10 active obstacles
  - Recycling: Obstacles off-screen are moved to the end

### Key Components

- **[`main.py`](main.py)**: Entry point that initializes [`Game`](Classes/Game.py) and starts the game loop
- **[`Classes/Game.py`](Classes/Game.py)**: Main game class with event handling, update loop, and rendering
- **[`Classes/GameState.py`](Classes/GameState.py)**: Enum defining game states (SPLASH, PLAYING, PAUSED, GAME_OVER)
- **[`Classes/Player.py`](Classes/Player.py)**: Player physics, sprite flipping, and movement logic
- **[`Classes/Obstacles.py`](Classes/Obstacles.py)**: Manages obstacle spawning, updating, and collision detection
- **[`Classes/Obstacle.py`](Classes/Obstacle.py)**: Individual obstacle with movement and collision visualization
- **[`Classes/Background.py`](Classes/Background.py)**: Infinite scrolling background system
- **[`Classes/SplashScreen.py`](Classes/SplashScreen.py)**: Interactive start screen with button hover effects
- **[`Classes/Entity.py`](Classes/Entity.py)**: Base class for all game entities with position, velocity, and image loading
- **[`Classes/Env.py`](Classes/Env.py)**: Loads configuration from [.env](.env) file using python-dotenv
- **[`utils.py`](utils.py)**: Utility functions including [`clamp`](utils.py) for boundary checking

## 🎨 Customization

### Gameplay Settings

Edit [.env](.env) to customize gameplay:

```env
# Screen settings
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 729
FPS = 60

# Player physics
PLAYER_GRAVITY = 800
PLAYER_JUMP_STRENGTH_UP = -200
PLAYER_JUMP_STRENGTH_FORWARD = 50
PLAYER_JUMP_COOLDOWN = 0.05
PLAYER_HORIZONTAL_DAMPING = 200
PLAYER_MIN_HORIZONTAL_VELOCITY = -50

# Obstacle settings
OBSTACLE_VERTICAL_GAP_MIN = 250
OBSTACLE_VERTICAL_GAP_MAX = 350
OBSTACLE_HORIZONTAL_GAP_MIN = 150
OBSTACLE_HORIZONTAL_GAP_MAX = 250

# Background
BACKGROUND_SCROLL_SPEED = 35
```

### Obstacle Count

Modify the number of obstacles in [`Classes/Game.py`](Classes/Game.py):

```python
self.obstacles = Obstacles(num_of_obstacles=10)  # Change this value
```

## 🎯 Game Mechanics

1. **Start**: Click the green button or press Space on the splash screen
2. **Movement**: Use A/D to control horizontal direction while jumping with Space
3. **Physics**: Gravity pulls you down, horizontal damping slows forward movement
4. **Obstacles**: Navigate through gaps between top and bottom obstacles
5. **Collision**: Hitting any obstacle resets the game to the splash screen
6. **Infinite Loop**: Obstacles recycle endlessly for continuous gameplay

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
- Uses python-dotenv for configuration management

---

Made with ❤️ using Python and Pygame