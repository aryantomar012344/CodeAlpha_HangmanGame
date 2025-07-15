import random

def hangman():
    # List of predefined words
    words = ["apple", "banana", "cherry", "grape", "orange"]
    word = random.choice(words)  # Randomly choose a word
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        # Show current progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
