#!/usr/bin/env python
# encoding:utf-8

import os
import simhash
def hamming_distance(simhash_a,simhash_b):
    x = (simhash_a ^ simhash_b) & ((1 << 128) - 1)
    tot = 0
    while x :
        tot += 1
        x &= x - 1
    return tot
def comp(simhash_a,res):
    res = []
    for a,b in res:
        if hamming_distance(simhash_a,b) <= 3:
            res.append([a,b])
    return res