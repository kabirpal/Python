fname = open('mbox-short.txt')
counts = dict()
for line in fname:
    if line.startswith('From:'):
       words = line.split()
       mail = words[1]
       counts[mail] = counts.get(mail, 0) + 1

#counting
bigcount = None
bigword = None
for mail,count in counts.items():
    if bigcount is None or count > bigcount:
       bigword = mail
       bigcount = count
print(bigword,bigcount)