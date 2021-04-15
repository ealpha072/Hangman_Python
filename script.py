userName = input("Enter your name: ")
print("Hello "+userName,"welcome to hangman")

gameWord = "edureka"

#holds the player's guess
playerGuesses = ''

#holds number of turns
turns = 10

while turns > 0:
    failed = 0
    for letter in gameWord:
        if letter in playerGuesses:
            print(letter)
        else:
            print('__')
            failed +=1
    if failed == 0:
        print("You have won")
        break
    
    playerGuess = input("Guess a character")
    playerGuesses+=playerGuess

    if playerGuess not in gameWord:
        turns-=1
        print("Wrong guess")

        print("You have "+turns, "more guesses to go")
    if turns == 0:
        print("You loose")