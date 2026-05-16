import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Name=input('Enter You Name: ')

Human_choice=int(input('''Choose Number
For Rock :  0
For paper : 1
For Scissor : 2\n'''))

computer_choice=random.randint(0,2)
#print(computer)

if Human_choice==0 :
    print(rock)
    if computer_choice==0:
        print(f'Computer chose {computer_choice}\n {rock} \n Game is Tie😊 No One Win this game')

    elif computer_choice==1:
        print(f'Computer chose {computer_choice}\n {paper} \n {Name} You Lose this game😕😖')
    elif computer_choice==2:
        print(f'Computer chose {computer_choice}\n {scissor} \n  {Name} Congratulations!!! You Win this game 🤩😃🥳')
    
elif Human_choice==1 :
    print(paper)    
    if computer_choice==0:
        print(f'Computer chose {computer_choice}\n {rock} \n {Name} Congratulations!!! You Win this game 🤩😃🥳')
    elif computer_choice==1:
        print(f'Computer chose {computer_choice}\n {paper} \n Game is Tie 😊 No One Win this game')
    elif computer_choice==2:
        print(f'Computer chose {computer_choice}\n {scissor} \n {Name} You Lose this game😕😖')
    
elif Human_choice==2 :
    print(scissor)
    if computer_choice==0:
        print(f'Computer chose {computer_choice}\n {rock} You Lose this game😕😖')
    elif computer_choice==1:
        print(f'Computer chose {computer_choice}\n {paper} Congratulations!!! You Win this game 🤩😃🥳')
    elif computer_choice==2:
        print(f'Computer chose {computer_choice}\n {scissor} \n Game is Tie 😊 No One Win this game')
else:
    print(f'{Name} You Enter Wrong Number Plz Choose  Nmbr Between (0_2)  ')
 
