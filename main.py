## complex version of the hangman game
import sys
import random
import string

gameWords = ['bulti',
 'Rauschenberg',
 'quizzing',
 'stairwell',
 'were-jaguar',
 'digressing',
 'multicore',
 'Posadas',
 'decolonises',
 'quibblingly',
 'Lubitsch',
 'decahydrate',
 'kimberlites',
 'disinhibitor',
 'Tsinan',
 'situates',
 'torcher',
 'forswearer',
 'Eyemouth',
 'biennale',
 'moralizes',
 'stitches',
 'chloranthus',
 'benzol',
 'delimbed',
 'vis-a-vis',
 'churners',
 'supplicates',
 'aminobenzoate',
 'hybridising',
 'dimple',
 'meat-eating',
 'conformists',
 'cartable',
 'misdeem',
 'impeditive',
 'subverting',
 'prefigurative',
 'artisanal',
 'gager',
 'extirp',
 'damasking',
 'altar-herse',
 'hobbleshow',
 'hatstand',
 'bacteriome',
 'long-horned',
 'checks',
 'sodicity',
 'horologue']

#function for asking user number of attempts

def userNumberOfAttempts():
    numAttempts = input("How many wrong attempts do you want to allow? [1-25]: ")
    numAttempts  = int(numAttempts)
    if numAttempts <= 0 or numAttempts > 25:
        print ("The number {0} is not a number between 1 and 25".format(numAttempts))
    else:
        return numAttempts

def minWordLength():
    wordLength = input("What min word length do you want ? [4-16]: ")
    wordLength = int(wordLength)
    if wordLength < 4 or wordLength >16:
        print("{0} is not a number between 4 and 16".format(wordLength))
        minWordLength()
    else:
        return wordLength

def getNextLetter(remaining_letters):
    #check below;
    #Next letter is not more than a single character
    #Next letter is a letter (no other character)
    #Next letter is not already guessed before
    return True
    

def playGame():
    name = input("What is your name ?:")
    print("Hello " + name, "welcome to the game!!")
    print("Starting the game....")

    #player settings 
    attempts = userNumberOfAttempts()
    wordLength = minWordLength()

    #Randomly selecting a word
    word = random.choice(gameWords)

    wrongLetters = []
    #main game loop
    while attempts > 0:
        #print game state
        print("Attempts remaining: {0}".format(attempts))
        print("Previous guesses: {0}".format(' '.join(wrongLetters)))



