s = 'aabbaaaababaabababaabbbbbbbbbbbbcccccc'
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
keymax = max(zip(dic.values(),dic.keys()))[1]
print(keymax)

