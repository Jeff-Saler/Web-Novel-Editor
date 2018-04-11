import requests
from bs4 import BeautifulSoup

def main():
    fail=[]
    http= '896896.html'
    for i in range(1,201):
        link='https://www.piaotian.com/html/2/2072/{}'.format(http)
        page=requests.get(link)
        soup=BeautifulSoup(page.text, 'html.parser')

        a=list(soup.children)[2]
        b=list(a.children)[1]
        c=list(b.children)[34:]
        title= c[0].strip()
        body = c[1].get_text()
        text=title+body
        with open('Raw/raw{}.txt'.format(i),'w') as f:
            f.write(text)
            f.close()

        http=list(soup.children)[8]
        try:
            http=list(http.children)[10].prettify().split('"')[1]
        except:
            AttributeError
            print('Raw {} failed'.format(i))
            fail.append(i)
            pass
        print('Raw {} scraped'.format(i))
    print('Failed: {}'.format(fail))
if __name__=='__main__':
    main()
