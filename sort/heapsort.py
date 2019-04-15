# coding=UTF-8

def parent(index):
    return int((index-1)/2)

def leftchild(index):
    return 2*index+1

def rightchild(index):
    return 2*index+2

def heap_init(list):
    index=0

    while index < len(list):

        current = index
        p = int((index-1)/2)
        while current > 0 and list[current] > list[p]:
            swap(list, current, p)
            current = p
            p = int((p-1)/2)

        index+=1


def heap_adjust(list, lastindex):
    current = 0
    lc = 2*current+1
    if lc > lastindex:
        return
    rc = 2*current+2
    bigger = lc
    if rc <= lastindex and list[rc] > list[lc]:
        bigger = rc

    if list[current] >= list[bigger]:
        return

    while list[current] < list[bigger]:
        swap(list, current, bigger)
        current = bigger
        lc = 2*current+1
        if lc > lastindex:
            break
        rc = 2*current+2
        bigger = lc
        if rc <= lastindex and list[rc] > list[lc]:
            bigger = rc


# 堆排序，比快排慢
# 先建堆，然后交换堆顶和最后一个数字，再重建堆
def sort(list):

    heap_init(list)

    lastindex = len(list) -1

    while lastindex > 0:
        swap(list, 0, lastindex)
        lastindex -= 1
        heap_adjust(list, lastindex)



def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

# list = [1,6,3,4,5,2,7]


