import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
b=random.choices(cards,k=4)
human_card=b[0:2]
computer_card=b[2:4]

print("your_card = ",human_card)
print("Computer_card = ",b[2:3])



def computer():
    card_sum=0

    while card_sum<17:
        if card_sum<17:
            computer_card.append(random.choice(cards))
            print(computer_card)
            for i in range(len(computer_card)):
                card_sum+=computer_card[i]
            print("computer card sum : ", card_sum )
            
    if card_sum==21:
        print(f'Your Final Card: {human_card} \n Computer Final Card: {computer_card} \n ------ Computre Win The Game --------')




def human():
    card_choice=''
    human_card_sum=0
    
                
    while True:
        card_choice=input("\n Do you want to hit or stand? Means want more card or not? if yes type 'y' otherwise type 'n' : ").lower()

        if card_choice=='y':
            human_card.append(random.choice(cards))
            print(human_card)
            for i in range(len(human_card)):
                human_card_sum+=human_card[i]
                            #print(human_card_sum , "card human sum ")
            if human_card_sum>21:
                print(f'Your Final Card: {human_card} \n Computer Final Card: {computer_card}')
                print(f"You Loose Game:( ")
                break
            elif human_card_sum==21:
                print(f'Your Final Card: {human_card} \n Computer Final Card: {computer_card}')
                print("You Win Game:( Bcz your card_sum is {human_card_sum} thats equal to 21")
                break 
        else:
            computer()
    
human()

#card list 
#2. generate randomly 2 card for both person
#3. break list  through slicing
#4. ask from user hit or stand 