# Rock Paper Scissors Game

## About My Project
I built this classic Rock Paper Scissors game in Python to practice working with complex `if-else` conditions and user inputs. To make the terminal look visually fun and interactive, I included large ASCII art layouts for the hand signs so you can actually see what both you and the computer picked.

## How It Works
The program is very straightforward to use. First, it asks you to type in your name to personalize the experience, and then it prompts you to pick a number: `0` for Rock, `1` for Paper, or `2` for Scissors. Once you hit enter, the program instantly generates a secret random move for the computer using Python's `random.randint()` feature.

## Game Logic and Results
To find out who won, the code runs through a nested `if-elif` setup that compares your choice directly against the computer's pick. It handles all possible scenarios—telling you if the game is a tie, if the computer beat you, or if you won with a celebratory message using your name and fun emojis. I also added a final safety check at the bottom so that if someone accidentally types a wrong number outside the 0-2 range, the program catches it and tells them to choose correctly.