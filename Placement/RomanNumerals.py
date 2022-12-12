class Solution:
    def romanToInt(self, s: str):
        s = list(s)
        count = 0
        i = 0
        for i in range(len(s)):
            if i < len(s)-1:
                if s[i] == 'I' and s[i+1] =='V':
                    count -= 1
                    i += 1
                elif s[i] == 'I' and s[i+1] =='X':
                    count = count - 1
                    i += 1
                elif s[i] == 'X' and s[i+1] =='L':
                    count = count - 10
                    i += 1
                elif s[i] == 'L' and s[i+1] =='C':
                    count = count - 10
                    i += 1
                elif s[i] == 'C' and s[i+1] =='D':
                    count = count - 100
                    i += 1
                elif s[i] == 'C' and s[i+1] =='M':
                    count = count - 100
                    i += 1
                elif s[i] == 'I':
                    count += 1
                    i += 1
                elif s[i] == 'V':
                    count += 5
                    i += 1
                elif s[i] =='X':
                    count += 10
                    i += 1
                elif s[i] == 'L':
                    count += 50
                    i +=  1
                elif s[i] == 'C':
                    count += 100
                    i += 1
                elif s[i] == 'D':
                    count += 500
                    i += 1
                elif s[i] == 'M':
                    count += 1000
                    i += 1

            else:
                if s[i] == 'I':
                    count += 1
                    i += 1
                elif s[i] == 'V':
                    count += 5
                    i += 1
                elif s[i] =='X':
                    count += 10
                    i += 1
                elif s[i] == 'L':
                    count += 50
                    i +=  1
                elif s[i] == 'C':
                    count += 100
                    i += 1
                elif s[i] == 'D':
                    count += 500
                    i += 1
                elif s[i] == 'M':
                    count += 1000
                    i += 1
        return count
    
j = Solution()
s = input()
print(j.romanToInt(s))
        