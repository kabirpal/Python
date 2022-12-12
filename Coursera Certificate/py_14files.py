fname = input('Enter the file name')
if (len(fname) < 1):
    fname = "mbox-short.txt"
    fread = open(fname)
else:
   fread = open(fname)

count = 0

for line in fread :
    if line.startswith('From: '):
       word = line.split()
       count = count + 1
       print(word[1])
    continue
print("There were", count, "lines in the file with From as the first word")
