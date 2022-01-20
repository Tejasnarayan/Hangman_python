from function import get_random_word, displayBoard, getGuess, HANGMAN_display, playAgain
import random

guessedLetters = ''
correctLetters = ''
secretWord = get_random_word()
gameOver = False


while True:
    displayBoard(guessedLetters, correctLetters, secretWord)
    # Let the player enter a letter:
    guess = getGuess(guessedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check to see if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it RIGHT! YOU WIN')
            print('The word is "' + secretWord + '"!')
            gameOver = True
    else:
        guessedLetters = guessedLetters + guess

        # Check if the player has guessed too many times and lost.
        if len(guessedLetters) == len(HANGMAN_display) -1:
            displayBoard(guessedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(guessedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameOver = True
    # If the game is done, ask the player to try again.
    if gameOver:
        if playAgain():
            guessedLetters = ''
            correctLetters = ''
            gameOver = False
            secretWord = get_random_word()
        else:
            break
