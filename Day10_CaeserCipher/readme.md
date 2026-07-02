# Caesar Cipher Project

## About My Project
I made this Python program to build a secret messaging tool called a Caesar Cipher. It is a fun project that lets you lock your text messages with a secret number so nobody else can read them, or unlock them if someone sends you a hidden message.

## How It Works
The program works by using two separate functions that I wrote for encoding and decoding. They take your message and shift every letter forward or backward in the alphabet. When you want to encode, it moves the letters forward by the secret shift number you type in. When you want to decode, it moves them backward by that same number. I wrote the logic using a small math trick (`% 26`) inside these functions so that if the shifting goes past the letter 'z', it smoothly wraps around back to 'a' without crashing.

## Running and Options
To run the program, you just use the `python main.py` command in your terminal. It will instantly show a cool text art banner and ask if you want to 'encode' or 'decode'. After you type your message and secret shift number, it prints the result on the screen. At the end, it asks if you want to try another message; you can type 'yes' to keep going or 'no' to close the program.
