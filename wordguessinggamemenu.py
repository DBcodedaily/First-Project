#python program to create a word guessing game

#import for different colored display words
import sys
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

#functin for rules
def Rules():
    print("")
    color.write("""GUESS IT! GAME RULES:
1. Game will give you a word with blank spaces.
2. Enter one letter at a time.
3. If you choose the wrong letter 3 times, game restarts.
""","BUILTIN")
  
#main menu display
def display():
    option = 0
    loop = True
    while loop:
        
        print("")
        print("""GUESS IT!
1. Rules
2. Play Against Computer
3. Play 2 Player Game
4. See High Score
5. Quit """)

        option = int(input("Choose an option 1 through 5: "))

        if option == 1:
            Rules()
            loop = True

    #elif option == 2:

    #elif option == 3:

    #elif option == 4:

    #elif option == 5:

        else:
            print("You didn't choose a valid option, try again!")
            loop = True
            
    return option

display()

    
