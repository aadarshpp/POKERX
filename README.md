
# POKERX

POKERX is a poker game developed in Python using `customtkinter` for the user interface, along with various other libraries for game mechanics and AI-based decision-making. You can either download the executable file (`POKERX.exe`) from the `Releases` section or clone the repository and run it in your local environment.

## Features

- **Interactive Poker Game**: A fully functional poker game with AI opponents.
- **AI Move Prediction**: The game includes AI for opponents, which calculates probability and makes decisions.
- **Custom UI**: Built using `customtkinter` for a visually appealing and intuitive interface.

## Requirements

To run POKERX, you will need Python 3.7+ and the following libraries:

- `customtkinter` for the UI
- `Pillow` for image handling

### Option 1: Running the Executable (`POKERX.exe`)

The easiest way to play the game is by simply running the `POKERX.exe` file, which can be found in the `Releases` section of this repository. No installation or additional setup is required. Just download and run the executable!

### Option 2: Running from Source (Cloning the Repository)

If you prefer to run the game from the source code, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/POKERX.git
   ```

2. **Navigate into the project directory**:

   ```bash
   cd POKERX
   ```

3. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the game**:

   After installing the dependencies, you can run the game by executing:

   ```bash
   python POKERX.py
   ```

## File Structure

```
POKERX/
├── IMAGES/
│   ├── CARDS/                   # Folder containing card images
│   └── ...                       # Other image assets (background, etc.)
├── PROGRAMS/
│   ├── COMPUTE.py               # Helper functions for computations
│   ├── PREDICT.py               # Functions for AI move and probability calculations
│   └── POKERX.py                # Main game logic and UI
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Troubleshooting

- If you run into any issues while running the game, ensure that all dependencies are installed correctly by running `pip install -r requirements.txt`.
- If you encounter problems with the `POKERX.exe`, make sure all necessary image files are present in the `IMAGES/` directory, as they are required for the game to run properly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
