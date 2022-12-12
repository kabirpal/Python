# n,w1 = input().split()
# n2,w2 = input().split()
# n3,w3 = input().split()
# m = input()
 
class Solution:
   def solve(self, weights, values, capacity):
      res = 0
      for pair in sorted(zip(weights, values), key=lambda x: - x[1]/x[0]):
         if not bool(capacity):
            break
         if pair[0] > capacity:
            res += int(pair[1] / (pair[0] / capacity))
            capacity = 0
         elif pair[0] <= capacity:
            res += pair[1]
            capacity -= pair[0]
      return int(res)

ob = Solution()
weights = [20, 50, 30]
values = [60, 100, 120]
capacity = 50
print(ob.solve(weights, values, capacity))