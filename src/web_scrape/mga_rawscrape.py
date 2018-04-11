import requests
from bs4 import BeautifulSoup

link='http://www.17k.com/list/493239.html'
page=requests.get(link)
soup=BeautifulSoup(page.content,'html.parser')
ind=soup.find_all(class_='Volume')[1]
tags=[]
z=0
while len(tags)<200:
    try:
        tags.append(list(list(ind.children)[3].children)[z].prettify().split('"')[1])
        z+=1
    except:
        AttributeError
        z+=1

link='http://www.17k.com'
for j in range(1,201):
    page=requests.get(link+tags[j-1])
    soup=BeautifulSoup(page.content,'html.parser')
    source=list(soup.find(class_='readAreaBox content').children)
    content=''
    for i in source:
        if i.name=='h1':
            content+=i.get_text().strip()
    x=list(soup.find(class_='p').children)
    k=0
    for i in range(len(x)):
        try:
            x[k]=x[k].strip()
            if x[k].endswith('End') or x[k].endswith('Start') or len(x[k])<8:
                del x[k]
            else:
                content+=x[k]+'\n'
                k+=1
        except:
            TypeError
            del x[k]
    with open('Raw/raw{}.txt'.format(j),'w') as f:
        f.write(content)
    print('Raw{} scraped'.format(j))
