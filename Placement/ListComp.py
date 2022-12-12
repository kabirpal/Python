a = [1,2,3,4,5]
item = [lambda i : i*i for i in a]
for i in range(len(item)):
    print(i,end="***")


#creating a dic from two list

name = ['Khushi','Chandu','Piyu']
classes = [8,4,5]
z = zip(name,classes)
print('\n')
for i in z:
    print(i)

dic = { Name:Grade for Name,Grade in zip(name,classes)}
print(dic)
