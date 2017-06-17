#!/usr/bin/python
# coding: utf-8

def move_hanoi(size, from_tower, to_tower, help_tower):
    """
    移动size个碟子
    :param size: 碟子id，从0开始，到size-1
    :param from_tower: 
    :param to_tower: 
    :param help_tower: 
    :return: 
    """
    if size <= 0:
        return
    move_hanoi(size - 1, from_tower, help_tower, to_tower)
    print "move %d from:%d to:%d" % ((size-1), from_tower, to_tower)
    move_hanoi(size - 1, to_tower, to_tower, help_tower)

if __name__ == '__main__':
    move_hanoi(3, 0, 1, 2)