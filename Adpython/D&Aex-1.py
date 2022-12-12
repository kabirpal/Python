def Jan_feb(list1):
    if (list1['January']>list1['February']):
        print('Dollars you spent extra compare to February: ',list1['January'] - list1['February'])
    else:
        print('Dollars you spent extra compare to January: ',list1['February']-list1['January'])
    return
def Tot_quarter(list1):
    print('Total spending in 1st quater: ')
    print(list1['January']+list1['February']+list1['March'])
    return
# def exact_2000(list1):
#     y = list(list1.values())
#     for i in range(len(y)):
#         if y[i] == 2000:
#             print('Found')
#         else:
#             print('not')
   


    # if list1.values == 2000:
    #     print(list1.key())
    # else:
    #     print('No exact value found')
def June(list1):
    list1['June'] = 1980
    print(list1)
def April(list1):
    list1['April']=list1['April']+200
    print(list1)

list1 = {'January':2200,'February':2350,'March':2600,
'April':2130,
'May':2190}
Jan_feb(list1)
Tot_quarter(list1)
# exact_2000(list1)
June(list1)
April(list1)