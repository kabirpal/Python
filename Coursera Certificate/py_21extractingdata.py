import urllib.request ,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#all the input
url = input('Enter-')
count = int(input('Enter count'))
position = int(input('Enter position'))
html = urllib.request.urlopen(url , context = ctx).read()
soup = BeautifulSoup(html,'html.parser')


#the extraction work
href = soup('a')
#here we declare all the websites in the file
for i in range(count):
#here he count function decides how many times i want to run the fuction    
    link = href[position].get('href', None)
    print (href[position].contents[0])
#here the position function decides at which point you want to open the link
    html = urllib.request.urlopen(link).read()
#this htmk will used to open the new link until the count turns to be zero
    soup = BeautifulSoup(html,"html.parser")
#here this beautifulsoup is used again to sort out the html link, cuz it is the new link
    href = soup('a')
#this extra href contains the new link