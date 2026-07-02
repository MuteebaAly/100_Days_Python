print(""" 
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|\n""")

def addition(n1,n2):
    result=n1+n2
    return result

def subtraction(n1,n2):
    result=n1-n2
    return result

def multiply(n1,n2):
    result=n1*n2
    return result

def division(n1,n2):
    result=n1/n2
    return result

num1=int(input("Enter Num1 : "))

while True:
    print("+\n-\nx\n/")
    operation=input("choose operation : ")
    num2=int(input("Enter Next Number : "))

    if operation=='+':
        result=addition(num1,num2)
        print(f'\n{num1} + {num2} = {result}\n') 

    elif operation=='-':
        result=subtraction(num1,num2)
        print(f'\n{num1} - {num2} = {result}\n')     
            
    elif operation=='*':
        result=multiply(num1,num2)
        print(f'/n{num1} * {num2} = {result}\n') 

    elif operation=='/':
        if num1>=0 and num2>0:
            result=division(num1,num2)    
            print(f'{num1} / {num2} = {result}') 
        else:
            print(f'Num is {num1}/{num2} Denominator should be greater than 0 \n so plz Write Nmber greater than 0')
            continue
          
    else:
        print(f"Invalid operation {operation} please write correct one")
        continue


    continue_option=input(f"Type 'y' to continue with {result}, 'n' to restart, 'q' to quit: ").lower()

    if continue_option=='y':
        num1=result
        continue

    elif continue_option=='n':
        num1=int(input("Enter Num1 : "))
        continue  
    elif continue_option=='q':
        break
    else:
        print('Invalid option')
        continue


