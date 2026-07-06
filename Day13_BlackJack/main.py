print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
                       _/ |                
                      |__/
""")
import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
b=random.choices(cards,k=4)
human_card=b[0:2]
computer_card=b[2:4]

print("your_card = ",human_card)
print("Computer_card = ",b[2:3])



def computer():
    card_sum=computer_card[0]+computer_card[1]

    while card_sum<17:
        if card_sum<17:
            c=random.choice(cards)
            computer_card.append(c)
            card_sum+=c
            #print("computer card sum : ", card_sum )
        else:
             human()


        if card_sum>21:
            print(f'Your Final Card: {human_card} \n Computer Final Card: {computer_card} \n******* Computer Loose Game:( *********** ')
            break
        elif card_sum==21:
            print(f'Your Final Card: {human_card} \nComputer Final Card: {computer_card} \n------ Computer Win The Game --------')
            break


def human():
    card_choice=''
    human_card_sum=human_card[0]+human_card[1]
    #print(human_card_sum ,"human card sum ")
                    
    while card_choice!='n':
        card_choice=input("\n Do you want to hit or stand? Means want more card or not? if yes type 'y' otherwise type 'n' : ").lower()


        if card_choice=='y':
            n=random.choice(cards)
            human_card.append(n)
            human_card_sum+=n 
            #print(human_card)
        else:
             computer()
        

        if human_card_sum>21:
                print(f'Your Final Card: {human_card} \nComputer Final Card: {computer_card}')
                print(f"\n----------You Loose Game  -----------  ")
                break
        elif human_card_sum==21:
                print(f'Your Final Card: {human_card} \n Computer Final Card: {computer_card}')
                print(f"\n********** You Win Game:)  ************\n Bcz your card_sum is {human_card_sum} thats equal to 21")
                break

human()
