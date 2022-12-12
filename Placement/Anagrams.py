a=input("Enter string 1:")
b=input("Enter string 2:")
count=0
for i in a:
    for j in b:
        if i==j:
            count=count+1

if count==len(a):
    print("Strings are anagram of each other.")

else:
    print("Strings are not anagram of each other.")

# str1 = "aaba"
# str2 = "bada"
# count = 0
# if len(str2) == len(str1):
#     for i in range(0,len(str2)):
#         for j in range(0,len(str1)):
#             if i == j:
#                 count += 1
    
#         print("It is anagram")
# else:
#     print("not anagram")

# class Anagrams:
#     def solution(l):
#         j = len(l)-1
#         i = 0
#         while(i<j/2):
#             if l[i] != l[j]:
#                 return False
#             else:
#                 j -= 1
#                 i += 1
#         return True
            
# if __name__== '__main__':
#     num = input()
#     l =[]
#     for i in num:
#         l.append(i)
#     print(Anagrams.solution(l))


