# My Secret Auction Program

## About My Project
I built this Secret Auction program in Python to create a fun, blind-bidding experience right in the terminal. It is designed for situations where multiple people want to bid on something, but they need to keep their bid amounts completely hidden from each other until the very end.

## How It Works
The program works by taking continuous inputs from the users in a loop. First, it asks for your name, then it asks for your bid amount, and automatically saves this pair inside a dictionary database. If there are more bidders coming up next, I used `os.system('cls')` to clear the terminal screen completely. This ensures that the next person cannot scroll up or peek at what the previous person bid, keeping the auction truly secret.

## Finding the Winner
Once all bidders have entered their amounts and someone types `no` to the question, the loop breaks. The program then triggers a custom function that loops through my database dictionary. It compares all the values, filters out the highest number, and instantly prints a nice congratulatory message showing the winner's name along with their highest winning bid.

#works