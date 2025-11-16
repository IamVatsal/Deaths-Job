# Death's Job

A 2D arcade-style game built with Pygame where you control a ghost navigating through obstacles in the sky. Inspired by Flappy Bird mechanics with enhanced movement controls and a splash screen.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/pygame--ce-latest-green.svg)

## 🎮 About

In Death's Job, you play as a ghost navigating through pairs of obstacles (top and bottom) while managing gravity and momentum. The game features smooth physics, pixel-perfect collision detection with mask-based collision, a scrolling cloud background, sound effects, background music, and an interactive castle-themed splash screen.

## 🎥 Screen Recording


https://github.com/user-attachments/assets/f5515ea4-7d1e-4d43-94c5-df0f99ec18ab



## ✨ Features

- **Interactive Splash Screen**: Start screen with hover effects on buttons (Start/Exit)
- **Flappy-style mechanics**: Jump/flap with cooldown system and forward momentum
- **Horizontal movement**: Control left/right direction during flight with sprite flipping
- **Physics simulation**: Realistic gravity, velocity, and horizontal damping
- **Dynamic obstacles**: Randomized top/bottom obstacle pairs with recycling system
- **Pixel-perfect collision**: Mask-based collision detection for accurate gameplay
- **Sound system**: Jump sound effects, button clicks, collision sounds, and background music
- **Scrolling background**: Infinite parallax cloud effect
- **Game state management**: Smooth transitions between splash, playing, and game over states
- **Auto-reset**: Automatic restart on collision with restart delay
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
| **Left Arrow / A** | Face and move left |
| **Right Arrow / D** | Face and move right |
| **Escape** | Return to splash screen (during gameplay) / Quit (from splash) |
| **Mouse Click** | Interact with buttons on splash screen (Start/Exit) |

## 🛠️ Project Structure

```
Death's Job/
├── main.py                    # Entry point
├── requirements.txt           # Python dependencies (pygame-ce, python-dotenv)
├── .env                       # Game configuration (physics, paths, etc.)
├── .gitignore                 # Git ignore file
├── LICENSE                    # MIT License
├── README.md                  # This file
├── Classes/
│   ├── Game.py               # Main game loop and state management
│   ├── GameState.py          # Game state enum (SPLASH, PLAYING, PAUSED, GAME_OVER, EXIT)
│   ├── Player.py             # Player physics, controls, and sprite management
│   ├── Entity.py             # Base class for game entities
│   ├── Obstacle.py           # Individual obstacle with collision mask
│   ├── Obstacles.py          # Obstacle manager (spawning, recycling, collision)
│   ├── Background.py         # Scrolling background system
│   ├── SplashScreen.py       # Start screen with interactive buttons
│   ├── Button.py             # Button class with hover effects
│   └── Env.py                # Environment configuration loader
└── data/
    ├── gfx/                   # Graphics folder
    │   ├── ghost.png         # Player sprite
    │   ├── poll_new.png      # Obstacle sprite
    │   ├── background.png    # Scrolling background
    │   ├── back.png          # Splash screen background
    │   ├── start_button_normal.png
    │   ├── start_button_hover.png
    │   ├── exit_button_normal.png
    │   └── exit_button_hover.png
    └── sfx/                   # Sound effects folder
        ├── flap.wav          # Jump sound
        ├── button_click.wav  # Button click sound
        ├── collision_sound.wav # Collision sound
        └── bgm-blues-guitar-loop-192099.mp3 # Background music
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
  - Initial velocity: -50 units/s (horizontal)
- **Obstacles**:
  - Vertical gap: 250-350 pixels (randomized)
  - Horizontal gap: 150-250 pixels (randomized)
  - Speed: 35 units/s (matches background scroll speed)
  - Number: 10 active obstacles
  - Recycling: Obstacles off-screen are moved to the end
  - Collision: Pixel-perfect mask-based collision detection
- **Background**:
  - Scroll speed: 35 units/s
  - Infinite scrolling with seamless loop

### Key Components

- **[`main.py`](main.py)**: Entry point that initializes [`Game1`](Classes/Game.py) and starts the game loop
- **[`Classes/Game.py`](Classes/Game.py)**: Main game class with event handling, update loop, rendering, and sound management
- **[`Classes/GameState.py`](Classes/GameState.py)**: Enum defining game states (SPLASH, PLAYING, PAUSED, GAME_OVER, EXIT)
- **[`Classes/Player.py`](Classes/Player.py)**: Player physics, sprite flipping, collision mask, and movement logic
- **[`Classes/Obstacles.py`](Classes/Obstacles.py)**: Manages obstacle spawning, updating, recycling, and collision detection
- **[`Classes/Obstacle.py`](Classes/Obstacle.py)**: Individual obstacle with movement, collision mask, and scaled sprite
- **[`Classes/Background.py`](Classes/Background.py)**: Infinite scrolling background system with dual-image technique
- **[`Classes/SplashScreen.py`](Classes/SplashScreen.py)**: Interactive start screen with button hover effects
- **[`Classes/Button.py`](Classes/Button.py)**: Button class with hover state and click detection
- **[`Classes/Entity.py`](Classes/Entity.py)**: Base class for all game entities with position (Vector2), velocity, and image loading
- **[`Classes/Env.py`](Classes/Env.py)**: Loads configuration from [.env](.env) file using python-dotenv

## 🎨 Customization

### Gameplay Settings

Edit [.env](.env) to customize gameplay:

```env
# Screen settings
SCREEN_WIDTH = 1296
SCREEN_HEIGHT = 729
FPS = 60
WINDOW_TITLE = "Death's Job"

