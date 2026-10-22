# Datheon_Python_Internship
Python tasks complete as the part of Datheon Internship. 

**Author**: Hassan Ilyas


| Task | Project | Difficulty | Status |
|------|---------|------------|--------|
| 1 | Hangman Word Guessing Game (Console) | Beginner | Completed |

# Task 1: Hangman Word Guessing Game

A terminal-based Hangman game written in Python 3. The player guesses a hidden word letter by letter, with a maximum of 6 incorrect attempts.

 Features
- Random word selection using `random.choice()`
- Masked word display (e.g. `_ A _ H E O N`)
- ASCII gallows art that updates after each wrong guess
- Tracks guessed letters using a set
- Repeated guesses do not cost an attempt
- Input validation (single letters only)
- Victory and defeat screens
- Play again option

# Requirements
- Python 3
- No external packages (uses only the standard library: `random`, `os`)

# Installation and Usage
1. Clone the repository:
   ```
   git clone https://github.com/Hassan-ilyas-web/Datheon_Python_Internship.git
   ```
2. Open the folder:
   ```
   cd Datheon_Python_Internship
   ```
3. Run the game:
   ```
   python hangman.py
   ```

Optional: place an English word list named `words.txt` in the same folder. If it is not found, the game uses a built-in word list.

# Code Structure
| Function | Purpose |
|----------|---------|
| `load_words()` | Loads words from `words.txt` or the default list |
| `display_word()` | Builds the masked word string |
| `get_guess()` | Validates input and rejects repeated letters |
| `show_status()` | Prints gallows art, word, guessed letters and mistakes |
| `play_round()` | Main game loop |
| `victory_screen()` / `defeat_screen()` | End-of-game screens |
| `main()` | Starts the game and handles replay |
