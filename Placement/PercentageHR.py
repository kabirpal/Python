n = int(input("Enter the number of students"))
student_marks = {}
for _ in range(n):
    name, *lne = input("Enter name followed by scores in 3 subjects").split()
    scores = list(map(float,lne))
    student_marks[name] = scores
inn = input()
a,b,c = student_marks[inn]
print('%.2f'%((a+b+c)/3))

