import urllib.request, re
from bs4 import BeautifulSoup

url = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1201199.html').read()

soup = BeautifulSoup(url, 'html.parser')
total = 0

for tag in soup('td'):
    search = re.findall("\>([0-9]+)\<\/", str(tag))
    if search:
        total += int(search[0])
print(total)
