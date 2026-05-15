N = int(input("How many operations that you want to perform: "))
l=[]
for i in range(N):
    user_input=(input(f'Enter commands {i}: ')).split()
    #print(user_input[0])
    #print(user_input[1])
    #print(user_input[2])


    #check lengths and perform opertions:
    if len(user_input)==3:
        command=user_input[0]
        position=int(user_input[1])
        num=int(user_input[2])

        if command=='insert':
            l.insert(position,num)
        else:
            continue

    elif len(user_input)==2:
        command=user_input[0]
        num=int(user_input[1])

        if command=='remove':
            l.remove(num)
        else:
            l.append(num)
    
    elif len(user_input)==1:
        command=user_input[0]


        if command=='reverse':
            l.reverse()
        elif command=='sort':
            l.sort()
        elif command=='pop':
            l.pop()
        elif command=='reverse':
            l.reverse()
        elif command=='print':
            print(l)
        else:
            print('You Enter Wrong command')
        




    


