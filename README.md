Introduction

In this project, we will create a game where the user has to guess the names of different Indian states. For every correct guess, the user will be awarded a point. The game will continue until the user decides to quit.
Requirements

To run this project, you will need:

    Python 3.x installed on your computer

Project Structure

The project will consist of a single Python file:

    india_state_guessing_game.py: The Python file which will contain the game code

Steps

    Import the necessary libraries:

    arduino

import random
import pandas as pd

Load the CSV file containing the names of all the Indian states and their respective capitals into a pandas dataframe:

kotlin

data = pd.read_csv('states.csv')
