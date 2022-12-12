dic = {}
s = list()
for _ in range(int(input())):
    name = input()
    marks = float(input())
    if marks in dic:
        dic[marks].append(name)
    else:
        dic[marks]=[name]
    if marks not in s:
        s.append(marks)

print(dic)
print(s)
m = min(s)
s.remove(m)
m1 = min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)



















#working
# n = int(input())
# marksheet = [[input(),float(input())] for _ in range(n)]
# a =max(marksheet,key = lambda x :x[1] )
# marksheet.pop(a)
# print(marksheet)

        
# for i in marksheet:
    # if marksheet[1]
# n = int(input())
# person = []
# marks = []
# for i in range(n):
#     per = input()
#     person.append(per)
#     mar = input()
#     marks.append(mar)
# # print(person,marks)

