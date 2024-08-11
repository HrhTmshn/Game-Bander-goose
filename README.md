# Game Bander-goose

A Pygame-based mini-game where players control Bander-goose, a character that flies from left to right, catching valuable cargo while dodging incoming rockets. The game tracks the number of cargo collected, adding an element of challenge and competition.

#### Stack:

- [Python](https://www.python.org/downloads/)
- [Pygame](https://www.pygame.org/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.7 -m venv venv
   .\venv\Scripts\activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run the game:
   ```bash
   python main.py 
   ```

## Creating an Executable

To create an executable of the game, follow these steps:

1. Make sure PyInstaller is installed:
   ```bash
   pip install pyinstaller
   ```

2. Run PyInstaller with the spec file:
   ```bash
   pyinstaller exe/Bander-goose.spec
   ```

This will generate an executable in the dist folder, using the spec file located in the exe folder.