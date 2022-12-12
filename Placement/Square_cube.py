def square_no(number):
    square = []
    for i in number:
        square.append(i*i)
    return square

def cube_no(number):
    cube = [lambda i : i*i*i for i in number]
    for i in range(len(cube)):
        print(i*i*i)



number = range(1,100)
print(square_no(number))
print(cube_no(number))