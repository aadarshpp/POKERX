
# POKERX

POKERX is a poker game developed in Python using `customtkinter` for the user interface. This project provides an interactive poker game with various features, including playing against AI opponents, customizing game settings, and tracking the player's score.

## Features

- **Poker Gameplay**: Play poker with an AI opponent.
- **Graphics**: Uses images for cards and backgrounds.
- **Customizable Settings**: Configure game difficulty and options.
- **Game Flow**: Includes betting rounds, game actions (fold, call, raise), and a showdown.
- **Interactive Interface**: Buttons, labels, and dynamic elements to enhance user experience.

## How to Play

1. **Download the Game**:
   - Download the pre-built executable `POKERX.exe` from the [Releases](./releases) folder.

2. **Running the Game**:
   - Navigate to the `releases` folder where `POKERX.exe` is located.
   - Simply double-click the `POKERX.exe` to launch the game and start playing!

### File Structure

```
POKERX/
|-- IMAGES/
|   |-- CARDS/       # Folder containing card images
|   `-- ...          # Other image assets (backgrounds, UI elements)
|-- PROGRAMS/        # Python code and main game logic
|   `-- POKERX.py    # Main game script (for development only)
|-- releases/        # Pre-built executables (Nuitka)
|   `-- POKERX.exe   # Pre-built executable for easy access
`-- README.md        # Documentation
```

---

### Notes:

- **No Installation Required**: Since the game is packaged into a standalone `.exe`, you don't need to install Python or any dependencies to run the game.
- **Running the Executable**: Just double-click `POKERX.exe` from the `releases` folder, and the game will start immediately.

## Troubleshooting

- **Missing images error**: If the game doesn't start properly or you see an image-related error, make sure that the `IMAGES` folder and its contents are in the correct location relative to the executable. This is already handled if you're using the pre-built `.exe`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the Python and Tkinter communities for providing the tools to make this game possible.
- Special thanks to Pillow for image processing in Python.
