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
def ceaser_encode(msg, shift):
    alphabets = list(string.ascii_lowercase)
    encrypt = [] 
   
    for i in range(len(msg)):
        for j in range(len(alphabets)): 
            if alphabets[j] == msg[i]:
                index_i = (j + shift) % 26   
                encrypt.append(alphabets[index_i])

    print(f"Encrypted Message is: {''.join(encrypt)}")


def ceaser_decode(msg, shift):
    alphabets = list(string.ascii_lowercase)
    decrypt = [] 

    for i in range(len(msg)):
        for j in range(len(alphabets)): 
            if alphabets[j] == msg[i]:
                index_i = (j - shift) % 26   
                decrypt.append(alphabets[index_i])
                
    print(f"Decrypted Message is: {''.join(decrypt)}")


exit_option = ''
while exit_option != 'no':
    message = input("Do You Want To Encrypt ('Encode') Or Decrypt ('Decode'): ").lower()
    print() 

    if message == 'encode':
        msg = input("Write Message that you want to encode: ")
        shift = int(input("Enter Shift Number: "))
        print() 
        
        ceaser_encode(msg, shift)

    elif message == 'decode':
        msg = input("Write Message that you want to decode: ")
        shift = int(input("Enter Shift Number: "))
        print()
        
        ceaser_decode(msg, shift)

    else:
        print("Invalid input! you can only Enter Encode or Decode.")
    
    print()
    
    exit_option = input("Write 'yes' to go again, otherwise write 'no': ").lower()
    print()