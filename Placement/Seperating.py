import re

x ='kabirpal53'

temp = re.compile("([a-zA-Z]+)([0-9]+)")
y = temp.match(x).groups()

print(y)