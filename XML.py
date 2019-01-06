import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = 'http://py4e-data.dr-chuck.net/comments_119533.xml'
# # url = serviceurl + urllib.parse.urlencode({'address': address})
# data = urllib.request.urlopen(url).read()
# # print(data.decode())
# tree = ET.fromstring(data.decode())
# sum=0;
# print(tree);
# for i in tree:
#     print("inside")
#     # print('Num is:'r.find('comment').find('count').text)
#     print(i)
uh=urllib.request.urlopen(url)
data=uh.read()
# print(data.decode())
tree=ET.fromstring(data)
result=tree.findall('comments/comment')
# print(result)
sum=0
for item in result:
    a=int(item.find('count').text)
    sum+=a
print(sum)
