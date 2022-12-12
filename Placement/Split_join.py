def splitjoin(sstring):
    line = sstring.split()
    a = "-".join(line)
    return a
if __name__ == "__main__":
    sstring = input()
    result = splitjoin(sstring)
    print(result)


'''input --- kabir is my name
   output --- kabir-is-my-name
'''