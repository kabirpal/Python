def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    st = "".join(l)
    return st


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


"""
Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

Sample Output

abrackdabra

"""