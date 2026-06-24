import random 

print(r"""                                            
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/          """)


#words_list = ["pakistan", "blossom", "aesthetic", "gatekeeper", "almirah", "suspicious",'sliper',"poems","multitalennted","hangman","flower"] #manually 
 
import hangman_words #import file 

word = random.choice(hangman_words.word_list)
dash = []

for i in range(len(word)):
    dash.append('-')

life = 6  
guess = "" 

while life > 0:
    guess = input("Guess a Letter: ").lower()

    if len(guess) > 1:
        print("Please Enter only Single letter :)")
    else:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    dash[i] = word[i]
            print(dash)
            
            if dash != list(word):
                guess = " "
            else:
                print(f"\nGAME OVER !!!\nCONGRATULATIONS YOU WIN 😎👏🎉\nYOU GUESS CORRECTLY {word} WORD")
                break
                
        elif guess not in word:
            life -= 1
            
            if life == 5:
                print(r"""  +----+
  O    |            
       | 
       | 
       | 
       | 
====================== """)
                print(f"you guess {guess} thats not correct. you loose a life \n", dash)
                
            elif life == 4:
                print(r"""  +----+
  O    |            
 /     | 
       | 
       | 
       | 
====================== """)
                print(f"you guess {guess} thats not correct. you loose a life \n", dash)
                
            elif life == 3:
                print(r"""  +----+
  O    |            
 /|    | 
       | 
       | 
       | 
====================== """)
                print(f"you guess {guess} thats not correct. you loose a life \n", dash)

            elif life == 2:
                print(r"""  +----+
  O    |            
 /|\   | 
       | 
       | 
       | 
====================== """)
                print(f"you guess {guess} thats not correct. you loose a life \n", dash)
                
            elif life == 1: 
                print(r"""  +----+
  O    |            
 /|\   | 
 /     | 
       | 
       | 
====================== """)
                print(f"you guess {guess} thats not correct. you loose a life \n", dash)
                
            else: 
                print(r"""  +----+
  O    |            
 /|\   | 
 / \   | 
       | 
       | 
====================== """)
                print(f"GAME OVER !!! 😭\nYou lose all lives. The correct word was '{word}'.")
                break 