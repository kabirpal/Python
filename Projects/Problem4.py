x = int(input("Enter any Number"))
def findMultiples(x):
  for x in range(0, x + 1):
    if x % 3 == 0 and x % 5 == 0:
        print(x);

findMultiples(x);