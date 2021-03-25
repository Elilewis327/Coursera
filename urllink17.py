import urllib.request, re
from bs4 import BeautifulSoup
url = " http://py4e-data.dr-chuck.net/known_by_Oluwatosin.html"

def connect(url):
    return BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')

times = 7
position = 18

for i in range(times):
    url = re.findall('href="(.+)"', str(connect(url)('a')[position-1]))
    url = str(url[0])
    print(url)
