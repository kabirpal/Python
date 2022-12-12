import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET

list_of_ints = []
url = ('http://py4e-data.dr-chuck.net/comments_42.xml')
url_to_open = urllib.request.urlopen(url).read()

tree = ET.parse(url)
root = tree.getroot()
lst = root.findall('comment')

for item in lst:
   print(item.find('count'))