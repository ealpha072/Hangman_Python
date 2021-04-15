## complex version of the hangman game
import sys
import random

gameWords = ['computer','interesting','guess','introduction','popular','lion','history',
                'ponder','debate','issues']

#function for asking user number of attempts

def userNumberOfAttempts():
    numAttempts = input("How many wrong attempts do you want to allow? [1-25]: ")
    numAttempts  = int(numAttempts)
    if numAttempts == 0 or numAttempts > 25:
        print ("The number {0} is not a number between 1 and 25".format(numAttempts))
    else:
        return numAttempts

userNumberOfAttempts()
