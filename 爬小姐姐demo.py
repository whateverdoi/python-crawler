import re
import requests
from bs4 import BeautifulSoup
import time
url = 'http://pic.netbian.com/4kmeinv/'
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0"
}
head1 = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0"
}
head2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0"
}
response = requests.get(url=url, headers=head)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
all_links = soup.find_all('li')
method1 = re.compile(r'"(.*?\d+.html)"')
method2 = re.compile(r'src="(.*?)"')
i = 0
for item in all_links:
    if re.findall(method1, str(item)):
        reallink = 'http://pic.netbian.com'+re.findall(method1, str(item))[0]
        response = requests.get(url=reallink, headers=head1)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all_links = soup.find_all('div', class_='photo-pic')
        for item in all_links:
            i += 1
            imgurl = 'http://pic.netbian.com'+re.findall(method2, str(item))[0]
            wuhu = requests.get(url=imgurl, headers=head2)
            where = r'/home/lhh/图片/美女/美女%s.jpg' % (i)
            f = open(where, 'wb')
            f.write(wuhu.content)
            time.sleep(3)
