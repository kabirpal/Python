while True:
    print("""1) Addition
    2) Subtraction
    3) multiplication
    4) division
    0) Exist""")
    choice=int(input("Enter your choice"))
    if (choice == 1):
        n1 = int(input("Enter number 1"))
        n2 = int(input("Enter number 2"))
        result = n1+n2
        print(result)
    elif (choice == 2):
        n1 = int(input("Enter number 1"))
        n2 = int(input("Enter number 2"))
        result = n1-n2
        print(result)
    elif (choice == 3):
        n1 = int(input("Enter number 1"))
        n2 = int(input("Enter number 2"))
        result = n1*n2
        print(result)
    elif (choice == 4):
        n1 = int(input("Enter number 1"))
        n2 = int(input("Enter number 2"))
        result = n1/n2
        print(result)
    elif (choice == 0):
        break
       
