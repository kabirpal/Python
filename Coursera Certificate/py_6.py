hours = input('Enter hours')
rate = input('Enter rate')
try :
   hrs = float(hours)
   rt = float(rate)
except:
   print('Enter a numeric value')
   quit()
#print(hrs,rt)
if hrs < 40:
   pay = hrs * rt
   print('Pay = ',pay)
else :
   x = float(hrs) - 40
   pay = 40 * rt + x * rt * 1.5
   print('pay =',pay)
print('All done')
