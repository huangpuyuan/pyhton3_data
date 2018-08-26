# -*- coding: utf-8 -*-
"""
Spyder Editor

Author kaitai--HPY

Plays a game of guess the number with the user
"""

import random

def main():
    '''Input the bounds of the range of numberss and lets the user guess the compouter's 
    number until the guess is correct. '''
    smaller = int(input("Enter the smaller number: "))
    larger =  int(input("Enter the larger number: "))
    myNumber = random.randint(smaller,larger)
    count = 0
    while True:
        count +=1
        userNumber = int(input("Enter your guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too larger")
        else:
            print("You've got it in", count,"tries!")
            break
        
if __name__ == "__main__":
    main()
    
    