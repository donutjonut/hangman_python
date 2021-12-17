from game import *
from men import *

def newWord():
    global randomWord
    randomWord = generateWord()
    #store the word as an array 
    global word
    word = list(randomWord)
    #create an array of "_" with the same length as the word
    global blank
    blank = []
    for i in range(len(word)):
        blank.append("_")
        
newWord()
welcomePlayer()
man1()
gameState = True
while gameState:
    runGame(randomWord, word, blank)
    clearScreen()
    stateChanger = input("Would you like to play again? ").lower()
    if (stateChanger == "yes"):
        newWord()
        clearScreen()
    elif(stateChanger == "no"):
        gameState = False

print("\nENDING: ")
print(randomWord)
print(blank)