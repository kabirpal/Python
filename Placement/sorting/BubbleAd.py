def BubbleSort(elements,x):
    n = len(elements)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if elements[j][x] > elements[j+1][x]:
                elements[j][x], elements[j+1][x] = elements[j+1][x],elements[j][x]
                swapped = True
        if not swapped:
            break

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
x = input('Enter the key')
BubbleSort(elements,x)
print(elements)
