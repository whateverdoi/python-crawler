import re
import urllib.request
import requests
from bs4 import BeautifulSoup

def askURL(url):
    req=urllib.request.Request(url=url,headers=header)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    return html
#一些常量
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
i=0
baseurl='https://www.douban.com/doulist/3936288/?start='
method=re.compile(r'<img src="(.*?)"/>')

for n in range(15):
    url=baseurl+str(n*25)
    html=askURL(url)
    soup=BeautifulSoup(html,'html.parser')
    divlist=soup.find_all('div',class_='post')
    for item in divlist:
        i+=1
        imglink=re.findall(method,str(item))[0]
        where=r'/home/lhh/图片/豆瓣/img%d.jpg'%(i)#指定图片位置，在linux上面
        f=open(where,'wb')
        wuhu=requests.get(imglink)
        f.write(wuhu.content)

