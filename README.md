## Hangman Game (Python)

A simple command-line Hangman game built in Python.

The player must guess the correct word (from fruits, countries, or occupations) before the hangman is completely drawn!

## How to Play

Run the game using Python.

Choose a category:

fruits

countries

occupations

A random word from your chosen category will be selected.

Guess letters one by one.

You lose a life for every wrong guess.

If you run out of lives before guessing the word — you lose!

If you guess all letters correctly — you win!

## Features

* Multiple categories — fruits, countries, occupations
* Hangman visuals for every guess
* Input validation — prevents invalid category selection
* Keeps track of already guessed letters
* Simple and fun console interface

## Example Gameplay

Welcome to Hangman game !!!
If you guess the word before hangman forms you win or else you lose
Enter your choice of words to be asked fruits or countries or occupations: fruits

['_', '_', '_', '_','_']

guess the letter: a

['_', 'a', '_', '_', '_']

Guess the letter: z

Wrong guess !! Lost one life

   ------
   |    |
   O    |
        |
        |
        |
        |
   ======

...
You Win !!! The word is mango

## Code Explanation

The game uses lists of words for each category (fruits, countries, occupations).

The player is asked to select a category. Invalid inputs are handled using a loop until a valid option is chosen.

The program selects a random word using random.choice().

A while loop keeps the game running until:

The player wins (all letters guessed correctly), or

The player loses (no lives left).

Hangman visuals are displayed from the stages list based on remaining lives.

## How to Run

Save the code as hangman.py

Open your terminal or command prompt

Navigate to the file’s directory

Run:

python hangman.py
