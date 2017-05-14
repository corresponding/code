#!/usr/bin/python
# coding: utf-8

import random

from utils import swap

#及时终止的冒泡排序
def bubble_sort(list):
    for size in reversed(range(len(list))):
        # 设置排序校验
        sorted = True

        i = 0
        for k in range(1, size+1):
            if list[k] < list[i]:
                swap.swap(list, i, k)
                sorted = False
            i = k
        if sorted:
            break

if __name__ == '__main__':
    list = random.sample(range(100), 30)
    bubble_sort(list)
    print list