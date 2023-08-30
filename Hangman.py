import random

# Function to generate a random word from a list of words
def get_random_word():
    words = ["python", "java", "javascript", "c++", "ruby"]
    random_index = random.randint(0, len(words) - 1)
    return words[random_index]

# Function to draw the hangman
def draw_hangman(wrong_guesses):
    stages = [
        "    ",
        "   0  ",
        "  /|\ ",
        "  / \ ",
        "      ",
    ]
    return stages[wrong_guesses]

# Main function
def main():
    # Get the random word
    word = get_random_word()

    # Initialize the wrong guesses
    wrong_guesses = 0

    # Initialize the blank spaces for the word
    guessed_letters = []
    for i in range(len(word)):
        guessed_letters.append("_")

    # Play the game
    while wrong_guesses < 6:
        # Draw the hangman
        print(draw_hangman(wrong_guesses))

        # Get the user's guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is in the word
        if guess in word:
            # The letter is in the word
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_letters[i] = guess
        else:
            # The letter is not in the word
            wrong_guesses += 1

        # Check if the user has guessed the word
        is_word_guessed = True
        for i in range(len(word)):
            if guessed_letters[i] != word[i]:
                is_word_guessed = False
                break

        if is_word_guessed:
            print("Congratulations! You guessed the word!")
            break

    if not is_word_guessed:
        print("You lost! The word was: " + word)

if __name__ == "__main__":
    main()