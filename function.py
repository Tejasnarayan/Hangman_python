import requests

HANGMAN_display = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
def get_random_word():
    URL = "https://random-word-api.herokuapp.com/word"
    word = requests.get(URL).json()[0]

    if not word.isalpha():
        word = get_random_word()

    return word

def displayBoard(guessedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_display[len(guessedLetters)])

    print()
    print('Guessed letters: ', end=' ')
    for letter in guessedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end =' ')
    print()

def getGuess(alreadyGuessed):
    
    #Returns the letter the player entered.
    #Ensures the player enters a single letter and nothing else.

    while True:
        print('Please guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a letter from the alphabet.')
        else:
            return guess

def playAgain():
  
    #Returns True if the player wants to play again, False otherwise.

    print('Would you like to play again? Yes(y) or No(n)')
    return input().lower().startswith('y')
