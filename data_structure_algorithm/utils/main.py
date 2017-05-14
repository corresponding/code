#!/usr/bin/python
# coding: utf-8

import random

from chapter_02 import example_02_16

if __name__ == '__main__':
    origin_list = random.sample(range(100), 30)
    example_02_16.selectionSort(origin_list)