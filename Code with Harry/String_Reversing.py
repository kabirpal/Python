# string = "This is my string"
# print(string[::-1].split())

def reverse(sen):
    words = sen.split(" ")
    #newwords = [word[-1::-1] for word in words]
    newwords = words[::-1]
    newsen = " ".join(newwords)
    return newsen

sen = "This is my String  reversing"
print(reverse(sen))