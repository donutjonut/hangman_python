def man1(): #dababy
    amongUs1 = [' ', 'O', ' ']
    amongUs2 = ['\\', '|', '/']
    amongUs3 = ['/', ' ', '\\']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")

def man2(): #dababy1
    amongUs1 = [' ', 'O', ' ']
    amongUs2 = ['\\', '|', '/']
    amongUs3 = [' ', ' ', '\\']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")

def man3(): #dababy2
    amongUs1 = [' ', 'O', ' ']
    amongUs2 = ['\\', '|', '/']
    amongUs3 = [' ', ' ', ' ']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")

def man4(): #dababy3
    amongUs1 = [' ', 'O', ' ']
    amongUs2 = [' ', '|', '/']
    amongUs3 = [' ', ' ', ' ']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")

def man5(): #dababy4
    amongUs1 = [' ', 'O', ' ']
    amongUs2 = [' ', '|', ' ']
    amongUs3 = [' ', ' ', ' ']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")

def man6(): #dababy5
    amongUs1 = [' ', 'O', ' ']
    amongUs2 = [' ', ' ', ' ']
    amongUs3 = [' ', ' ', ' ']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")

def man7(): #dababy6
    amongUs1 = ['\\', ' ', '/']
    amongUs2 = [' ', 'X', ' ']
    amongUs3 = ['/', ' ', '\\']
    print(*amongUs1, sep="")
    print(*amongUs2, sep="")
    print(*amongUs3, sep="")


def makeMen(deaths): #monkey ass lmao
    if deaths == 0:
        man1()
    elif deaths == 1:
        man2()
    elif deaths == 2:
        man2()
    elif deaths == 3:
        man3()
    elif deaths == 4:
        man4()
    elif deaths == 5:
        man5()
    elif deaths == 6:
        man6()
    elif deaths == 7:
        man7()
    else: 
        man1()

