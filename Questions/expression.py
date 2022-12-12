import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
   line = line.rstrip()
   num = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
   if len(num) != 1 :
      continue
   numb = float(num[0])
   numlist.append(numb)
print('Minimum:',min(numlist))
print('Maximum:',max(numlist))