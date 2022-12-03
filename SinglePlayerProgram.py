#program to play word guessing game single player

#import random to allow program to randomly select a word in a list
import random

#function for solo players
def OnePlayer():

    name = input("What is your name? ")

    theme = input("""What theme of words would you like to play?
A. Cpmputers
B. """ )

    print("Goodluck, " + name "!")

    computerWords = ["Keyboard", "Laptop", "Mouse", "Monitor", "Disk", "Program"

    
