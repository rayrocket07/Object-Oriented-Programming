def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    extra = 0
    totalP = 0
    scrabble_letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
        'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
        'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
        'y': 4, 'z': 10
    }

    for i in word:
        totalP += scrabble_letter_values[i]
    totalP *= len(word)
    if len(word) == n:
        extra = 50
    return(totalP + extra)
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hi = {}
    for key,value in hand.items():
        hi[key] = value
    for i in word:
        hi[i] -= 1
    return(hi)
    
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handword = ""
    for key,value in hand.items():
        handword += key*int(value)
    lst = []
    for i in handword:
        lst.append(i)
    for i in word:
        if i in lst:
            lst.remove(i)
        else:
            return False
    return(word in wordList)
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    total = 0
    for i in hand.values():
        total += i
    return total

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    def displayH(hand):
        handword = ""
        for key,value in hand.items():
            handword += key*int(value)
        return(handword)
    number = 0
    for i in range(n):
        number += 1
    score = 0
    
    while True:
        print("Current Hand: " + str(displayH(hand)))
        gword = input('Enter word, or a "." to indicate that you are finished: ')
        if gword == ".":
            return("Goodbye! Total score: " + str(score) + " points.") 
        else:
             if not isValidWord(gword, hand, wordList):
                 print("Invalid word, please try again.")
                 continue
             else:
                 score += getWordScore(gword, n)
                 print('"' + str(gword) + '" earned ' + str(getWordScore(gword, n)) + " points. Total: " + str(score) + " points")
                 number -= len(gword)
             if number == 0:
                 return("Run out of letters. Total score: " + str(score) + " points.")
        

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    
    played = False
    while True:
        gameplay = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if gameplay != "n" and gameplay != "r" and gameplay != "e":
            print("Invalid command.")
            continue
        if gameplay == "e":
            break
        elif not played and gameplay == "r":
            print("You have not played a hand yet. Please play a new hand first!")
            continue
        gamemode = input("Enter u to have yourself play, c to have the computer play: ")
        while gamemode != "u" and gamemode != "c":
            print("Invalid command.")
            gamemode = input("Enter u to have yourself play, c to have the computer play: ")
        if gamemode == "u":
            if gameplay == "n":
                newhand = dealHand(HAND_SIZE)
                playHand(newhand,'<edX internal wordList>', HAND_SIZE)
                played = True
            elif gameplay == "r":
                playHand(newhand,'<edX internal wordList>', HAND_SIZE)
         
        else:
            if gameplay == "n":
                newhand = dealHand(HAND_SIZE)
                compPlayHand(newhand,'<edX internal wordList>', HAND_SIZE)
                played = True
            elif gameplay == "r":
                compPlayHand(newhand,'<edX internal wordList>', HAND_SIZE)
               
                   
           