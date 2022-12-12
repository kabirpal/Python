fname = input('Enter file name')
if (len(fname)<1):
   fname = 'mbox-short.txt'
   fread = open(fname)
else :
   fread = open(fname)

words = list()
for line in fread:
   if not line.startswith('From:'): continue
   line = line.split()
   words.append(line[1])
print(words)

counts = dict()
for count in words:
   counts[count] = counts.get(count,0) +1
print(counts)

maxvalue = None
maxkey = None

for key,value in counts.items():
   if maxvalue == None or value > maxvalue:
      maxvalue = value
      maxkey = key
print(maxkey, maxvalue)