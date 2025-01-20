# Rock-Paper-Scissors Game

A simple Rock-Paper-Scissors game built using Python and Tkinter. Play against the computer and keep track of your score.

## Features
- Choose between Rock, Paper, and Scissors to play against the computer.
- Display the choices made by both the player and the computer.
- Track the scores for both the player and the computer.
- Reset the game to start a new round.
- Exit the game at any time.

## Requirements
- Python 3.x
- Tkinter (usually bundled with Python installations)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.
3. Tkinter should come pre-installed with Python. If not, install it using your package manager.

## Usage

1. Run the Python script to start the game.
2. The game window will appear with buttons to select **Rock**, **Paper**, or **Scissors**.
3. The computer will randomly choose one of these options, and the result (win, lose, or tie) will be displayed.
4. Your score and the computer’s score will be updated after each round.
5. Press **Reset Game** to start a new game or **Exit** to close the application.

### Example

- **You choose:** Rock
- **Computer chooses:** Scissors
- **Result:** You win this round!
- **Your Score:** 1, **Computer Score:** 0

## How It Works

1. The player clicks one of the buttons to select Rock, Paper, or Scissors.
2. The computer randomly selects one of the choices.
3. The winner is determined based on the standard rules:
   - Rock beats Scissors.
   - Scissors beats Paper.
   - Paper beats Rock.
4. The scores for both the player and the computer are updated accordingly.
5. The player can reset the game anytime or quit the game by clicking the appropriate buttons.

## Code Overview

### `determine_winner()` function:
- Compares the user's choice with the computer’s choice and returns the winner: "user", "computer", or "tie".

### `play()` function:
- Handles the game logic, including selecting the computer's choice and updating the scores and result labels.

### `reset_game()` function:
- Resets the game scores and labels to start a new game.

### Tkinter UI:
- The user interface is built using Tkinter widgets such as `Button`, `Label`, and `Frame`.
- Players can choose their move, see the results, and keep track of scores.

## License
This project is open-source and available under the MIT License.
