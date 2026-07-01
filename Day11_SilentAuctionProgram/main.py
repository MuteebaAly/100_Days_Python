import os 
def highest_bid_calculation(database): 
    highest_bid=0
    winner_name=''

    for key, value in database.items():
        if value>highest_bid:
            winner_name=key
            highest_bid=value
    print(f"\nCongratulations! {winner_name} Is Winner  With Highest Bid {highest_bid}$") 

database={}
while True:
    print("\n***** Welcome To The Secret Auction Program *****\n")
    name=input("Whats Your Name?: ")
    bid=int(input("Whats your bid?: "))
    database[name]=bid

    choice=input("Are there any bidders? Type 'yes' or 'no': ").lower()

    if choice =='no':
        highest_bid_calculation(database)                           
        break    
    elif choice=='yes':
        os.system('cls')
    else:
        print("invalid option")
    
        




