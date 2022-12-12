def capitalize(a):
    words = a.split(" ")
    m = [w.capitalize() for w in words]
    return " ".join(m)


a = input()
print(capitalize(a))


"""
input = kabir is my name
output = Kabir Is My Name

"""