import re
s = "welcome to geeksforgeeks"
# v = ['a','e','i','o','u']
# list1 = []
# for letter in s:
#     if letter not in v:
#         list1.append(letter)
# print("".join(list1))
print(re.sub("[aeiouAEIOU]","",s))