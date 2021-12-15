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

#ask the user for input 6 times. each time if their input is equal to a character in the random word replace the blank string with it  
runGame(randomWord, word, blank)

print("\nENDING: ")
print(randomWord)
print(deathCheck)
print(blank)