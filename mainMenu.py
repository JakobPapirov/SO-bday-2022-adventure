# -*- coding: utf-8 -*-
import random as rand # Standard library
import time # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji

def runMainMenu(name):
  menuState = True

  while menuState:
    print("")
    print("--------------------")
    print("1. Val.")
    print("2. Val.")
    print("3. Val.")
    print("")
    print("0. Press 0 to exit the game")
    print("--------------------")
    userChoice = input("What do you want to do ? ")
    print("")
    if userChoice == '':
      print("You didn't make a choice, please try again")
    else:
      userChoice = int(userChoice)

    if userChoice == 1:
      print(f"Val = {userChoice}")
    elif userChoice == 2:
      print(f"Val = {userChoice}")
    elif userChoice == 3:
      print(f"Val = {userChoice}")
    elif userChoice == 0:
      print("Ha en fortsatt toppen födelsedag!")
      time.sleep(1)
      menuState = False