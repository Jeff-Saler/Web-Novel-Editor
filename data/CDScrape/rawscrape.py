import requests
from bs4 import BeautifulSoup

link='http://m.shushu8.com'
marker='/panlong/3.html'
for n in range(1,201):
    page=requests.get(link+marker)
    soup=BeautifulSoup(page.content,'html.parser')
    cont=soup.find('div',{'id':'content'})
    content=[]
    for i in cont:
        if str(i).strip().replace('<br/>','').startswith('<br>'):
            break
        else:
            content.append(str(i).strip().replace('<br/>',''))
    marker=soup.find(class_='nr_page').find_all('a',href=True)[2].attrs['href']
    with open('Raw/raw{}.txt'.format(n),'w') as w:
        w.writelines(content)
    print(n)
