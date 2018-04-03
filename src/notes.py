k=0
for i in range(len(train)):
  if len(train[k])<10:
    del train[k]
  else:
    train[k]=train[k].replace('\\u200b','')
    train[k]=train[k].strip()
    train[k]=train[k].replace('()','')
    k+=1

k=0
for i in range(len(target)):
  if len(target[k])<10:
    del target[k]
  else:
    k+=1

    for i in range(1,201):
        f=open('data/CSGScrape/Translated/Chapter{}.txt'.format(i))
        g=open('data/CSGScrape/Raw_Trans/rt{}.txt'.format(i))
        target=str(f.read().split('\n')).split('.')
        trans=f.read().strip().split('.')
        k=0
        for i in range(len(target)):
            if len(target[k])<10:
                del target[k]
            else:
                k+=1
        k=0
        for i in range(len(trans)):
            if len(trans[k])<10:
                del trans[k]
            else:
                trans[k]=trans[k].replace('\\u200b','')
                trans[k]=trans[k].strip()
                trans[k]=trans[k].replace('()','')
                k+=1
        if len(target)>len(trans):
            while len(target)!=len(trans):
                trans.append('')
        else:
            while len(target)!=len(trans):
                target.append('')
        d=open('traincorp.txt','a')
        for (a,b) in zip(trans,target):
            d.write('{}\t{}\n'.format(a,b))
        d.close()
