#!/usr/bin/python
# coding: utf-8

import random

def insert_sort(list):
    result = []
    for i in range(len(list)):
        insert(result, list[i])

def insert(inserted_list, insert_data):
    for i in reversed(range(len(inserted_list))):
        if insert_data >inserted_list[i]:
            inserted_list.insert(i, insert_data)

if __name__ == '__main__':
    list = random.sample(range(100), 30)
    insert_sort(list)
    print list

