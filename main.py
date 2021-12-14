import requests
import random

# generate a random word and store it as randomWord
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
randomWord = random.choice(WORDS).decode('utf-8')

#store the word as an array 
word = list(randomWord)

#create an array of "_" with the same length as the word
blank = []
for i in range(len(word)):
    blank.append("_")

#ask the user for input 6 times. each time if their input is equal to a character in the random word replace the blank string with it  
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



print("\nENDING: ")
print(randomWord)
print(deathCheck)
print(blank)