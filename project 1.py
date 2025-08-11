import random

def hangman():
    word_list = ["apple", "zebra", "train", "house", "robot"]
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6
    display_word = ["_" for _ in word]

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print(f"You have {tries} chances. Let's begin!")
    print(" ".join(display_word))

    while tries > 0 and "_" in display_word:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
            print("Nice! That one's correct.")
        else:
            tries -= 1
            print(f"Oops! That letter isn't in the word. {tries} tries left.")

        print("\nCurrent word:", " ".join(display_word))
        print("Letters guessed so far:", ", ".join(guessed_letters))

    if "_" not in display_word:
        print(f"\nWell done! You guessed the word: '{word}'.")
    else:
        print(f"\nYou're out of tries. The word was: '{word}'. Better luck next time!")

hangman()
