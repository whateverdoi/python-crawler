import urllib.request
from bs4 import BeautifulSoup
import re
from PIL import Image



def main():
    savedoc=''
    baseurl='https://www.douban.com/doulist/2772079/?start='
    method=re.compile(r'<img src="(.*?)"/>')      
    for i in range(15):
        url=baseurl+str(i*25)
        savedoc+=askURL(url)
        soup=BeautifulSoup(savedoc,'html.parser')
    first=soup.find_all('div',class_="post")
    for item in first:
       print(re.findall(method,str(item))[0])
        

    

#def getData(baseurl):
#    datalist=[]

#    return datalist

def askURL(url):
    head={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
            }
    req=urllib.request.Request(url=url,headers=head)
    response= urllib.request.urlopen(req)
    try:
        html=response.read().decode('utf-8')
    except Exception as e:
        print(e)
    return html
#def saveData(savepath):
#    print('储存数据')

if __name__=='__main__':
    main()
