# Hanoi Towers Game

## Description
A Python implementation of the classic Tower of Hanoi puzzle, developed in two milestones.
- Milestone 1 is a console-based version of the game.
- Milestone 2 is a graphical user interface (GUI) version created using the graphics library.
Both versions use a stack data structure to manage the towers and disks. 

## How it works
- The user chooses the number of towers and disks for the game.
- The first tower starts with all disks arranged from largest to smallest.
- The user moves disks between towers following the Tower of Hanoi rules.
- The program checks whether each move is valid.
- The game tracks the number of moves needed to complete the puzzle.
- The game can be saved and loaded. 

## Game rules
A disk can be moved:
- One disk at a time
- Only from the top of a tower
- A larger disk cannot be placed on top of a smaller disk

## How to run

### Milestone 1
1. Open the `Milestone-1` folder.
2. Run `hanoi_towers_milestone_1.py`.
3. Choose:
   - `1` to start a new game.
   - `2` to resume a saved game.
4. Follow the instructions displayed in the console.

### Milestone 2 
1. Open the `Milestone-2` folder.
2. Make sure the required files are in the same folder.
3. Run `hanoi_towers_milestone_2.py`.
4. Use the graphical interface to play the game.

## Files

### Milestone 1 
- `hanoi_towers_milestone_1.py` - Main program containing the game logic and user interaction.
- `stack.py` - Stack implementation used to manage the towers.
### Milestone 2 
- `hanoi_towers_milestone_2.py` - Main program containing the graphical user interface and the game logic.
- `stack.py` - Stack implementation used to manage the towers.
- `graphics.py` - Graphics library required for the GUI version.
## Output
The program displays:
- The current tower arrangement
- Valid and invalid move messages
- The number of moves taken to complete the puzzle
- Save/load game messages
- A graphical representation of the game in Milestone 2.

## Author
Vidushi (vidushi-shay)
