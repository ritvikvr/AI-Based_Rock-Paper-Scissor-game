# AI-Based Rock-Paper-Scissors Game

A Python implementation of the classic Rock-Paper-Scissors game with AI opponent. Play against the computer and track your score as you compete in multiple rounds.

## Features

- **Interactive Gameplay**: Play against an AI opponent in a command-line interface
- **Random AI Moves**: Computer makes random selections for unpredictable gameplay
- **Score Tracking**: Keep track of wins and losses throughout the game session
- **Input Validation**: Handles invalid user inputs gracefully
- **Easy Exit**: Type 'exit' at any time to quit and see final score
- **Real-time Feedback**: Immediate feedback on each round's outcome

## Game Rules

The standard Rock-Paper-Scissors rules apply:
- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- If both players choose the same option, it's a **tie**

## Installation

No external dependencies required! This game uses only Python's built-in `random` module.

### Prerequisites
- Python 3.x

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ritvikvr/AI-Based_Rock-Paper-Scissor-game.git
cd AI-Based_Rock-Paper-Scissor-game
```

2. Run the game:
```bash
python AI-Based_Rock,paper,scissors.py
```

## Usage

1. When prompted, enter your choice: `rock`, `paper`, or `scissors`
2. The computer will make its random selection
3. The game announces the winner or tie
4. Your cumulative score is displayed
5. Repeat for as many rounds as you want
6. Type `exit` to quit and see your final score

### Example Gameplay

```
Welcome to AI Rock, Paper, Scissors Game!
Type 'exit' to stop playing.

Enter rock, paper, or scissors: rock
Computer chose: scissors
You win!
Score -> You: 1 | Computer: 0

Enter rock, paper, or scissors: paper
Computer chose: paper
It's a tie!
Score -> You: 1 | Computer: 0

Enter rock, paper, or scissors: exit
Final Score:
You: 1 | Computer: 0
```

## How It Works

The game uses Python's `random.choice()` function to select from a list of three choices: `['rock', 'paper', 'scissors']`. Each round:

1. Accepts user input (case-insensitive)
2. Validates the input against available choices
3. Generates a random computer move
4. Compares both moves using conditional logic
5. Updates the score based on win/tie/loss
6. Displays the result and current score

## Code Structure

- **Imports**: Uses Python's `random` module
- **Variables**: Tracks user and computer scores
- **Game Loop**: Continuous `while True` loop for multiple rounds
- **Validation**: Checks user input validity
- **Winning Logic**: Comprehensive conditional statements to determine outcomes

## Future Enhancements

Potential improvements for this project:
- [ ] Add difficulty levels (easy, medium, hard)
- [ ] Implement a simple AI strategy instead of pure random
- [ ] Add a graphical user interface (GUI)
- [ ] Support for multiplayer mode
- [ ] Game statistics and history tracking
- [ ] Customizable win conditions
- [ ] Sound effects and animations

## Technologies Used

- **Language**: Python 3
- **Modules**: `random`

## Author

**Ritvík** (ritvikvr)

## License

This project is open source and available for personal and educational use.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for any improvements.

## Feedback

If you have suggestions or find any issues, please open an issue on GitHub.

---

**Enjoy the game and may the best player win! 🎮**
