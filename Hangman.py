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
             

