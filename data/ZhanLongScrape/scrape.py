import requests
from bs4 import BeautifulSoup

def main():
    for i in range(13,817):
        link = "http://gravitytales.com/novel/Zhan-Long/zl-chapter-{}".format(i)
        page=requests.get(link)
        soup=BeautifulSoup(page.content, 'html.parser')
        try:
            content = soup.find(class_='innerContent').get_text()
        except:
            AttributeError
            link+='-2'
            page=requests.get(link)
            soup=BeautifulSoup(page.content, 'html.parser')
            try:
                content = soup.find(class_='innerContent').get_text()
            except:
                AttributeError
                print('Chapter {} not scraped'.format(i))
                break
        filename='Chapter{}.txt'.format(i)
        f=open(filename,'w')
        f.write(content)
        f.close()
        print('Scraped Chapter {}'.format(i))

if __name__=='__main__':
    main()
