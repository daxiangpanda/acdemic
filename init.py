#!/usr/bin/env python
# encoding: utf-8

import time
import getpath
import simhash
import os
import cPickle as pickle


time.clock()
rootdir = '/home/ted'
dirlist = getpath.fileso().getpath(rootdir,filter = ['txt','doc'])
print dirlist
res = []
for i in dirlist:
    with open(i,'r') as f:
        content = f.read()
    res.append([i,str(simhash.simhash(content))])
res.sort(key = lambda a: a[1])
with open(os.path.join(os.getcwd(),'result'),'w') as f:
    f.write(pickle.dumps(res))
print time.clock()
