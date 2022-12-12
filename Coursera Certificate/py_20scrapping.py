import urllib.request ,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = list()
url = input('Enter-')
html = urllib.request.urlopen(url , context = ctx).read()
words = BeautifulSoup(html,'html.parser')

tags = words('span')
sum = 0
for word in tags:
    sum=sum+int(word.contents[0])
print(sum)