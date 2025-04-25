
# POKERX

POKERX is a Texas Hold'em poker game developed in Python using `customtkinter` for the user interface, along with various other libraries for game mechanics and decision-making. You can either download the executable file (`POKERX.exe`) from the `Releases` section or clone the repository and run it in your local environment.

## Features

- **Interactive Poker Game**: A fully functional Texas Hold'em poker game with computer-controlled opponents.
- **Move Prediction**: The game includes automated decision-making for the opponents based on game probabilities.
- **Custom UI**: Built using `customtkinter` for a visually appealing and intuitive interface.
- **Cheat Section**: A section for testing and using cheats to modify game parameters.
- **Learning Section**: A dedicated section to help you learn poker strategies.

## Requirements

To run POKERX, you will need Python 3.7+ and the following libraries:

- `customtkinter` for the UI
- `Pillow` for image handling

### Running the Executable (`POKERX.exe`)

The easiest way to play the game is by simply running the `POKERX.exe` file, which can be found in the `Releases` section of this repository. No installation or additional setup is required. Just download and run the executable!

### Running from Source (Cloning the Repository)

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
│   ├── CARDS/           # Card image assets
│   └── ...              # Other visual assets
│
├── COMPUTE.py           # Core logic for calculating scores and determining the best hands
├── PREDICT.py           # Probability calculations and prediction of the best move
├── POKERX.py            # Main file — handles game flow and UI
│
├── requirements.txt     # List of required Python packages
├── README.md            # Project overview and usage instructions
└── LICENSE              # MIT License (open-source)
```

## Troubleshooting

- If you run into any issues while running the game, ensure that all dependencies are installed correctly by running `pip install -r requirements.txt`.
- If you encounter problems with the `POKERX.py`, make sure all necessary image files are present in the `IMAGES/` directory, as they are required for the game to run properly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
