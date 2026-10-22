import os
import random

MAX_MISTAKES = 6

# ASCII gallows art: index = number of wrong guesses (0 to 6)
STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

DEFAULT_WORDS = [
    "python", "variable", "function", "analytics", "dataset",
    "spreadsheet", "database", "algorithm", "keyboard", "network",
    "programming", "multan", "university", "statistics", "notebook",
]


def load_words(filename="words.txt"):
    """Words list file se load karo; agar file na mile to default list use karo."""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            words = [w.strip().lower() for w in f
                     if w.strip().isalpha() and len(w.strip()) >= 4]
        if words:
            return words
    return DEFAULT_WORDS


def display_word(secret, guessed):
    """Masked string banao, jaise: _ A _ H E O N"""
    return " ".join(ch.upper() if ch in guessed else "_" for ch in secret)


def get_guess(guessed):
    """User se valid, naya letter lo. Duplicate par penalty nahi lagti."""
    while True:
        guess = input("\nEk letter guess karo: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Sirf ek letter (A-Z) likho.")
        elif guess in guessed:
            print(f"Tum '{guess.upper()}' pehle guess kar chuke ho. Koi penalty nahi, dobara try karo.")
        else:
            return guess


def show_status(secret, guessed, mistakes):
    print(STAGES[mistakes])
    print("\nWord:", display_word(secret, guessed))
    print("Guessed letters:", " ".join(sorted(l.upper() for l in guessed)) or "-")
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")


def victory_screen(secret):
    print("\n" + "*" * 32)
    print("   MUBARAK! TUM JEET GAYE!")
    print(f"   Word tha: {secret.upper()}")
    print("*" * 32)


def defeat_screen(secret):
    print(STAGES[MAX_MISTAKES])
    print("\n" + "x" * 32)
    print("   GAME OVER! TUM HAAR GAYE.")
    print(f"   Sahi word tha: {secret.upper()}")
    print("x" * 32)


def play_round(words):
    secret = random.choice(words)
    guessed = set()
    mistakes = 0

    print("\n=== HANGMAN ===")
    print(f"Word mein {len(secret)} letters hain.")

    while mistakes < MAX_MISTAKES:
        show_status(secret, guessed, mistakes)

        if all(ch in guessed for ch in secret):
            victory_screen(secret)
            return

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in secret:
            print(f"Sahi! '{guess.upper()}' word mein hai.")
        else:
            mistakes += 1
            print(f"Galat! '{guess.upper()}' word mein nahi hai.")

        # Last guess ke baad win check
        if all(ch in guessed for ch in secret):
            show_status(secret, guessed, mistakes)
            victory_screen(secret)
            return

    defeat_screen(secret)


def main():
    words = load_words()
    while True:
        play_round(words)
        again = input("\nDobara khelna hai? (y/n): ").strip().lower()
        if again != "y":
            print("Khuda hafiz!")
            break


if __name__ == "__main__":
    main()

