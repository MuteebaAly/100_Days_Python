n = int(input('Enter number: '))
student_marks = {}

for _ in range(n):
    name , *line = input('Enter name and all the marks ').split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("enter query : ")
    

if query_name in student_marks:
    sum=0
    for i in student_marks[query_name]:
        sum+=i

    divsion=sum/len(student_marks[query_name])
    print(divsion)
        
else:
    print('name is not in the dict')



