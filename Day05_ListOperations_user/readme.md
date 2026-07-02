# Python List Operations Program

## About My Project
I built this interactive Python script to practice dynamic list manipulation and handle custom user text commands. It is a great project for understanding how different built-in list methods work by letting the user control the list completely through the terminal.

## How It Works
The program starts by asking you how many operations ($N$) you want to perform. It then runs a loop exactly $N$ times to take your inputs. Every time you enter a command line, the code uses the `.split()` function to break the text into individual words so it can read the command name and the numbers separately.

## Processing Commands
To figure out what action to take, the code intelligently checks the length of your split input. If the input has three items, it extracts the position and number to call `.insert()`. If it has two items, it handles `.remove()` or `.append()`. For single-word inputs, it checks for specific keywords to run `.reverse()`, `.sort()`, `.pop()`, or simply print the current state of the list. It also includes an error handling path to catch any mistyped commands safely.