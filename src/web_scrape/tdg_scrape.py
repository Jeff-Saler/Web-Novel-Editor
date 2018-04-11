import requests
from bs4 import BeautifulSoup

shortlink='https://www.wuxiaworld.com'
link='/novel/tales-of-demons-and-gods/tdg-chapter-1'
for i in range(1,201):
    page=requests.get(shortlink+link)
    soup=BeautifulSoup(page.content,'html.parser')
    content=[]
    for j in list(soup.find(class_='fr-view').children):
        if j.name=='p' and not j.get_text().startswith('Previous') and not j.get_text().startswith('['):
            content.append(j.get_text().strip())
    with open('Translated/Chapter{}.txt'.format(i),'w') as w:
        w.writelines(content)
    link=list(soup.find(class_='next').children)[1].prettify().split('"')[3]
    print(i)
