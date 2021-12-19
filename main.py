from game import *
from men import *

def newWord():
    global randomWord
    randomWord = generateWord()
    global word
    word = list(randomWord)
    global blank
    blank = []
    for i in range(len(word)):
        blank.append("_")
        
newWord()
welcomePlayer()
makeMen(0)
gameState = True
while gameState:
    runGame(randomWord, word, blank)
    clearScreen()
    print("\033[1mGAME OVER!\033[0m")
    makeMen(7)
    stateChanger = input("Would you like to play again? ").lower()
    if (stateChanger == "yes"):
        newWord()
        man1()
        clearScreen()
        makeMen(0)
    elif(stateChanger == "no"):
        gameState = False

print("\nENDING: ")
print(randomWord)
print(blank)