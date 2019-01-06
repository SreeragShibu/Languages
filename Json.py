import urllib.request, urllib.parse, urllib.error
import json
serviceurl='http://py4e-data.dr-chuck.net/comments_119534.json'
sum=0
uh=urllib.request.urlopen(serviceurl)
data=uh.read().decode()
js=json.loads(data)
datap=js["comments"]
for item in datap:
    sum+=int(item["count"])
print(sum)
