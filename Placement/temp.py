# Python program to remove vowels from a string
# Function to remove vowels

# import the module for regular expression (re)
import re
def rem_vowel(string):
	return (re.sub("[aeiouAEIOU]","",string))		

# Driver program
string = "GeeksforGeeks - A Computer Science Portal for Geeks"
print(rem_vowel(string))
