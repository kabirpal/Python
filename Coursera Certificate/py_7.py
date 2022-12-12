# grade = input('Enter your grade')
# grade = float(grade)
# if grade<= 1.0:
#    if grade >= 0.9 :
#        print('A')
#    elif grade >=0.8 :
#        print('B')
#    elif grade >=0.7 :
#        print('C')
#    elif grade >=0.6 :
#        print('D')
#    elif grade < 0.6 :
#        print('F')
# else :
#    print('Error')
# Python3 code to demonstrate
# to find the first position of the character
# in a given string

# Initializing string
ini_string = 'abcdef'
c = "c"
# Character to find
# printing initial string and character
print ("initial_string : ", ini_string, "\ncharacter_to_find : ", c)

# Using Naive Method

if(c in ini_string): 
	k = ini_string.find(c)
	print ("Character {} is present at {}".format(c,k))
else:
	print ("No such character available in string")
