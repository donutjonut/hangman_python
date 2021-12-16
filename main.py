import requests
import random
from game import *

randomWord = generateWord()
#store the word as an array 
word = list(randomWord)
#create an array of "_" with the same length as the word
blank = []
for i in range(len(word)):
    blank.append("_")

gameState = True
while gameState:
    runGame(randomWord, word, blank)
    stateChanger = input("Would you like to play again?").lower()
    if (stateChanger == "yes"):
        gameState = True
    elif(stateChanger == "no"):
        gameState = False


print("\nENDING: ")
print(randomWord)
print(deathCheck)
print(blank)