name = "mbox-short.txt"
handle = open(name)
words = list()

for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])
#print(words)

counts = dict()

for word in words:
           counts[word] = counts.get(word, 0) + 1 
print(counts)   
maxval = None
maxkey = None
for key,val in counts.items() :
   if maxval == None or val > maxval : 
      maxval = val
      maxkey = key   

print (maxkey, maxval)
