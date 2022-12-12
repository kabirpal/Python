x =  "X-DSPAM-Confidence:   0.8475"
y = x.find(':')
z = x[y+4:]
# here the : this colon refers to the range funtion
z = float(z)
print(z)
