import urllib.request, urllib.parse, urllib.error
import json
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = "University of Cambridge"
url = serviceurl + urllib.parse.urlencode({'address': address})
uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)
place_id=js["results"][0]['place_id']
print(place_id)
