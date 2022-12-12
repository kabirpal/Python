class RomanNumerals:
    def solution(number):
        number = list(number)
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        inital_vaue = 0
        for i in range(len(number)):
            if i>0 and dic[number[i]] > dic[number[i-1]]:
                inital_vaue += dic[number[i]]- 2*dic[number[i-1]]
            else:
                inital_vaue += dic[number[i]]
        return inital_vaue

number = input()
print(RomanNumerals.solution(number))
