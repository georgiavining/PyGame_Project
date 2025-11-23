# PyGame_Project

## How to Run

1. **Clone the repo**  
```bash
git clone <repo_url>
```

2. **Navigate to the project folder**  
```bash
cd Pygame_Project
```

3. **Install depedencies**  
```bash
python -m pip install pygame
```

3. **Run the game**  
```bash
python main.py
```

## Folder Structure

```
PyGame Project/
├─ main.py              # Entry point to run the game
├─ config.py              # Constants
├─ game/                  # Core game logic
│  ├─ card.py
│  ├─ deck.py
│  ├─ hand.py
│  ├─ player.py
│  ├─ rules.py
│  ├─ turn_manager.py
│  └─ state.py
├─ ui/                    # Pygame UI components
│  ├─ screen.py
│  ├─ main_screen.py
|  ├─ game_over_screen.py
│  ├─ layout.py             # Layout function for player's hands
│  └─ visual_objects.py
├─ asets/          # Images for cards, deck, background
└─ README.md
```