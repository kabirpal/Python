try:
    j = open("hello.txt",'w')
    j.write('This is new me, I\'m not a looser')
except Exception as e:
    print(e)
    print('There\'s an error')
# finally:
#     print('I will always execute')
    