#!/usr/bin/env python
# encoding: utf-8

import time
import getpath
start = time.time()

class ShingLing(object):

    cut_step = 5  #切片字长
    text = []
    com_count = 0

    def __init__(self,text1,text2):
        self._cut(text1)
        self._cut(text2)

    def _cut(self,text):
        if len(text) < self.cut_step:
            return

        text = list(text)
        pice_list = []
        for i in range(len(text) - self.cut_step):
            pice = text[i:i + self.cut_step]
            pice_list.append(pice)
        re = {'pice':pice_list,'length':len(text)-self.cut_step}
        self.text.append(re)

    def com(self):
        pice1 = self.text[0]['pice']
        pice2 = self.text[1]['pice']

        for item in pice1:
            if item in pice2:
                self.com_count += 1

        total_length = self.text[0]['length'] + self.text[1]['length']
        com_count = self.com_count*2
        return com_count/float(total_length)


s = ShingLing(text1,text2)
end = time.time()
time = end-start

print 'shingling is:'+str(s.com())
print 'running time:' + str(time)