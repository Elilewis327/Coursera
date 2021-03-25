import json, urllib.request, urllib.parse
total = 0

url = input('Url ->')

data = json.loads(urllib.request.urlopen(url).read())

for item in data['comments']:
    total += int(item['count'])
print(total)
