#!/usr/bin/env python
# encoding: utf-8
import jieba
import time
from collections import Counter
time.clock()
with open('test_weicheng.txt','r') as f:
    seg_list = jieba.cut(f.read(),cut_all=True)
# seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
k = 0

print time.clock()
print k

newdict = sorted(dict(Counter(seg_list)).iteritems(),key=lambda a:a[1],reverse=True)

def newhash(source):
    if source == "":
        return 0
    else:
        x = ord(source[0])<<7
        m = 1000003
        mask = 2**128-1
        for c in source:
            x = ((x*m)^ord(c)) & mask
        x ^= len(source)
        if x == -1:
            x = -2
        return x
for i in newdict:
    print len(bin(newhash(i[0]))),len(bin(hash(i[0]))),i[1]