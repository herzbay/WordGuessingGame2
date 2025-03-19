import random
import time

def play_game():
    # Header Game
    print("===============================")
    print("      WORD GUESSING GAME 2     ")
    print("    ( Progamming Language )     ")
    print("===============================")

    # Use system time as seed to ensure random results differ each run
    random.seed(time.time())

    word_bank = ['python', 'java', 'ruby', 'dart', 'kotlin']
    word = random.choice(word_bank)  # Randomly select a word from word_bank
    guessedWord = ['_'] * len(word)

    attempts = 10
    guessed_letters = set()  # To store guessed letters
    score = 100  # Initial score

    start_time = time.time()  # Start time for timeout check

    while attempts > 0:
        # Check for timeout (e.g., 60 seconds)
        if time.time() - start_time > 60:
            print("\nTime's up! Game over!")
            print('Your final score:', score)
            break

        print('\nCurrent word: ' + ' '.join(guessedWord))
        print('Attempts left:', attempts)
        print('Guessed letters:', ', '.join(sorted(guessed_letters)))

        guess = input('Guess a letter: ').lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single valid letter.')
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print('You already guessed that letter. Try a different one.')
            continue

        # Add the guessed letter to the set
        guessed_letters.add(guess)

        # Decrease attempts, regardless of correct or incorrect guess
        attempts -= 1

        # Check if the letter is in the word
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print('Great guess!')
        else:
            score -= 10  # Deduct score only if the guess is wrong
            print('Wrong guess!')

        # Check if the word has been fully guessed
        if '_' not in guessedWord:
            print('\nCongratulations!! You guessed the word: ' + word)
            print('Your final score:', score)
            break

    # If attempts run out
    if attempts == 0:
        print('\nGame over! The word was: ' + word)
        print('Your final score:', score)

# Main loop to rerun the game
while True:
    play_game()  

    # Ask if the user wants to repeat the game
    replay = input('\nDo you want to play again? (yes/no): ').lower()
    if replay != 'yes':
        print('Thank you for playing! Goodbye!')
        break  
