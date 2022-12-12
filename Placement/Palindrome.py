def palindrome(lst):
    i = 0
    j = len(lst)-1
    while i<j/2:
        if lst[i]!=lst[j]:
            return False
        else:
            i +=1
            j -= 1
    return True
            
if __name__ == '__main__':
    s = input()
    lst = []
    for i in s:
        lst.append(i)
    print(palindrome(lst))
