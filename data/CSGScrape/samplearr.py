import numpy as np
from googletrans import Translate

def main():
    t=Translate()
    arr=np.empty((10,2)).astype(list)

    for n,i in enumerate(arr):
        f=open('Raw/raw{}.txt'.format(n+1))
        raw=[]
        for line in f.readlines():
            raw.append(t.translate(line).text)
        i[0]=raw

    for n,i in enumerate(arr):
        f=open('Translated/Chapter{}.txt'.format(n+1))
        body=[]
        for line in f.readlines():
            body.append(line)
        i[1]=body

if __name__=='__main__':
    main()
