import string

print(r'''                               
  ___ ___  __ _ ___  ___ _ __ 
 / __/ _ \/ _` / __|/ _ \ '__|
| (_|  __/ (_| \__ \  __/ |   
 \___\___|\__,_|___/\___|_|                                         
       _       _               
      (_)     | |              
  ___ _ _ __  | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                                                            
''')

alphabets = list(string.ascii_lowercase)
exit_option = ''

while exit_option != 'no':

    encrypt = []
    decrypt = []

    print("-" * 15) 
    message = input("Do You Want To Encrypt ('Encode') Or Decrypt ('Decode'): ").lower()
    print() 

    if message == 'encode':

        msg = input("Write Message that you want to encode: ")
        shift = int(input("Enter Shift Number: "))
        print() 

        for i in range(len(msg)):
            for j in range(len(alphabets)): 
                if alphabets[j] == msg[i]:
                    index_i = (j + shift) % 26   
                    encrypt.append(alphabets[index_i])
        
        print(f"👉 Encrypted Message is: {''.join(encrypt)}")
        print() 
        exit_option = input("Write 'yes' to go again, otherwise write 'no': ").lower()
        print()

    elif message == 'decode':

        msg = input("Write Message that you want to decode: ")
        shift = int(input("Enter Shift Number: "))
        print()

        for i in range(len(msg)):
            for j in range(len(alphabets)): 
                if alphabets[j] == msg[i]:
                    index_i = (j - shift) % 26   
                    decrypt.append(alphabets[index_i])
        
        print(f"Decrypted Message is: {''.join(decrypt)}")
        print() 
        exit_option = input("Write 'yes' to go again, otherwise write 'no': ").lower()
        print()

    else:
        print("Invalid input! Please enter either 'encode' or 'decode'.")
        print()