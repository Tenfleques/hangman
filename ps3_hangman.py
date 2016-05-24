# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/tenda/learn python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if len(secretWord)==0:
        return True
    else:
        if secretWord[-1] in lettersGuessed:
            return isWordGuessed(secretWord[:-1], lettersGuessed)
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = []
    for i in secretWord:
        result.append("_")
    ind = 0
    for lt in secretWord:
        if lt in lettersGuessed:
            result[ind] = lt
        ind +=1
    return " ".join(result)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    result = list(string.ascii_lowercase)
    for i in lettersGuessed:
        result.remove(i)
    return "".join(result)

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
    # FILL IN YOUR CODE HERE...
    import string
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print ('------------')
    
    lettersGuessed=list()
    numguesses = 8
    while numguesses:
        print("You have "+str(numguesses)+" guesses left.")
        print("Available letters: "+getAvailableLetters(lettersGuessed))
        guess = raw_input("Please guess a letter: ").lower()
        if guess in  lettersGuessed:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
        elif guess in string.ascii_lowercase and guess not in secretWord:
            print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
            numguesses-=1
            lettersGuessed.append(guess)
        elif guess in string.ascii_lowercase:
            lettersGuessed.append(guess)
            print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
                print("Congratulations, you won!")
                break
        print ('------------') 
    if not isWordGuessed(secretWord, lettersGuessed):
        print("Sorry, you ran out of guesses. The word was " + secretWord)
    return None 
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
