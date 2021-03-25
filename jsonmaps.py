import json, urllib.request, urllib.parse

url = 'http://py4e-data.dr-chuck.net/json?'

location = input('Enter Location: ')
parms = {'address': location, 'key': 42}

url = url + urllib.parse.urlencode(parms)
json_data = json.loads(urllib.request.urlopen(url).read())

print(json_data['results'][0]['place_id'])
