from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="http://py4e-data.dr-chuck.net/comments_119531.html"
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")
print("worked")
tags=soup('span')
print("again")
sum=0
for tag in tags:
    # print("inside")
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    sum+=int(tag.contents[0])
print(sum)