# Player physics
PLAYER_GRAVITY = 800
PLAYER_JUMP_STRENGTH_UP = -200
PLAYER_JUMP_STRENGTH_FORWARD = 50
PLAYER_JUMP_COOLDOWN = 0.05
PLAYER_HORIZONTAL_DAMPING = 200
PLAYER_MIN_HORIZONTAL_VELOCITY = -50

# Player movement
PLAYER_MOVE_SPEED_VERTICAL = 400
PLAYER_MOVE_SPEED_HORIZONTAL = 300

# Obstacle settings
OBSTACLE_VERTICAL_GAP_MIN = 250
OBSTACLE_VERTICAL_GAP_MAX = 350
OBSTACLE_HORIZONTAL_GAP_MIN = 150
OBSTACLE_HORIZONTAL_GAP_MAX = 250

# Background
BACKGROUND_SCROLL_SPEED = 35

# Asset paths can also be customized
GHOST_SPRITE_PATH = 'data/gfx/ghost.png'
BACKGROUND_PATH = 'data/gfx/background.png'
# ... and more
```

### Obstacle Count

Modify the number of obstacles in [`Classes/Game.py`](Classes/Game.py):

```python
self.obstacles = Obstacles(num_of_obstacles=10)  # Change this value
```

## 🎯 Game Mechanics

### Physics System
- **Gravity**: Constant downward acceleration applied each frame
- **Velocity**: Uses pygame's Vector2 for precise float-based positioning
- **Damping**: Horizontal velocity gradually decreases over time
- **Jump**: Applies upward and forward impulse with cooldown to prevent spam

### Collision Detection
- **Two-phase detection**: 
  1. Rectangle-based broad phase for performance
  2. Mask-based pixel-perfect collision for accuracy
- **Sound feedback**: Collision sound plays on impact
- **Auto-reset**: 20-frame delay before returning to splash screen

### Obstacle System
- **Initial spawn**: Obstacles spawn with randomized gaps on game start
- **Recycling**: When an obstacle goes off-screen (left), it's repositioned to the right
- **Synchronized pairs**: Top and bottom obstacles always share the same X position
- **Random gaps**: Both horizontal and vertical gaps are randomized within configured ranges

### Sound System
- **Background music**: Loops continuously throughout gameplay
- **Jump sound**: Plays on each jump with reduced volume (0.1)
- **Button clicks**: Feedback when interacting with UI
- **Collision sound**: Plays when player hits an obstacle

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

**My Skils** 😅

![Death Game FF](https://github.com/user-attachments/assets/dacf298d-1135-41b5-8e59-7bb4df63ec72)

## 🙏 Acknowledgments

- Inspired by the classic Flappy Bird game
- Built with Pygame Community Edition
- Uses python-dotenv for configuration management
- Background music: "Blues Guitar Loop" by Ncone

---

Made with ❤️ using Python and Pygame
