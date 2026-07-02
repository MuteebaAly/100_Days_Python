# Treasure Island Text Game
Take treasure box Ascii  from the https://ascii.co.uk/art/treasure

## About My Project
I built this Text-Based Adventure Game in Python to practice writing and structuring deeply nested conditional statements. It is a fun, choice-based game inspired by classic text adventures where the player has to make the exact right decisions to find a hidden treasure box without hitting a sudden "Game Over."

## How It Works
The game starts by printing a large ASCII brick-art graphic and asking for your name to personalize the story lines. From there, the program takes step-by-step text inputs from the player to move forward. Every single decision you make leads down a different branch of the plot: first, you have to choose between going Left or Right, then you decide whether to Swim or Wait for a boat, and finally, you have to pick between a Red, Blue, or Yellow door. 

## Logic and Game Over Paths
I used a nested `if-elif-else` layout to manage all the different paths and consequences in the game. To prevent simple capitalization bugs, I applied the `.lower()` function to all user inputs so that typing 'LEFT' or 'left' both work perfectly. If you pick a wrong path, the code instantly triggers a funny custom message explaining how you failed, while the correct path rewards you with the winning screen. I also included fallback `else` blocks at each step to catch invalid typing so the program safely handles unexpected words.