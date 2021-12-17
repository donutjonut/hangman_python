import requests
import random
import os

def clearScreen(): #literal among us god
    os.system('cls' if os.name == 'nt' else 'clear')

def generateWord(): #generate a random word and return it
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    randomWord = random.choice(WORDS).decode('utf-8')
    return randomWord

def checkDone(randomWord, blank):
    count = 0
    for i in range(len(randomWord)):
        if (blank[i] == "_"):
            count += 1
    return count

def runGame(randomWord, word, blank): #ask the user for input 6 times. each time if their input is equal to a character in the random word replace the blank string with it  
    deathCheck = 0
    ranCheck = False
    print(*blank, sep=" ") 
    while(deathCheck < 6):
        check = input("What is your letter? ").lower()
        clearScreen()
        print("Entered Letter: " + check) #monkeeyyyyyy as LMAO
        for j in range(len(randomWord)):
            if (check == word[j]):
                blank[j] = check
                ranCheck = True
        if(ranCheck == False):
            deathCheck = deathCheck + 1
        ranCheck = False
        print(*blank, sep=" ")    
        print("Death Check: " + str(deathCheck))

def welcomePlayer():
    clearScreen()
    print("Welcome to Hangman!")
    gameStart = input("Press enter to start a game or type exit to quit ").lower()
    if gameStart == "exit" or gameStart == "q" or gameStart == "quit":
        exit()
    else:
        clearScreen()