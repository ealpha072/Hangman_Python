playerName = input("Enter your name: ")
print("Hello "+playerName,"welcome to hangman and good luch")

word = "boy"
#playerGuess = input("Guess any alphabet: ")
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
        break
    
    playerGuess = input("guess a character: ")
    playerGuesses+=playerGuess

    if playerGuess== 'q':
        break
    if playerGuess not in word:
        attempts-=1
        print("Wrong guess")
        print("You have ",attempts,"more gueses")

        if attempts == 0:
            print("You loose")
        



