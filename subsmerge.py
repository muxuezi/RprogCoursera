# coding: utf-8
import os
os.chdir('sub')

def unit(u):
    with open(u, 'r') as f:
        return f.readlines()


def std(s):
    foo = s.split(' - ')[:2]
    if len(foo[1]) == 1:
        return int('0'.join(foo)), s
    else:
        return int(''.join(foo)), s

news = [k[1] for k in sorted(map(std, os.listdir('.')))]
kk = map(unit, news)
f = open(r'..\allsub.txt', 'w')
for ix, k in enumerate(kk):
    tit = news[ix][:-4]
    print(tit)
    f.write(tit + '\n')
    f.write(' '.join([x.strip() for x in k]))
    f.write('\n\n')
f.close()
