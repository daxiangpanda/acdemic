#!/usr/bin/env python
# encoding: utf-8
import os

class fileso:
    def getpath(self,path,filter = []):
        res = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.split('.')[-1] in filter:
                    res.append(os.path.join(root, file))
        return res
