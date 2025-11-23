# PyGame_Project

## How to Run

1. Clone the repo:
   git clone <repo-link>

2. Navigate to the project folder:
   cd PyGame_Project

3. Install dependencies:
   python -m pip install pygame

4. Run the game:
   python main.py

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