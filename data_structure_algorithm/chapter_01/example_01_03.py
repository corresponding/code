#!/usr/bin/python
# coding: utf-8

import random

from utils import swap

def perm(list, begin, end):
    if begin == end:
        printout_list = []
        for list_item in list:
            printout_list.append(list_item)
        print printout_list
    else:
        for i in range(begin, end+1):
            swap.swap(list, begin, i)
            #确定begin+1~end之间的排列组合
            perm(list, begin+1, end)
            swap.swap(list, begin, i)

if __name__ == '__main__':
    list = random.sample(range(100), 5)
    perm(list, 0, len(list)-1)