largest = None
smallest = None
while True:
    x = input("Enter a number: ")
    if x == "done" : break
    try:
        y = float(x)
    except:
        print ('Invalid input')
        continue
    if smallest is None:
       smallest = y
    elif smallest > y:
         smallest = y
    if largest is None:
       largest = y
    elif y > largest:
       largest = y

def done(largest,smallest):
    print (('Maximum is'), int(largest))
    print (('Minimum is'), int(smallest))

done(largest,smallest)
