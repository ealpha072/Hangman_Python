## complex version of the hangman game
import sys
import random
from string import ascii_lowercase

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

def getWord(arr):
    reqLen = input("Choose word length: ")
    reqLen = int(reqLen)
    myArr = []
    #myWord=''
    for word in arr:
        if(len(word) > reqLen):
            myArr.append(word)
            print(random.choice(myArr))

getWord(gameWords)




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
    #remaining_letters = set(ascii_lowercase)
    if(len(remaining_letters)==0):
        raise ValueError("There are no remaining letters")  

    nextLetter = input("Guess a character: ".lower())
    if(len(nextLetter)!= 1):
        print("{0}, is not a single character".format(nextLetter))
        getNextLetter(remaining_letters)
    elif(nextLetter not in ascii_lowercase):
        print("{0}, is not a letter".format(nextLetter))
        getNextLetter(remaining_letters)
    elif(nextLetter not in remaining_letters):
        print("{0}, has been guessed before")
        getNextLetter(remaining_letters)
    else:
        remaining_letters.remove(nextLetter)
        return nextLetter


    

def playGame():
    name = input("What is your name ?:")
    print("Hello " + name, "welcome to the game!!")
    print("Starting the game....")

    #player settings 
    attempts = userNumberOfAttempts()
    wordLength = minWordLength()

    #Randomly selecting a word
    word = random.choice(gameWords)

    #game variables 
    remaining_letters = set(ascii_lowercase)

    wrongLetters = []
    wordSolved = False
    #main game loop
    while attempts > 0:
        #print game state
        print("Attempts remaining: {0}".format(attempts))
        print("Previous guesses: {0}".format(' '.join(wrongLetters)))

        #getting next letter guess
        nextLetter = getNextLetter(remaining_letters)

        #check if letter guessed is in the word
        if nextLetter in word:
            #correctly guessed
            print("Letter {0} is in the word".format(nextLetter))
        
        else:
            print("Letter {0} is not in the word".format(nextLetter))
            attempts -=1
            wrongLetters.append(nextLetter)



