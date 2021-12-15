import requests
import random

def generateWord(): #generate a random word and return it
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    randomWord = random.choice(WORDS).decode('utf-8')
    return randomWord

def runGame(randomWord, word, blank):
    deathCheck = 0
    ranCheck = False
    while(deathCheck < 6):
        check = input("What is your letter?").lower()
        for j in range(len(randomWord)):
            if (check == word[j]):
                blank[j] = check
                ranCheck = True
        if(ranCheck == False):
            deathCheck = deathCheck + 1
        ranCheck = False
        print(*blank, sep=" ")    
        print("Death Check: " + str(deathCheck))