import random


def print_scaffold(guesses, word):
    if (guesses == 0):
        print("_____________")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_____________")
    elif (guesses == 1):
        print("_____________")
        print("|      |")
        print("|      o")
        print("|")
        print("|")
        print("|")
        print("|_____________")
    if (guesses == 2):
        print("_____________")
        print("|      |")
        print("|      o")
        print("|      |")
        print("|      |")
        print("|")
        print("|____________")
    if (guesses == 3):
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|")
        print("|      |")
        print("|")
        print("|____________")
    if (guesses == 4):
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|\ ")
        print("|      |")
        print("|")
        print("|____________")
    if (guesses == 5):
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|\ ")
        print("|      |")
        print("|     / ")
        print("|____________")
    if (guesses == 6):
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|\ ")
        print("|      |")
        print("|     / \ ")
        print("|____________")
        print("\n")
        print("The word was " + word + ".")
        print("\n")
        print("YOU LOSE!")
        print("Do you want to play again?(Yes/No)")
        again = input(":").lower()
        if again == "yes":
            hangman()
        elif again == "no":
            quit()


def selectWord():
    file = open("WORDS.txt", "r")
    words = file.readlines()

    myword = 'a'
    while len(myword) < 3:
        myword = random.choice(words)
        myword = str(myword).strip('[]')
        myword = str(myword).strip("''")
        myword = str(myword).strip("\n")
        myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword