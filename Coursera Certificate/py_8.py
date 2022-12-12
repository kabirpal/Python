hours = input('Enter hours')
hrs = float(hours)
rate = input('Enter rate')
rt = float(rate)
def computepay (hrs):
   if hrs < 40:
      pay = hrs * rt
      return pay
   else :
      x = float(hrs) - 40
      pay = 40 * rt + x * rt * 1.5
      return pay
print('Pay',computepay (hrs))
