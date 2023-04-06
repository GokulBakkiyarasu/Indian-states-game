Introduction

In this project, we will create a game where the user has to guess the names of different Indian states. For every correct guess, the user will be awarded a point. The game will continue until the user decides to quit.

![Screenshot (9)](https://user-images.githubusercontent.com/87391223/230473071-2d14fc73-22f1-4253-9fef-80eeb814c621.png)


Requirements

To run this project, you will need:

    Python 3.x installed on your computer

Project Structure

The project will consist of a single Python file:

    main.py: The Python file which will contain the game code
    scoreboard.py: The Python class file which will contain the behaviour of a scoreboard

Steps

    Import the necessary libraries:

    import turtle
    import pandas 

Load the CSV file containing the names of all the Indian states and their respective capitals into a pandas dataframe:

    data = pd.read_csv('states.csv')
