def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    correct = 0
    lenght = len(secretWord)
    for i in secretWord:
        if i in lettersGuessed:
            correct += 1
    return correct == lenght

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    space = []
    for i in secretWord:
        space += "_ "
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            space[i*2] = secretWord[i]
    strspace = ""
    for i in space:
        strspace += i
    return strspace
             
def getAvailableLetters(lettersGuessed):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    for i in letters:
        lst.append(i)
    for i in lettersGuessed:
        lst.remove(i)
    lettersleft = ""
    for i in lst:
        lettersleft += i
    return(lettersleft)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def lst_to_str(lst):
        x = ""
        for i in lst:
            x += i
        return x
    guesses = 8
    rayquaza = []
    print("""Welcome to the game, Hangman!
I am thinking of a word that is """ +  str(len(secretWord)) + " letters long.")
    while True:
        print("------------")
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break
        elif "_" not in getGuessedWord(secretWord, rayquaza):
            print("Congratulations, you won!")
            break
            
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(rayquaza))
        guessedletter = input("Please guess a letter: ")
        
        if guessedletter in rayquaza:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, rayquaza))
        elif guessedletter in secretWord:
            rayquaza.append(guessedletter)
            print("Good guess: " + getGuessedWord(secretWord, rayquaza))
        else:
            rayquaza.append(guessedletter)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, rayquaza))
            guesses -= 1

