def reversing(Sentence):
    words = Sentence.split(" ")
    newwords = [word[::-1] for word in words]
    sen = " ".join(reversed(newwords))
    return sen

Sentence = "My name is kabir"
print(reversing(Sentence))