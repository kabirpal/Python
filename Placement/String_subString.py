def count_substring(string, sub_string):
    #initilizing c as 0
    c= 0
    for i in range(len(string)):
        #applying for loop to run the loop till len of string
        if string[i:].startswith(sub_string):
            #if string starts with substring irrespective of len
            #then enter in the loop\
            c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)