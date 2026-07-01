print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('''\nWelcome To Treasure Island 🏝️
Your Mission Is To Find the Treasure 💰
''')


name=input('Enter Your Name: ')

dir1 = input('In Which Direction Do You Want To Go To find out Box? Left or Right? ').lower()

if dir1 == 'right':
    print(f'''GAME OVER 💀
Congratulations! {name} You fell into the well and  found disaster instead of Treasure box 😂''')

elif dir1 == 'left':
    print(f'''{name} You chose the Best Direction 🤩''')
    dir2 = input("Will you swim or just wait for boat? ").lower()

    if dir2 == 'swim':
        print(f'''GAME OVER 💀
{name} You jumped into the water...
The fish are still laughing at you 🐟😂
''')

    elif dir2 == 'wait':
        print(f'''Good choice 😂
{name} You survived without becoming fish food 🌊''')
        
        door = input('''Now choose a door 🚪
Red, Blue, or Yellow?
Choose wisely... one of them is professionally dangerous 💀:
''').lower()

        if door == 'red':
            print(f'''GAME OVER {name} 💀
The Red Door was full of fire and danger 🔥
Bro got cooked instantly 😂
''')
        elif door == 'blue':
            print(f'''GAME OVER 💀
Behind the Blue Door was a hungry shark 🦈
{name} Now You became today's seafood special 😂''')
        elif door == 'yellow':
            print(f'''{name} YOU WIN 🏆✨
Behind the Yellow Door was treasure and freedom 💰🚪
For once... your luck actually worked 😂
''')
        else:
            print("Invalid door 🚪")

    else:
        print('Invalid option for Water')

else:
    print("Invalid direction ❌")

