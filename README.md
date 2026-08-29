# Hanoi Towers Game

## Description
A python implementation of the classic Tower of Hanoi puzzle, developed in two milestones.
- Milestone 1 is a console-based version of the game.
- Milestone 2 is a graphical user interface (GUI) version created using the graphics library. 

## How it works
- The user chooses the number of towers and disks for the game.
- The first tower starts with all disks arranged from largest to smallest.
- The user moves disks between towers following the Tower of Hanoi rules.
- The program checks whether each move is valid.
- The game tracks the number of moves needed to complete the puzzle.

## Game rules
A disk can be moved:
- One disk at a time
- Only from the top of a tower
- A larger disk cannot be placed on top of a smaller disk

## How to run
1. Make sure Python is installed.
2. Run the program using Python.
3. Choose:
   - `1` to start a new game
   - `2` to resume a saved game
4. Follow the instructions displayed in the console.

## Files
- `hanoi_towers_milestone_1.py` - Main program containing the game logic and user interaction.
- `stack.py` - Stack implementation used to manage the towers.

## Output
The program displays:
- The current tower arrangement
- Valid and invalid move messages
- The number of moves taken to complete the puzzle
- Save/load game messages

## Author
Vidushi (vidushi-shay)
