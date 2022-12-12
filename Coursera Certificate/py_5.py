hours = input('Enter hours')
hours = float(hours)
rate = 10.50
if (hours <= 40):
   pay = hours * rate
   print('Pay = ',pay)
else :
   x = float(hours) - 40
   pay = 40 * 10.50 + x * 10.50 * 1.5
   print('pay =',pay)
print('All done')
