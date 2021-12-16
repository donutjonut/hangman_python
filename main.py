import requests
import random
import os
from game import *

randomWord = generateWord()
#store the word as an array 
word = list(randomWord)
#create an array of "_" with the same length as the word
blank = []
for i in range(len(word)):
    blank.append("_")

welcomePlayer()

gameState = True
while gameState:
    runGame(randomWord, word, blank)

    clearScreen()
    stateChanger = input("Would you like to play again? ").lower()
    if (stateChanger == "yes"):
        gameState = True
        randomWord = generateWord()
        word = list(randomWord)
        blank = []
        for i in range(len(word)):
            blank.append("_")
        clearScreen()
    elif(stateChanger == "no"):
        gameState = False

print("\nENDING: ")
print(randomWord)
print(blank)