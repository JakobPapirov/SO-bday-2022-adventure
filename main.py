# -*- coding: utf-8 -*-
import random as rand # Standard library
import time # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji

from mainMenu import runMainMenu

def runGame(name):
  # Use a breakpoint in the code line below to debug your script.
  print("")
  print(f"Välkommen, {chalk.blue(name)}, strax börjar det roliga" + emoji.emojize(":red_exclamation_mark:")) # Press Ctrl+F8 to toggle the breakpoint.
  time.sleep(1)
  runMainMenu(name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  runGame('Sandra')