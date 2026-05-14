
record=[]

for _ in range(int(input('enter the nmber of students: '))):
    name = input('Enter name: ')
    score = float(input('Enter scores : '))
     
    record.append([name,score])
    #print(record)
 
score=[]
for i in record:
    score.append(i[1])
 
 
for i in range(len(score)):
    for j in range(0,i+1):
        if record[i][1]<record[j][1]:
            record[i],record[j]=record[j],record[i]
            
    
    #print('Record  \n', record,'\n')



unique_scores = []
for student in record:
    s = student[1]
    if s not in unique_scores:
        unique_scores.append(s)


second_lowest = unique_scores[1]


names = []
for student in record:
    if student[1] == second_lowest:
        names.append(student[0])


for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]


for n in names:
    print(n)
   
   


        







    