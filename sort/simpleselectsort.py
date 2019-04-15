# coding=UTF-8
# 简单选择排序,比冒泡快
# 每次选择未排序里最小的数和未排序的第一个交换，这样就缩小未排序区域
def sort(list):
    target = 0
    size = len(list)

    while target < size-1:
        src = target
        index = target + 1
        while index < size:
            if list[index] < list[src]:
                src = index
            index += 1

        swap(list, src, target)
        target += 1

def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp