
def perm(list, begin, end):
    if begin == end:
        printout_list = []
        for list_item in list:
            printout_list.append(list_item)
        print printout_list
    else:
        for i in range(begin, end+1):
            swap(list, begin, i)
            # 确定begin+1~end之间的排列组合
            perm(list, begin+1, end)
            swap(list, begin, i)

def swap(list, x, y):
    tmp = list[x]
    list[x] = list[y]
    list[y] = tmp

if __name__ == '__main__':
    perm(['a', 'b', 'c'], 0, 2)