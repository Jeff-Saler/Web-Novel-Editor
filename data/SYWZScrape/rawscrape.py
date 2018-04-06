import requests
from bs4 import BeautifulSoup

link='http://www.shenyinwangzuo.com/sywz/520/1-1.html'

for i in range(1,201):
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    content=''
    content+=str(list(soup.find(class_='entry-title').children)[0])+'\n'
    body=list(soup.find(class_='entry-content').children)
    body=[i.get_text().strip() for i in body if i.name=='p']
    for j in body:
        content+='\n'+j
    with open('raw{}.txt'.format(i),'w') as f:
        f.write(content)
    print('Raw{} scraped'.format(i))
    link=soup.find(class_='nav-next').prettify().split('"')[3]
