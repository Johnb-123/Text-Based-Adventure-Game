# -*- coding: utf-8 -*-
"""
Spyder Editor

Text based adventure game
"""
import random

#WHY IS NONE POPPING UP?
#Start of adventure
def first_room():
    print("""Hi, whoever you may be...
youve got a chance to win gold!\n
Please choose room on the left or right""")
    a = input("Choose left of right:")
    if a == "left":
        print(left())
    elif a == "right":
        print(right())
    else:
        print("Make a decision if you want to win gold!")


def left():
    print("""\nYou have chosen the left room,
now you are on a number game for your chance at
the gold, you have three guesses to gain access to the 
gold best of luck""")
    number = random.randint(0, 5)
    guesses = 0
    gone_gold = 3
    while guesses != gone_gold:
    #for i in range(0, 5):
        guess = input("Choose a number between 0 and 5:\n")
        guess = int(guess)
        if guesses == gone_gold:
            print("You have lost!!! You are out of guesses.")
            break #put in an option to start all over again.
        elif guesses > number:
            print("Your guess is too high")
            guesses += 1            
        elif guesses < number:
            print("Your guess is too low")
            guesses += 1
        elif guesses == number:
            print("You did it, you won the gold!!!!")
            break         
        else:
            print("Why are you waiting to make a decision??")
        #Got to work on guessing countdown.
        #None keeps showing up and i don't know why.

def right():
    print(""" AHA!! You thought you won the gold! 
          Think again, you do have another shot.""")
    choice = input()
    #print(choice)
    if choice == "left":
        print("You did it! You have won the Gold!")
    elif choice == "right":
        print("NOM NOM NOM. Game Over, You have been eaten by a big Tiger.")
    else:
        print("You did not make a decision!")


print(first_room())




    