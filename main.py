## complex version of the hangman game
import sys
import random

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

minWordLength()
