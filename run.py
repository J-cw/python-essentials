import random


def print_scaffold(guesses, word):
    if guesses == 0:
        print("_____________")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_____________")
    elif guesses == 1:
        print("_____________")
        print("|      |")
        print("|      o")
        print("|")
        print("|")
        print("|")
        print("|_____________")
    if guesses == 2:
        print("_____________")
        print("|      |")
        print("|      o")
        print("|      |")
        print("|      |")
        print("|")
        print("|____________")
    if guesses == 3:
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|")
        print("|      |")
        print("|")
        print("|____________")
    if guesses == 4:
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|\ ")
        print("|      |")
        print("|")
        print("|____________")
    if guesses == 5:
        print("_____________")
        print("|      |")
        print("|      o")
        print("|     /|\ ")
        print("|      |")
        print("|     / ")
        print("|____________")
    if guesses == 6:
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


def select_word():
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


def hangman():
    guesses = 0
    word = select_word()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Let's play hangman\n")
    print_scaffold(guesses, word)
    print("\n")
    print(" " + ' '.join(blanks_list))
    print("\n")
    print("Guess a letter.\n")

    while guesses < 6:
        guess = (input(">>> "))
        guess = guess.lower()

        if len(guess) > 1:
            print("Enter 1 letter at a time, please ")

        elif guess == "":
            print("What is your letter?")

        elif guess in guess_list:
            print("You have already guessed that one! Letter(s) used: ")
            print(''.join(guess_list))
            # show the player the letter that is already guessed

        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1
                print_scaffold(guesses, word)

                if guesses < 6:
                    print("Guess again.")
                    print('' .join(blanks_list))

            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print("".join(blanks_list))

                if word_list == blanks_list:
                    print("You Win! Congratulations!:")
                    print("\n")
                    print("Do you want to play again?(Yes/No")
                    again = input(":")
                    if again == "Yes" or again == "yes":
                        hangman()
                    quit()

                else:
                    print("Correct! Another?")


def main():

    hangman()


main()
