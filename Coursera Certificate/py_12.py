#fn = input('Enter the file name')
fo = open("Coursera Certificate\mbox.txt")
count = 0
tot = 0
ans = 0
for line in fo:
    if line.startswith('X-DSPAM-Confidence:'):
       count = count + 1
       num = float(line[21:])
       tot = num + tot
    continue
ans = tot/count
print('Average spam confidence:',ans)