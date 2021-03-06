#!/usr/bin/python
# coding: utf-8

import random

from utils import swap

#及时终止的选择排序
def selection_sort(list):
    for size in reversed(range(len(list))):
        # 设置排序校验
        sorted = True
        #寻找0~size中，最大值的index
        max_order = 0
        for k in range(1, size+1):
            if list[k] > list[max_order]:
                max_order = k
            else:
                sorted = False
        #i位置放置最大值
        swap.swap(list, max_order, size)
        if sorted:
            break

if __name__ == '__main__':
    list = random.sample(range(100), 30)
    selection_sort(list)
    print list