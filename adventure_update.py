# -*- coding: utf-8 -*-
"""
Spyder Editor

Text based adventure game
"""
#import random module to randomise guessing room.
import random


# Start of adventure

#User chooses left or right.
def first_room():
    print("""Hi, whoever you may be...
youve got a chance to win gold!\n
Please choose room on the left or right""")
    a = input("Choose left of right:")
    if a == "left":
        left()
    elif a == "right":
        right()
    else:
        first_room()

#if user chooses left, they are brought to a number guessing game.
#They have three guesses and if their number doesn't pop up, they can play again.
#If not, it exits. 
def left():
    print("""\nYou have chosen the left room,
now you are on a number game for your chance at
the gold, you have three guesses to gain access to the
gold best of luck""")
    number = [1, 2, 3, 4, 5]
    your_pick = random.choice(number)
    guesses_left = 3
    while guesses_left > 0:
        guess = input("Choose a number between 1 and 5:\n")
        guess = int(guess)
        if guess == your_pick:
            print("You did it, you won the gold!!!!")
            break
        elif guess > your_pick:
            print("Your guess is too high")
            guesses_left -= 1
        elif guess < your_pick:
            print("Your guess is too low")
            guesses_left -= 1
    else:
        print("Your time is up! You didn't guess correctly!")
        restart = input("Would You like to go again? yes or no?")
        if restart == "yes":
            first_room()
        else:
            print("Goodbye!")

#If user chooses right room, they get to choose again as a trick guess. 
#To add a little complexity to the project in a sense. 
def right():
    print(""" AHA!! You thought you won the gold!
Think again, you do have another shot.""")
    choice = input("Choose Wisely! left or right? ")
    if choice == "left":
        print("You did it! You have won the Gold!")
    elif choice == "right":
        print("NOM NOM NOM. Game Over, You have been eaten by a big Tiger.")
        restart = input("Would You like to go again? yes or no?")
        if restart == "yes":
            first_room()
        else:
            print("Goodbye!")
    else:
        right()            

first_room()

