s = 'aassasbasbabaabbbbbaaa1234a'
list1 = []
for j in s:
    try:
        if int(j):
            continue
    except:
        list1.append(j)
print("".join(list1))
dic ={}
for i in s:
    dic[i] = dic.get(i,0)+1
print(dic)