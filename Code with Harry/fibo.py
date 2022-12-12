class Interview:
    def fibo(num):
        a = 0
        b = 1
        temp = 0
        
        while(num):
            temp = a
            a = b
            b = temp + b
            num -= 1
            
        return b

num = int(input('Enter any number'))
print(Interview.fibo(num))





"""
1 1 2 3 5 
num input
numth term
initialize = 0 and 1
temp
"""