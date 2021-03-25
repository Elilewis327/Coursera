import xml.etree.ElementTree as ET
import urllib.request
total = 0

#url = input('Url ->')
url='http://py4e-data.dr-chuck.net/comments_1201201.xml'

data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
elements = tree.find('comments').findall('comment')
for item in elements:
  total += int(item.find('count').text)
print(total)
