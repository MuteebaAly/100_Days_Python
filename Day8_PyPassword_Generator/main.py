print("\n******* Welcome to the PasswordGenerator ******\n\n Lets Ask Some Question From You\n")
import random
import string


letters=int(input("How many letters would you like in the password?: "))

symbol=int(input("How many symbols would you like in the password?: "))

num=int(input("How many Numbers would you like in the password?: "))

#string.ascii letters contains all the letters upper+lower
all_letters=string.ascii_letters
#print(all_letters)

#string.punctaution contains all the special characters

all_symbols=string.punctuation
#print(all_symbols)


password=''
l=password 

for i in range(letters):
    ran_letter=random.choice(all_letters)
    l+=ran_letter

for j in range(symbol):
    ran_punctuation=random.choice(all_symbols)
    l+=ran_punctuation

for k in range(num):
        ran_num=random.randint(0,9)
        l+=str(ran_num)
        #random.shuffle(l)


password_list = list(l)

random.shuffle(password_list)

final_password = "".join(password_list)
print("Here is Your Password: \n", final_password)


print('\n********** Thanks For Using This :) **********\n')




