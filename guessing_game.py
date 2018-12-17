"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

I AM AIMING FOR THE EXCEEDS EXPECTATIONS LEVEL
       Thank you! =]
                     -Ben

"""

import random


def start_game():
    
    print("  Hello, and welcome to the Number Guessing Game!")
    print("___________________________________________________")
    
    new_game = ''
    guess = ''
    highscore = 11
    while new_game.lower() != 'n':
        number = random.randint(1,10)
        if highscore < 11:
            print("\nHIGHSCORE: {} Guesses".format(highscore))
        num_guesses = 0
        while guess != number:
            
            try:                                                   #catch invalid entry errors
                guess = int(input("\nWhat is your guess?   "   ))
                if guess > 10 or guess < 1:
                    raise ValueError("ValueError; Number out of range of game")
            except ValueError as err:
                print("""
                    INVALID ENTRY:
                    Please enter an integer value between 1-10...
                    """)
                print(err)
                continue
                
            num_guesses += 1                                       #if entry is valid, continue on to the rest of the sequence
            if guess > number:
                print("It's LOWER, try again!")
                continue
            elif guess < number:
                print("its HIGHER, try again!")
                continue
            elif guess == number:
                if num_guesses < highscore:
                    print(
                   """
                     Got it!
                      ~~NEW HIGHSCORE~~
                        It took you {} attempts""".format(num_guesses))
                    highscore = num_guesses
                elif num_guesses >= highscore:
                    print(
                   """
                     Got it!
                        It took you {} attempts""".format(num_guesses))
        while True:                                                            #here we are catching wrong inputs for new game decision
            try:
                new_game = input("  GAME OVER  \n     Would you like to play again?  [Y]es/[N]o:  ")
                if new_game.lower() == "n":
                    break
                if new_game.lower() == "y":
                    break
                raise ValueError("\nINVALID ENTRY: please select: [Y]es/[N]o \n")
                
            except ValueError as e:
                print(e)
                
    print(" \n Goodbye! \n")
              
if __name__ == '__main__':
    start_game()
