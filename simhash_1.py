#!/usr/bin/python
# coding=utf-8
import getpath
import time
import os
class simhash:
    
    #构造函数
    def __init__(self, tokens='', hashbits=128):        
        self.hashbits = hashbits
        self.hash = self.simhash(tokens);
    
    #toString函数    
    def __str__(self):
        return str(self.hash)
    
    #生成simhash值    
    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]: #t为token的普通hash值           
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask :
                    v[i] += 1 #查看当前bit位是否为1,是的话将该位+1
                else:
                    v[i] -= 1 #否则的话,该位-1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint #整个文档的fingerprint为最终各个位>=0的和
    
    #求海明距离
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0;
        while x :
            tot += 1
            x &= x - 1
        return tot
    
    #求相似度
    def similarity (self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b : return b / a
        else: return a / b
    
    #针对source生成hash值   (一个可变长度版本的Python的内置散列)
    def _string_hash(self, source):        
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x
             

if __name__ == '__main__':
    time.clock()
    rootdir = r'E:\\'
    dirlist = getpath.fileso().getpath(rootdir,['doc','txt'])
    res = []
    for i in dirlist:
        res.append([i,str(simhash(i.split()))])
    res.sort(key = lambda a: a[1])
    cmp = []
    for i in res:
        if i[1] in cmp:
            print i
            continue
        else:
            cmp.append(i[1])
    print cmp
    print time.clock()
