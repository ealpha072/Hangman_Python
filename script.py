import sys
import random
      
def playGame():
    playerName = input("Enter your name: ")
    print("Hello "+playerName,"welcome to hangman and good luck")

    gameWords = ['computer','interesting','guess','introduction','popular','lion','history',
                'ponder','debate','issues']

    word = random.choice(gameWords)

    #holds player guess as a string, this is compared to the word
    playerGuesses=''

    attempts = 10
    while attempts > 0:
        failed = 0
        for letter in word:
            if letter in playerGuesses:
                print(letter)
            else:
                print("__")
                failed +=1

        if failed == 0:
            print ("You win")
            print("The word is: ",word)
            choice = input("Play again ? y/n: ")

            #code for checking game continuity

            if 'y' in choice:
                playGame()
            elif 'n' in choice:
                sys.exit()
            else:
                print("Something went wrong type y or n")

        playerGuess = input("guess a character: ")
        playerGuesses+=playerGuess

        if playerGuess == 'exit':
            break

        if playerGuess not in word:
            attempts-=1
            print("Wrong guess")
            print("You have ",attempts,"more gueses")

            if attempts == 0:
                print("You loose")
                choice = input("Play again ? y/n: ")

                #code for checking game continuity
                if 'y' in choice:
                    playGame()
                elif 'n' in choice:
                    sys.exit()
                else:
                    print("Something went wrong type y or n")

playGame()


