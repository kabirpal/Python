s = 'kabir123jabh'
lst = []
lst2 = []
# for i in s:
#     try:
#         if int(i):
#             lst.append(i)
#     except:
#         lst2.append(i)

for i in s:
    try:
        if int(i):
            lst.append(i)
    except:
        lst2.append(i)
print("".join(lst))
print(lst2)

