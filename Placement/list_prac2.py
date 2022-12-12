#working
n = int(input())
l = []
for _ in range(n):
    x = input().split()
    cmd = x[0]
    args = x[1:]
    if cmd == 'insert':
        l.insert(int(args[0]),int(args[1]))
    if cmd == 'remove':
        l.remove(int(args[0]))
    if cmd == 'print':
        print(l)
    if cmd == 'append':
        l.append(int(args[0]))
    if cmd == 'sort':
        l.sort()
    if cmd == 'reverse':
        l.reverse()
    if cmd == 'pop':
        l.pop()
print(l)

# 4
# insert 0 3
# append 2
# append 1
# sort
# [1, 2, 3]