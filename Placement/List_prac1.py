#working
n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "("+ ",".join(args) +")"
        #for insert cmd it will create insert(5,6)
        eval("l."+cmd)
        #l.insert(5,6)
    else:
        print(l)

# 4
# insert 0 3
# append 2
# append 1
# sort
# [1, 2, 3]