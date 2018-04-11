import requests
from bs4 import BeautifulSoup

link='https://m.xs.la/9_9081/'
marker='4520432.html'

for n in range(1,201):
    page=requests.get(link+marker)
    soup=BeautifulSoup(page.content,'html.parser')
    content=[]
    for i in range(len(list(soup.find('div',{'id':'chaptercontent'}).children))):
        stuff=str(list(soup.find("div", {"id": "chaptercontent"}).children)[i]).strip()
        if len(stuff)>6 and not stuff.startswith('<'):
            content.append(stuff)
    for i in soup.find_all('a', href=True):
        try:
            if i.attrs['id']=='pb_next':
                found=i.attrs['href']
        except:
            KeyError
    marker=found
    with open('Raw/raw{}.txt'.format(n),'w') as w:
        w.writelines(content)
    print(n,marker)
