words=("Brazil","Russia","India","China","South Africa","Albania", "Belgium", "Bulgaria", "Canada", "Croatia", "Czech Republic", "Denmark", "Estonia", "France",
       "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
       "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Turkey", "United Kingdom", "United States")
        #BRICS                                          #NATO
from random import choice

inp=input("Press Enter to Start...")
if inp=="":
    while True:
        #pick a random word at start of game
        word=choice(words).lower()

        fails=7
        char_guess=''
        print("Guess Country Names..\n\nTotal Fails Allowed: ",fails)

        while fails>0:
            #display unveiled word
            for char in word:
                if char in char_guess:
                    print(char,end=" ")
                elif char==' ':
                    print(' ',end=" ")
                else:
                    print('_',end=" ")
            print()

            #Ask player to guess a character
            letter=input("Guess:: ").lower()
            char_guess+=letter
            if letter in word:
                print("Correct Guess..\n")
            else:
                fails-=1
                print("Wrong Input..\n\nChances left ",fails)

            #Exit Condition
            if all((char in char_guess or char==' ') for char in word):
                print('--',word.upper(),"--\n\n** You Won **")
                break

        if fails==0:
            print("You Lose\nThe Word was--",word.upper())
            
        if input("\nPlay Again?\n")=="No":
            break;
        print()
