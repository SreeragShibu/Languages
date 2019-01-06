from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
cnt=input("enter count")
c=int(cnt)
pos=input("enter pos")
p=int(pos)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="http://py4e-data.dr-chuck.net/known_by_Surien.html"
ls=list()
for i in range(c):
    html=urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")
    tags=soup('a')
    url= tags[p-1].get('href', None)
    s=tags[p-1].contents[0]
    ls.append(s)
print(ls[len(ls)-1])
