largest = None
smallest = None

while True:
    x = input('Enter any number')
    if x == "done": break
    try: 
        y = float(x)
    except:
        print('Invalid input')
        continue
    if smallest == None:
        smallest = y
    elif smallest > y:
        smallest = y
    if largest == None:
        largest = y
    elif largest < y:
        largest = y
    
def done(largest,smallest):
    print(("minimum number is"), int(smallest))
    print(("Maximum number is "),int(largest))
done(largest,smallest)

