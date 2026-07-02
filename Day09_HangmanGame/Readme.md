# My Hangman Game

## About My Project
I built this classic Hangman guessing game in Python to practice working with loops, lists, and conditions. It is a fun text-based game where the computer picks a secret word, and you have to guess it letter by letter before you run out of lives.

## How It Works
The program starts by importing a huge list of words from a separate file named `hangman_words` and picks one secret word randomly using the `random` module. It then creates a list of hidden dashes that matches the exact length of that word. Every time you type a letter, the code checks if it is valid (only a single letter). If your guess is correct, a loop runs through the word and swaps the blank dashes with your correct letter so you can see your progress.

## Lives and Game Over
You start the game with 6 lives. If you guess a wrong letter, you lose one life, and the program uses cool ASCII text art to draw a part of the hangman on the screen. I set up the conditions so that the game keeps looping until one of two things happens: you either guess all the letters correctly to win, or you lose all 6 lives, which triggers a "Game Over" and reveals the secret word.