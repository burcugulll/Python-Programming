import random

# List of words to choose from
words = ["python", "java", "ruby", "javascript", "csharp", "swift", "html", "css", "php"]

def choose_word():
    return random.choice(words)

def display_word(selected_word, guessed_letters):
    display = ""
    for letter in selected_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_game():
    selected_word = choose_word()
    max_wrong_guesses = round(len(selected_word) / 2)
    wrong_guesses_made = 0
    score = 0
    guessed_letters = []

    print("The word has", len(selected_word), "letters.")
    print(display_word(selected_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            print(display_word(selected_word, guessed_letters))
            print("Good guess!")

            if guess in "aeiou":
                score += 3 * selected_word.count(guess)
            else:
                score += 2 * selected_word.count(guess)
        else:
            wrong_guesses_made += 1
            if wrong_guesses_made >= max_wrong_guesses:
                print("\nYou lost!")
                print("The word was:", selected_word)
                break
            print("\nWrong guess! You have", max_wrong_guesses - wrong_guesses_made, "guesses left.")
            score -= 4

        if all(letter in guessed_letters for letter in selected_word):
            print("\nCongratulations, you guessed the word!")
            print("Score:", score)
            choice = input("Do you want to play again? (y/n) ").lower()
            if choice == "y":
                selected_word = choose_word()
                max_wrong_guesses = round(len(selected_word) / 2)
                wrong_guesses_made = 0
                guessed_letters = []
                score = 0
                print("\nThe word has", len(selected_word), "letters.")
                print(display_word(selected_word, guessed_letters))
            else:
                break

if __name__ == "__main__":
    play_game()
