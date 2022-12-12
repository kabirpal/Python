# def reversing(str1):
#     list1 = []
#     for i in str1:
#         list1.insert(0,i)
#     return "".join(list1)
# OUTPUT = gnirts fo gnisrever ym si sihT



# def reversing(str1):
#     str1 = str1.split(" ")
#     start = 0
#     end = len(str1)-1
#     while start < end:
#         str1[start],str1[end] = str1[end],str1[start]
#         start +=1
#         end -=1
#     return str1
# OUTPUT = ['string', 'of', 'reversing', 'my', 'is', 'This']



# def reversing(str1):
#     list1 = str1.split(" ")
#     k = list1[::-1]
#     return k
# OUTPUT = ['string', 'of', 'reversing', 'my', 'is', 'This']


def reversing(str1):
    list1 = str1.split(" ")
    list2 = []
    for i in list1:
        list2.append(i[::-1])
    return " ".join(list2)

#output = sihT si ym gnisrever fo gnirts

if __name__ == "__main__":
    str1 = "This is my reversing of string"
    print(reversing(str1))
