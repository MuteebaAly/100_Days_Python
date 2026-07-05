
# Student Average Marks Calculator

## About My Project
I built this Python script to practice working with dictionaries, variable-length inputs, and basic mathematical operations. It is a handy little tool that lets you store academic scores for multiple students and then quickly look up a specific student to calculate and print out their average score.

## How It Works
The program first asks you how many students you want to add to your records. Then, it runs a loop to take the student's name and all their marks in a single line. I used a neat Python feature called unpacking (`name, *line`) along with `.split()` so the program can easily separate the student's name from their scores. The code then automatically converts those scores into decimal numbers using `map(float)` and saves them as a list inside a dictionary database, using the student's name as the key.

## Finding the Average
After saving all the data, the program prompts you to type in a "query name" to search for. If the name exists in the dictionary, a loop runs through that specific student's score list to add all their marks together. It then divides that total sum by the number of scores to get the final average and displays it on the screen. If you enter a name that wasn't recorded, the program safely jumps to the `else` block and warns you that the name is not in the dictionary. 

added 