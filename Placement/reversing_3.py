A = 'this is my reversing practice'
words = A.split()
s = []
for word in words:
    s.insert(0,word)
print(" ".join(s))