class Factorial:
    def factorial(x):
        fac = 1
        for i in range(1,x+1):
            fac *= i
        return fac

if __name__ == '__main__':
    x = 6
    print(Factorial.factorial(x))